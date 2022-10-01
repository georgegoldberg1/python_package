# python_package

Repo to create a basic python package consisting of modules that can be imported and used on projects.

1. Create folder for package

   - "mypackage/"

2. Create \_\_init\_\_.py (double underscores) file inside package folder

   - "mypackage/\_\_init\_\_.py"

3. Create your_module.py inside package folder

   - "mypackage/my_module.py"

4. Write imports and functions inside your_module.py script

```python
"my_module.py file requires numpy"

import numpy as np

def newfunc(input_x):
    times_three = input_x * 3
    return np.sum([1, times_three])
```

5. Optional: add newfunc to \_\_init\_\_.py file so you can import it directly from the package, instead of via the module:

   - `from .my_module import newfunc`

6. Create script outside package folder and import package contents here to use

   - if step 5 done: `from mypackage import newfunc`
   - if step 5 skipped: `from mypackage.my_module import newfunc`

7. Create setup.py file outside package folder

```python
from setuptools import setup

setup(
    name='mypackage3',
    version='0.1',
    description='test package requiring pandas',
    url='http://github.com/put_your_url_here',
    author='Your Name',
    author_email='xxxxxxx@example.com',
    license='MIT',
    packages=['mypackage'],
    install_requires=['numpy'],
    zip_safe=False
    )
```

8. Build and install the package globally on your system

   - `python setup.py build`
   - `python setup.py install`

9. Push to PyPi (python public publishing index)

   - tbc
