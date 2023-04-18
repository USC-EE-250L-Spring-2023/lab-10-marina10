# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Marina Braga
- team member 2

## Lab Question Answers

Question 1: Under what circumstances do you think it will be worthwhile to offload one or both
of the processing tasks to your PC? And conversely, under what circumstances will it not be
worthwhile?

Answer: It will, because the processor of my computer is way more potent than the RiPi so when testing my code it is better to use it so I can get my results earlier

Question 2: Why do we need to join the thread here?

Answer: Because we will use the result of the operation in the next line, so we need to wait for its result


Quetion 3: Are the processing functions executing in parallel or just concurrently? What is the difference?

Answer: Only concurrently as the code doesn't split a task in several sub-tasks as it would in parallel,  it only executes them simultaneously using threads
Used chatGPT to answer this question


Question 4: What is the best offloading mode? Why do you think that is?

Answer: forkserver, because it is not as slow as spawn and it doesn't inherit unecessary processes as in fork


Question 5: What is the worst offloading mode? Why do you think that is?

Answer: Spawn, because it is slower than the others


Question 6: The processing functions in the example aren't very likely to be used in a real-world application. What kind of processing functions would be more likely to be used in a real-world application? When would you want to offload these functions to a server?

Answer: 


Sources:

Programiz - Python int()
Geeks for geeks - numpy.mean() in Python
                -numpy.sqrt() in Python
NumPy - numpy.sqrt()
W3 Schools - Python operators
           - Python all() Function
Super Fast Python - How to join a thread in python
Stack Overflow - Save plot to image file instead of displaying it
ChatGPT - Please give me a brief explanation of the difference between parallel and concurrent execution
Python.org - multiprocessing - Process-based parallelism


