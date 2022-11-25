def read(dir):
    '''Open file from directory'''
    with open(dir, 'r') as f:
        result = f.read()
    return result