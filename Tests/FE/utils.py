from robot.api import logger
from robot.api.deco import keyword
from random import randint
import time


@keyword("Generate Random Number")
def generate_random_number(int_a, int_b):
    """ Generates a random integer within the arguments' values. Returns string """
    number = randint(int(int_a), int(int_b))
    logger.info("generated the number: %s" % str(number))
    return number

@keyword("Convert Int to Time")
def convert_int_to_time(int_a):
    """ Formats value to the stopwatch time format. Returns string """
    timestamp = str(time.strftime('%M:%S', time.gmtime(int_a)))
    logger.info("Pause time: %s" % timestamp)
    return timestamp