class Registry(object):
    __slots__ = ('__params',)

    def __init__(self):

        self.__params = {}

    def __iter__(self):
        return iter(self.__params.items())

    def __setattr__(self, name, value):

        try:

            return super().__setattr__(name, value)

        except AttributeError:
            self.__params[name] = value

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)

        except AttributeError:
            return self.__params.get(attr)

    def __delattr__(self, name):
        try:
            return super().__delattr__(name)

        except AttributeError:
            del self.__params[name]
