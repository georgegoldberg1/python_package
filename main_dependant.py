"""script to test the package mypackage3 that has pandas dependencies"""

import numpy as np

from mypackage3.module2 import func_requiring_pandas

arr_x = np.array([2,4,5]) 
arr_y = np.array([1,2,3])

#test the function, without importing pandas here
try:
    func_requiring_pandas(arr_x, arr_y)
    print('it worked! no import needed in the main script')
    
except Exception as exc:
    raise NameError('Could not find pandas, have you imported it?') from exc

print(type(func_requiring_pandas(arr_x, arr_y)))