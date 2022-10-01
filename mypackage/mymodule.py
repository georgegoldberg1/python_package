#mymodule.py inside mypackage

def myfunction(x,y,z=[]):
    """First function inside mypackage.mymodule
    -----
    Desc:
        pre-prends list "z" with product of "x" and "y"
    -----
    Args:
        x:int: integer input called "x"
        y:float: float input called "y"
        z:list: list input called "z"
    -----
    Returns:
        list [x * y] + z
    -----
    Usage:
        extendedlist = myfunction(x=1, y=4.2, z=[20,30,40])
        print(extendedlist)
    """
    return [x * y] + z

def myfunction2(str_text):
    """Second function inside mypackage.mymodule
    -----
    Desc:
        prints string with more verbose output
    -----
    Args:
        str_text:str text to print
    -----
    Returns:
        "Printing string...
            str_text
        "
    -----
    Usage:
        myfunction2("print me")
    """
    print("Printing string...\n\t",str_text, sep='')
    return
