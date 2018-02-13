import time

def pause(sleeptime):
    def decorator(func):
        def wrapper(*args, **kwargs):
            sleep = time.sleep(sleeptime)
            # print('Фунция выполняется с задержкой {} секунды!'.format(sleeptime))
            return func(*args, **kwargs)
        return wrapper
    return decorator
