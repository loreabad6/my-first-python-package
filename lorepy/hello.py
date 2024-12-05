from emoji import emojize

def hello(name = "world"):
    """Hello function
    
    My function is very nice and says hello to you.
    
    Parameters
    ----------
    name : str
        Who do you want to say hello to?

    Returns
    -------
    str
        A very nice greeting to "name".
    
    Examples
    --------
    >>> lorepy.hello("Lore").
    """
    print("Hello ", name, "! Welcome to my first Python package!", emojize(":wave:"), sep = "")