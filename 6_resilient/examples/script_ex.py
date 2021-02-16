##################################
# Run script till it gets an error
##################################

import time

time.sleep(2)
raise Exception("Oh no, this script just died")
