def data_types():
    types = [
        (1).__class__.__name__,
        ("I'm string").__class__.__name__, 
        (3.14).__class__.__name__, 
        (1 == 2).__class__.__name__, 
        ([1, 2, 3]).__class__.__name__, 
        ({'name': 'Alise'}).__class__.__name__, 
        ((1, 2, 3)).__class__.__name__, 
        ({1, 2, 3}).__class__.__name__
    ]
    print("["+", ".join(types)+"]")


if __name__ == '__main__':
    data_types()
