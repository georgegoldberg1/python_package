"""mymodule.py inside mypackage"""

def myfunction(var_x: int,var_y: float,var_z: list|None=None):
    """First function inside mypackage.mymodule
    -----
    Desc:
        pre-prends list "var_z" with product of "var_x" and "var_y"
    -----
    Args:
        var_x: integer input called "var_x"
        var_y: float input called "var_y"
        var_z: list input called "var_z"
    -----
    Returns:
        list [x * y] + z
    -----
    Usage:
        extendedlist = myfunction(var_x=1, var_y=4.2, var_z=[20,30,40])
        print(extendedlist)
    """
    return [var_x * var_y] + var_z

def myfunction2(str_text:str):
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
