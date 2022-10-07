
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.FileHandler('Calcadv_logging.log')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

ch.setFormatter(formatter)
logger.addHandler(ch)


def add(num_a, num_b):
    return num_a + num_b


def sub(num_a, num_b):
    return num_a - num_b


def division(num_a, num_b):
    return num_a / num_b


def remainder(num_a, num_b):
    return num_a % num_b


logger.info('Calc Open')
# some code
logger.info('Calc Closed')
