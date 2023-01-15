import time
import random
import matplotlib.pyplot as plt
from completbinarytree import MinPriorityQueue

time_used = []
a = []
# Insert n random values into the heap and measure the average consumed time
for i in range(1, 1000):
    pq = MinPriorityQueue()
    random_list = [random.randint(0, 100000) for _ in range(i)]
    start_time = time.time()
    for j in random_list:
        pq.insert(j)
    end_time = time.time()
    time_used.append((end_time - start_time) / i)
plt.plot(time_used)
plt.show()


# Delete the minimum key n times from the heap measure the consumed time
n = 5000
for i in range(500, 1000):
    pq = MinPriorityQueue()
    random_list = [random.randint(0, 100000) for _ in range(i)]
    for j in random_list:
        pq.insert(j)

    start_time = time.time()
    for i in range(n):
        pq.delMin()
    end_time = time.time()
    time_used.append(end_time - start_time)

plt.plot(time_used)
plt.show()

