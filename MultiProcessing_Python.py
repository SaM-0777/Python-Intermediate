# multiprocessing
import multiprocessing as multi
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # Create processes
    for i in range(num_processes - 1):
        p = multi.Process(target=square_numbers)
        processes.append(p)

    # Start Processes
    for p in processes:
        p.start()

    # join
    for p in processes:
        p.join()

    print('end main...')









