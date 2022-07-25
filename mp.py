import multiprocessing as multi
import os
import time


def worker():
    """ print ("Worker!!!") """
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multi.Process(target=worker)
        jobs.append(p)
        p.start()
    for job in jobs:
        job.join()
