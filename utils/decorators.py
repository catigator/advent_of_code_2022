import time
import datetime


def time_it(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        tt = te - ts
        now = datetime.datetime.now()
        print(f"[{now}] Time taken to execute '{method.__name__}' was {tt} seconds")
        return result
    return timed
