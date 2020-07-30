def hello(name=None):
    '''
    >>> hello("Taro")
    'Hello, Taro!'

    >>> hello()
    'Hello!'
    '''

    if name:
        return f"Hello, {name}!"
    else:
        return "Hello!"
