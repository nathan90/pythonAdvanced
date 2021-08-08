# Asynchronous Programming

1. Latency problem
2. Concurrency and Parallelism
3. Threads in python
4. Short history of AsyncIO
5. Other contemporary frameworks

Main threads and worker threads. Threads take up space in the operating system schedule and memory. We need a way to synchronize them.  
Threads are not independent programs, they share data within the program. If multiple threads change the data at the same time, it will corrupt it  

## The Goal of AsyncIO
* maximize the usage of a single thread
* by handling I/O asynchronously, and 
* by enabling concurrent code using coroutines

AsyncIO avoids blocking functions and uses coroutines

## The Event Loop