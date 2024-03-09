## Multithreading vs Multiprocessing Performance Comparison

The provided Python script demonstrates a comparison between multithreading and multiprocessing techniques for concurrent execution in Python. It utilizes a geometric shape generation task to showcase the performance differences between the two approaches.
We also consider the mixed approach of using multithreading within each process to further improve the performance.
### Overview

The script employs object-oriented programming to define classes representing geometric shapes, including trapezoids, rectangles, and squares. It then utilizes ThreadPoolExecutor and ProcessPoolExecutor from the `concurrent.futures` module to distribute shape generation tasks across multiple threads and processes.

Not only does the script compare the performance of multithreading and multiprocessing, but it also evaluates the scalability of both techniques concerning the number of generated shapes and the available computational resources. The results provide insights into when to use multithreading or multiprocessing based on task characteristics and system constraints.

The task also focuses on the OOP principles, and contains overridden methods like
- `__str__` to provide a string representation of the object
- `__eq__` equality comparison between two objects
- `__lt__` less than comparison between two objects
- `__gt__` greater than comparison between two objects
- `__le__` less than or equal to comparison between two objects
- `__ge__` greater than or equal to comparison between two objects
- `__ne__` not equal comparison between two objects
- `__add__` addition of two objects
- `__sub__` subtraction of two objects
- `__mod__` modulo of two objects

### Key Points

- **Multithreading:** Utilizes ThreadPoolExecutor to execute tasks concurrently within a single Python process, leveraging multiple threads. Ideal for I/O-bound tasks where waiting for external resources is the bottleneck.
- **Multiprocessing:** Employs ProcessPoolExecutor to execute tasks concurrently across multiple Python processes, utilizing separate memory space. Suited for CPU-bound tasks where computational operations dominate.

### Usage

1. Clone the repository.
2. Run the Python script `main.py`.
3. Adjust parameters such as `NUMBER_OF_SAMPLES`, `NUMBER_OF_PROCESSES`, and `NUMBER_OF_THREADS_PER_PROCESS` to explore various scenarios.

### Example

```python
# Adjust parameters for the number of samples,
# processes, and threads
NUMBER_OF_SAMPLES = 100000
NUMBER_OF_PROCESSES = 5
NUMBER_OF_THREADS_PER_PROCESS = 20
```

# Summary
I have run the script on my local machine and the results are as follows:

Sample Size: 10000 \
Number of Processes: 5 \
Number of Threads per Process: 20

- **Only Multithreading:** 0.5725481750014296 seconds
- **Only Multiprocessing:** 3.3681731219985522 seconds
- **Mixed Approach:** 0.22209466800268274 seconds

Sample Size: 100000 \
Number of Processes: 5 \
Number of Threads per Process: 20

- **Only Multithreading:** 7.042422448997968 seconds
- **Only Multiprocessing:** 32.4911008329982 seconds
- **Mixed Approach:** 2.2041477390012005 seconds
