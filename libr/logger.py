import logging

# Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
level_logging = logging.INFO

logging.basicConfig(filename="mylog.log",format = u'# %(levelname)-8s [%(asctime)s]  %(message)s',level = level_logging)


def format_logging_debug(message='debug'):
    return logging.debug( message )


def format_logging_info(message='info'):
    return logging.info( message)


def format_logging_warning(message='warning'):
    return logging.warning( message)


def format_logging_error(message='error'):
    return logging.error( message )


def format_logging_critical(message='critical'):
    return logging.critical( message)

