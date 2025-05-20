import asyncio
import argparse
from pathlib import Path
from aiopath import AsyncPath
from aioshutil import copyfile
import logging.config
from file_sorting.logging_config import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('sorting')


async def read_folder(path, new_path, memo=None, indent="  "):
    if memo is None:
        memo = set()

    async for el in path.iterdir():
        if await el.is_dir():
            await read_folder(el, new_path, memo, indent + "  ")
        else:
            file_key = str(await el.resolve())
            if file_key not in memo:
                memo.add(file_key)
                await copy_file(el, new_path)


async def copy_file(current_path, new_path):
    directory_name = current_path.suffix[1:]
    new_path_directory = new_path / directory_name
    destination = new_path_directory / current_path.name
    if not await new_path_directory.exists():
        await new_path_directory.mkdir(exist_ok=True, parents=True)
    try:
        if not await destination.exists():
            await copyfile(current_path, destination)
            logger.info(f"Copied: {current_path} -> {destination}")
        else:
            logger.info(f'Skipped (already exists): "{destination}"')
    except Exception as e:
        logger.error(f"Error while copying {current_path}: {e}")


async def main():
    parser = argparse.ArgumentParser(description="Sort files by extension")
    parser.add_argument("source", help="Path to the source folder")
    parser.add_argument("output", help="Path to the destination folder")
    args = parser.parse_args()

    source_path = Path(args.source)
    output_path = Path(args.output)

    source_apath = AsyncPath(f'{source_path}')
    output_apath = AsyncPath(f'{output_path}')
    
    await read_folder(source_apath, output_apath)
    logger.info("Copying completed.")
    logger.info(f"Source: {args.source}")
    logger.info(f"Destination: {args.output}")


if __name__ == '__main__':
    asyncio.run(main())