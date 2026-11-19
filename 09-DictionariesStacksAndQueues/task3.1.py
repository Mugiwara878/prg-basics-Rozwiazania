###
# Modified stack example: push numbers, sum last two, sum the rest
#
import queue

numbers = queue.LifoQueue()
for n in [2, 3, 7, 4, 1, 9, 8]:
    numbers.put(n)                              # dodaje kolejno na WIERZCH stosu

# .get() na LifoQueue zawsze zdejmuje OSTATNIO dodany element (LIFO)
last_two_sum = numbers.get() + numbers.get()    # zdejmuje 8, potem 9 (odwrotna kolejnosc dodania)
print('Sum of last two:', last_two_sum)

remaining_sum = 0
while not numbers.empty():                      # dopoki stos nie jest pusty
    remaining_sum += numbers.get()               # zdejmuj i sumuj reszte
print('Sum of remaining:', remaining_sum)