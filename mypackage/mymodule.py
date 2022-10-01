"""mymodule.py inside mypackage"""

def myfunction(var_x: int,var_y: float,var_z: list|None=None) -> list:
    """First function inside mypackage.mymodule
    pre-prends list "var_z" with product of "var_x" and "var_y"

    Args:
        var_x (int): first input
        var_y (float): second input
        var_z (list | None, optional): a list input. Defaults to None.

    Returns:
        list: list [x * y] + z

    Useage:
        extendedlist = myfunction(var_x=1, var_y=4.2, var_z=[20,30,40])
        print(extendedlist)
    """
    return [var_x * var_y] + var_z

def myfunction2(str_text:str) -> None:
    """Second function inside mypackage.mymodule

    prints string with more verbose output

    Args:
        str_text (str): _description_

    Usage:
        myfunction2("print me")
    """
    print("Printing string...\n\t",str_text, sep='')
    return
