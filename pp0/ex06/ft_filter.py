def ft_filter(function, iterable):
    """
    Recode of Python built-in filter function
    """
    if function is None:
        return (x for x in iterable if x)
    else:
        return (x for x in iterable if function(x))
