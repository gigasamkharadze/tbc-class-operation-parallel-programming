import time
import concurrent.futures
import random


NUMBER_OF_SAMPLES = 10000
NUMBER_OF_PROCESSES = 5
NUMBER_OF_THREADS_PER_PROCESS = 20


class Trapezoid:
    """
    Class to represent an isosceles trapezoid
    That's a trapezoid with two parallel sides of different lengths
    and two non-parallel sides of equal length.

    parameters:
    a: float
        Length of the first parallel side
    b: float
        Length of the second parallel side
    h: float
        Height of the trapezoid
    """
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return (self.a + self.b) * self.h / 2

    def __str__(self):
        return f'Trapezoid: a={self.a}, b={self.b}, h={self.h}, area={self.area()}'

    def __repr__(self):
        return f'Trapezoid: a={self.a}, b={self.b}, h={self.h}, area={self.area()}'

    def __le__(self, other):
        return isinstance(other, Trapezoid) and self.area() <= other.area()

    def __lt__(self, other):
        return isinstance(other, Trapezoid) and self.area() < other.area()

    def __ge__(self, other):
        return isinstance(other, Trapezoid) and self.area() >= other.area()

    def __gt__(self, other):
        return isinstance(other, Trapezoid) and self.area() > other.area()

    def __eq__(self, other):
        return isinstance(other, Trapezoid) and self.area() == other.area()

    def __ne__(self, other):
        return isinstance(other, Trapezoid) and self.area() != other.area()

    def __add__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() + other.area()
        raise TypeError('Unsupported operand type(s) for +: Trapezoid and {}'.format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() - other.area()
        raise TypeError('Unsupported operand type(s) for -: Trapezoid and {}'.format(type(other)))

    def __mod__(self, other):
        if isinstance(other, Trapezoid):
            return self.area() % other.area()
        raise TypeError('Unsupported operand type(s) for %: Trapezoid and {}'.format(type(other)))


class Rectangle(Trapezoid):
    """
    Class to represent a rectangle
    That's a trapezoid with two parallel sides of equal lengths

    parameters:
    a: float
        Length of the first parallel side
    b: float
        Length of the second parallel side
    """
    def __init__(self, a, b):
        super().__init__(a, b, a)

    def __str__(self):
        return f'Rectangle: a={self.a}, b={self.b}, area={self.area()}'

    def __repr__(self):
        return f'Rectangle: a={self.a}, b={self.b}, area={self.area()}'


class Square(Rectangle):
    """
    Class to represent a square
    That's a rectangle with two parallel sides of equal lengths

    parameters:
    a: float
        Length of the parallel sides
    """
    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return f'Square: a={self.a}, area={self.area()}'

    def __repr__(self):
        return f'Square: a={self.a}, area={self.area()}'


def work(_):
    Trapezoid(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)).area()
    Rectangle(random.randint(1, 10), random.randint(1, 10)).area()
    Square(random.randint(1, 10)).area()


def work_for_process_pool_executor(_):
    global NUMBER_OF_SAMPLES
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUMBER_OF_THREADS_PER_PROCESS) as executor:
        executor.map(work, range(NUMBER_OF_SAMPLES // NUMBER_OF_PROCESSES))


def main():
    global NUMBER_OF_SAMPLES

    # Using ThreadPoolExecutor
    start = time.perf_counter()
    with (concurrent.futures.ThreadPoolExecutor(max_workers=NUMBER_OF_THREADS_PER_PROCESS * NUMBER_OF_PROCESSES)
          as executor):
        executor.map(work, range(NUMBER_OF_SAMPLES))
    finish = time.perf_counter()
    print(f'Using Only ThreadPoolExecutor: {finish - start} seconds')

    # Using ProcessPoolExecutor
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=NUMBER_OF_PROCESSES) as executor:
        executor.map(work, range(NUMBER_OF_SAMPLES))
    finish = time.perf_counter()
    print(f'Using Only ProcessPoolExecutor: {finish - start} seconds')

    # Using ThreadPoolExecutor and ProcessPoolExecutor
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=NUMBER_OF_PROCESSES) as executor:
        executor.map(work_for_process_pool_executor, range(NUMBER_OF_PROCESSES))
    finish = time.perf_counter()
    print(f'Using ThreadPoolExecutor and ProcessPoolExecutor: {finish - start} seconds')


if __name__ == '__main__':
    main()
