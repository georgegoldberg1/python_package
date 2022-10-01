"""script to test the package mypackage"""

print("Importing 'myfunction' indirectly from 'mymodule', within 'mypackage'")
from mypackage.mymodule import myfunction as test1

print("Importing 'myfunction' directly from 'mypackage2'")
from mypackage2 import myfunction as test2

try:
    print("Attempting to import 'myfunction' directly from 'mypackage' as we did with 'mypackage2' where the function is declared in the __init__.py file")
    from mypackage import myfunction as test3

except Exception as exc:
    raise ImportError("Could not import 'myfunction' directly from 'mypackage', is it declared in the __init__.py file as 'from .mymodule import myfunction'?") from exc

print("Running 'myfunction' from 'mymodule', within 'mypackage'")
print(test1(2,4.5,[3.5,2.3]))

print("Running 'myfunction' directly from mypackage2")
print(test2(2,4.5,[3.5,2.3]))
