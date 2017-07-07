import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_time_of_execution(f):
    """ Decorator to get time of execution of any method inside a class. """

    def wrapped(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        logger.info("Computing time to " + f.__name__ + " (in seconds): " + str(time.time() - start_time))
        return res

    return wrapped