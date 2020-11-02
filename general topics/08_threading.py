import threading
import time
import concurrent.futures
# to make a thread we need a function that acts as a thread
# def funct():
#     print('ran')
#     time.sleep(1)
#     print("done")

# x = threading.Thread(target = funct)
# x.start()
# print(threading.activeCount())

# def count(n):
#     for i in range(1, n+1):
#         print(i)
#         time.sleep(0.01)

# for _ in range(2):
#     x = threading.Thread(target=count, args =(10,))
#     x.start()

# print("done")


# Threading is used when we want to speed up our program significantly
# the speedup comes from running different tasks concurrently

# start = time.perf_counter()

# def do_something():
#     print('Sleep for 1 second')
#     time.sleep(1)
#     print('done sleeping')

# do_something()
# do_something()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)')

# cpu bound and io bound tasks
# Cpu bound tasks are using a lot of cpu like crunching a lot of number etc
# Io bound tasks are those waiting for input output operations to be completed eg: reading writing from the file system network operations, downloading stuff online

# We only see most benefits when our tasks are io bound, ie lot of waiting around for input and output operations
# when task is cpu bound its ideal to use mutliprocessing rather than multi threading

# when we run something concurrently using threads, its not actually going to run the code at the same time, it just gives the illusion of running code at the same time because when it comes to point when it is just waiting around, it is just going to move ahead to the next section in the script

#THREADING METHOD
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleep for {seconds} second(s)')
    time.sleep(seconds)
    print('done sleeping')

# t1 = threading.Thread(target= do_something)
# t2 = threading.Thread(target= do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# The join method makes sure that they complete before moving on to calculate the finish time

# Threading in a loop
# threads = []

# for _ in range(10):
#     t = threading.Thread(target= do_something)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()
    
# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)')

# Passing Arguments
# threads = []

# for i in range(10):
#     t = threading.Thread(target= do_something, args= [i])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()
    
# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)')

# USING THREAD POOL EXECUTOR

def do_something1(seconds):
    print(f'Sleep for {seconds} second(s)')
    time.sleep(seconds)
    return f'done sleeping for {seconds} second(s)'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something1, 1)
    # f2 = executor.submit(do_something1, 1)
    # print(f1.result())
    # print(f2.result())
    # For looping
    # results = [executor.submit(do_something1, i) for i in range(10)]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    # USING MAP METHOD IN PYTHON
    secs = [5,4,3,2,1]
    results = executor.map(do_something1, secs)
    
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')


# Threading Advanced - Thread Local Data, Raise Conditions, Thread Locks etc




