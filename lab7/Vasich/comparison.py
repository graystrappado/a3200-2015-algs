from lab4.Vasich.combine_sort import merge_sort
from lab5.Vasich.quicksort import quicksort
from lab6.Vasich.radix_sort import radix_sort
from lab7.Vasich.generators import *
from time import time
import pylab


# almost completely stolen from vks
def grade(sort_func, array_generator, size):
    millis = 0.0
    for i in range(5):
        array = array_generator(size)
        t1 = time()
        sort_func(array)
        t2 = time()
        millis += t2 - t1
    millis /= 5.0
    return millis


funcs = dict()
funcs["Combined sort"] = lambda x: merge_sort(x, 0, len(x))
funcs["Quick sort"] = lambda x: quicksort(x, 0, len(x))
funcs["Radix sort"] = lambda x: radix_sort(x)
funcs["Standard sort"] = sorted


arrs = dict()
arrs["Random array (-1000000 to 1000000)"] = lambda x: random_array(-1000000, 1000001, x)
arrs["Random array (0 to 10000)"] = lambda x: random_array(0, 10001, x)
arrs["Semi-sorted array (0 to 10000)"] = lambda x: semi_sorted_array(0, 10001, x)
arrs["Ascending sorted array (0 to 10000)"] = lambda x: ascending_sorted_array(0, 10001, x)
arrs["Descending sorted array (0 to 10000)"] = lambda x: descending_sorted_array(0, 10001, x)
arrs["Array of repeating values"] = lambda x: same_value_array(-100000, 100001, x)

sizes = [100 + 100000 * i for i in range(6)]
current = 1

for gen_name, gen in arrs.items():
    pylab.subplot(2, 3, current)
    pylab.xlabel("size, elements")
    pylab.ylabel("time, sec")
    print("Now passing: %s" % gen_name)
    for func_name, func in funcs.items():
        millis = []
        for size in sizes:
            print("\tUsing %s on array of size %s" % (func_name, size))
            millis.append(grade(func, gen, size))
        print("\n\t***\n")
        pylab.plot(sizes, millis, label=func_name)
    pylab.title(gen_name)
    pylab.legend(loc='upper left', title="Sorts")
    current += 1

pylab.show()
