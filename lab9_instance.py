'''
lab9
instance
'''

from lab9_class import my_stat

my_cal_instance = my_stat()

print(my_cal_instance.cal_sigma(5,3))

print(my_cal_instance.cal_pi(5,3))
print(my_cal_instance.cal_f(5))
print(my_cal_instance.cal_p(5,2)) 

import numpy as np
print(np.math.factorial(999))
print(my_cal_instance.cal_f(999))
