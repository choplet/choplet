
from collections import namedtuple, OrderedDict

def return_namedtuple(*argums):
    def decorator(fn):
        def wrapped(*args,**kwargs):
            result = fn(*args,**kwargs)
            if isinstance(result, tuple):
                testup = namedtuple("tup",list(argums))
                custom = testup(*result)
            return result
            return custom
        return wrapped
    return decorator





'''
@return_namedtuple("adin", "adiin")
def hello():
    return ("hello habr","hello")

print (hello())

'''







'''
def makeitalic(fn):
    def wrapped(*args,**kwargs):
        testup = namedtuple("tup","a")
        custom = testup(fn(*args,**kwargs))
        return custom
    return wrapped

#@makebold
@makeitalic
def hello():
    return "hello habr"

print (hello())
'''
