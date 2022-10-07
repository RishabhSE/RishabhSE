"""
Topics
1. Simple printing
2. Logging Levels
3. Advance Logging

"""

# Making num_a calculator

from calculator import add,sub,division,remainder

num_a = 10
num_b = 2

print( f"The result after addition is {add(num_a, num_b)}")
print( f"The result after subtraction is {sub(num_a, num_b)}")
print( f"The result after division is {division(num_a, num_b)}")
print( f"The result after remainder is {remainder(num_a, num_b)}") 












# *********************************************************************************************



import logging
from calculator import add,sub,division,remainder

num_a = 10
num_b = 2

# Change it to warning(default)
logging.warning( f"The result after addition is {add(num_a, num_b)}")
logging.warning( f"The result after subtraction is {sub(num_a, num_b)}")
logging.warning( f"The result after division is {division(num_a, num_b)}")
logging.warning( f"The result after remainder is {remainder(num_a, num_b)}") 



 
 
 
 
 
# *********************************************************************************************
# Changing logging configurations, filename, format

from calculator import add,sub,division,remainder

import logging
import time

logging.basicConfig(level= logging.INFO,
                    filename= 'test.log',
                    format= '%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    )

num_a = 40
num_b = 3


logging.info( f"The result after addition is {add(num_a, num_b)}")
logging.info( f"The result after subtraction is {sub(num_a, num_b)}")
logging.info( f"The result after division is {division(num_a, num_b)}")
logging.info( f"The result after remainder is {remainder(num_a, num_b)}") 

# *********************************************************************************************

# filename= 'test.log',
# format= '%(asctime)s:%(levelname)s:%(message)s',
# datefmt='%d-%b-%y %H:%M:%S'
# format= '%(relativeCreated)d:%(levelname)s:%(process)d:%(message)s',

# to capture stack trace
# logging.error("Exception occurred", exc_info=True)
# logging.exception()











# *********************************************************************************************

# Advanced logging
# Importing module


import logging
import calculator

logging.basicConfig(level= logging.INFO,
                    filename="logging_test.log",
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
                    )

logging.info('loggin_demo Start')
# some code
logging.info('loggin_demo End')



print(__name__)










# *********************************************************************************************

"""
The logging library takes a modular approach

1. Loggers
2. Filters
3. Handlers 
4. Formatters 

"""



import logging

# step 1 :
# Creating a logger
logger = logging.getLogger(__name__)
# Set log level
logger.setLevel(logging.INFO)

# step 2 :
# Creating a handler
# fl = logging.FileHandler('adv_logging.log ')
ch = logging.StreamHandler()

# step 3 :
# Create formatter
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')


# step 4 :
# add the formatter to handler
ch.setFormatter(formatter)

# step 5 :
# add handler to logger
logger.addHandler(ch)


logger.info('This is a warning')











# *********************************************************************************************





import logging
import calc_adv

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.FileHandler('loogin_adv.log')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

ch.setFormatter(formatter)
logger.addHandler(ch)

# logging.basicConfig(level= logging.INFO,
#                     filename="logging_test.log",
#                     format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
#                     )

logger.info('loggin_demo Start')
# some code
logger.info('loggin_demo End')
