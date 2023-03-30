import logging

LOG_FILE_PATH = "../app.log"
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
KEEP_NUM_LINES = 1000


def log_func(level: int = 10, *args, **kwargs) -> logging.Logger:

    logger = logging.getLogger()
    logger.setLevel(level)

    handler = logging.FileHandler(LOG_FILE_PATH)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(handler)

    with open(LOG_FILE_PATH, "r+") as lf:
        lines = lf.readlines()

        if len(lines) > KEEP_NUM_LINES:
            lf.seek(0)
            lf.truncate()
            lf.writelines(lines[-KEEP_NUM_LINES:])

    logging.basicConfig(filename=LOG_FILE_PATH,
                        level=level,
                        format=LOG_FORMAT)

    return logger
