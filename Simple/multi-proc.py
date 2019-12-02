import os
from multiprocessing import Process, current_process, Lock, Pool

# http://python-3.ru/page/multiprocessing
# Simple multi-process
# def doubler(number):
#     result = number * 2
#     proc = os.getpid()
#     proc_name = current_process().name
#     print('{0} doubled to {1}; by process id: {2}; process name {3}'.format(
#         number, result, proc, proc_name))
#
# if __name__ == '__main__':
#     numbers = [5, 10, 15, 20, 25]
#     procs = []
#
#     for index, number in enumerate(numbers):
#         proc = Process(target=doubler, args=(number,))
#         procs.append(proc)
#         proc.start()
#
#     proc = Process(target=doubler, name='Test', args=(2,))
#     proc.start()
#     procs.append(proc)
#
#     for proc in procs:
#         proc.join()

def doubler(number):
    return number * 2

if __name__ == '__main__':
    numbers = [5, 10, 20]
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))