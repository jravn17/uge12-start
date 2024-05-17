

''' Singleton class for database connection.
This ensures that the connection is not changed if the class is instanced multiple times
with different parameters. '''


class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs) -> object:
        # if the instance is instanced again return the first reference
        if cls not in cls._instances:
            # safe the reference to the instance when it is instanced first time
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]