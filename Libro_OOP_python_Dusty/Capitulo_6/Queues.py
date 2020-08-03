from queue import Queue
#FIFO queues, First In First Out
lineup= Queue(maxsize=3)
#lineup.get(block=False)
lineup.put('one')
lineup.put('two')
lineup.put('three')
#lineup.put('four',timeout=1)
print(lineup.full())
print(lineup.get())
print(lineup.get())
print(lineup.get())
print(lineup.empty())

#LIFO queues,Last In First Out
from queue import LifoQueue
stack = LifoQueue(maxsize=3)
stack.put('one')
stack.put('two')
stack.put('three')
#stack.put('four',block=False)
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.empty())
#stack.get(timeout=1)
