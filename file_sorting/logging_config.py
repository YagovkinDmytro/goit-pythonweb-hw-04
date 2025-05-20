LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detailed',
        },
        'file_sorting': {
            'class': 'logging.FileHandler',
            'filename': 'sorting.log',
            'mode': 'a',
            'level': 'DEBUG',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'sorting': {
            'handlers': ['console', 'file_sorting'],
            'level': 'DEBUG',
            'propagate': False
        },  
    }
}