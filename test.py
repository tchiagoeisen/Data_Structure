from linkedlist import LinkedList
from stack import Stack
from queue import Queue

print('########## LinkedList ##########')
demo = LinkedList(0)
print('Create a LinkedList:' + '\n' + demo.string_linkedlist() + '\n')

for i in range(1,6):
  demo.insert_beginning(i)
print('Insert beginning from 1 to 5:' + '\n' + demo.string_linkedlist() + '\n')

for i in range(-1,-6,-1):
  demo.insert_end(i)
print('Insert end from -1 to -5:' + '\n' + demo.string_linkedlist() + '\n')

print('Get head Node:')
print(demo.get_head_node().get_value())

print('\n' + 'Get last Node:')
print(demo.get_last_node().get_value())

demo.replace_node(0,100)
print('\n' + 'Replace node 0 => 100:' + '\n' + demo.string_linkedlist() + '\n')

demo.remove_node(-1)
print('Remove node -1:' + '\n' + demo.string_linkedlist() + '\n')

print('Count node in linkedlist:')
demo.count_linkedlist()

print('\n' + 'Sum all nodes:')
demo.sum_all_nodes()

print('\n' + 'Reverse linkedlist:' + '\n' + demo.reverse_linked_list())

#If Node does not exist in the list
print(' ')
demo.remove_node(500)
print(' ')
demo.replace_node(1000,100)


########## Stack ##########
print('')
print('########## Stack ##########')
print('Creating Stack...')
my_stack = Stack('MyStack', 5)

my_stack.print_stack()

print('Adding items...')
for i in range(1,6):
  my_stack.push(i)

my_stack.print_stack()

print('Peek top item...')

my_stack.peek()

print('Removing items...')
while my_stack.get_size() > 0:
  my_stack.pop()

my_stack.print_stack()


########## Queue ##########

print('########## Queue ##########')
print('Creating a Queue with a max of 10 items...')
my_queue = Queue(10)

my_queue.enqueue("1")
my_queue.enqueue("2")
my_queue.enqueue("3")
my_queue.enqueue("4")
my_queue.enqueue("5")

print('')
my_queue.print_queue()
print('')

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

'''
########## LinkedList ##########
Create a LinkedList:
0

Insert beginning from 1 to 5:
5 -> 4 -> 3 -> 2 -> 1 -> 0

Insert end from -1 to -5:
5 -> 4 -> 3 -> 2 -> 1 -> 0 -> -1 -> -2 -> -3 -> -4 -> -5

Get head Node:
5

Get last Node:
-5

Replace node 0 => 100:
5 -> 4 -> 3 -> 2 -> 1 -> 100 -> -1 -> -2 -> -3 -> -4 -> -5

Remove node -1:
5 -> 4 -> 3 -> 2 -> 1 -> 100 -> -2 -> -3 -> -4 -> -5

Count node in linkedlist:
Number of Nodes = 10.

Sum all nodes:
The sum of all node is 101.

Reverse linkedlist:
-5 -> -4 -> -3 -> -2 -> 100 -> 1 -> 2 -> 3 -> 4 -> 5

Node "500" not found! Not possible to remove!

Node "1000" not found! Not possible to replace!

########## Stack ##########
Creating Stack...
Stack name: MyStack
Stack limit: 5
MyStack: []

Adding items...
The item "1" has been added to "MyStack".

The item "2" has been added to "MyStack".

The item "3" has been added to "MyStack".

The item "4" has been added to "MyStack".

The item "5" has been added to "MyStack".

Stack name: MyStack
Stack limit: 5
MyStack: [1, 2, 3, 4, 5]

Peek top item...
The top item is "5".

The top item "5" has been removed.

The top item "4" has been removed.

The top item "3" has been removed.

The top item "2" has been removed.

The top item "1" has been removed.

Stack name: MyStack
Stack limit: 5
MyStack: []

########## Queue ##########
Creating a Queue with a max of 10 items...
Adding "1" to the queue!
Adding "2" to the queue!
Adding "3" to the queue!
Adding "4" to the queue!
Adding "5" to the queue!

The first item in the queue is "1".
Queue: 1 => 2 => 3 => 4 => 5

Removing "1" from the queue!
Removing "2" from the queue!
Removing "3" from the queue!
Removing "4" from the queue!
Removing "5" from the queue!

'''