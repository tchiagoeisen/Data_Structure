from node import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    

  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print('Adding "{0}" to the queue!'.format(item_to_add.get_value()))

      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1

    else:
      print("Sorry, no more room!")


  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print('Removing "{0}" from the queue!'.format(item_to_remove.get_value()))

      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    
    else:
      print("The queue is empty!")
  

  def peek(self):
    if self.size > 0:
      return self.head.get_value()
    else:
      print("No orders waiting!")
  

  def print_queue(self):
    if self.size == 0:
      print('There is no queue!')
      return 'There is no queue!'
    
    queue_list = ''
    current_item = self.head

    for i in range(self.size):
      if i == self.size - 1:
        queue_list += current_item.get_value()
      else:
        queue_list += current_item.get_value() + ' => '
      current_item = current_item.get_next_node()

    print('The first item in the queue is "{0}".\nQueue: {1}'.format(self.head.get_value(), queue_list))
    
    return queue_list
  

  def get_size(self):
    return self.size
  

  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
    
  def is_empty(self):
    return self.size == 0

