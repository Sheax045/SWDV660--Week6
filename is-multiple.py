import logging
import logstash


logger = logging.getLogger('python-logstash-log')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.LogstashHandler('54.198.127.153', 5959, version=1))

#formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
#logger.setFormatter(formatter)
#could not get to work

def is_multiple(n, m):
    
    if m == 0:
        logger.error('Error: tried to divide by 0')
    elif n % m == 0:
        message = 'True, {} is a multiple of {}'.format(n,m)
        logger.info(message)
    else:
        message = 'False, {} is not a multiple of {}'.format(n,m)
        logger.warning(message)
        
    

is_multiple(1, 2)
is_multiple(2, 3)
is_multiple(3, 4)
is_multiple(0, 4)
is_multiple(6, 2)
is_multiple(9, 3)
is_multiple(12, 4)
is_multiple(12, 0)
