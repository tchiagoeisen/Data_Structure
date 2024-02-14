from node import Node

class Stack:
  def __init__(self, name, limit = 1000):
    self.size = 0
    self.top_item = None
    self.limit = limit
    self.name = name
  

  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print('The item "{0}" has been added to "{1}".\n'.format(self.top_item.get_value(), self.name))
    else:
      print("Stack is full!")


  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print('The top item "{0}" has been removed.\n'.format(item_to_remove.get_value()))
      return item_to_remove.get_value()
    print('Stack "{0}" is empty.\n'.format(self.name))


  def peek(self):
    if self.size > 0:
      print('The top item is "{0}".\n'.format(self.top_item.get_value()))
      return self.top_item.get_value()
    print('No item in "{0}" found!\n'.format(self.name))


  def has_space(self):
    return self.limit > self.size


  def is_empty(self):
    return self.size == 0
  

  def get_size(self):
    return self.size
  

  def get_name(self):
    return self.name
  
  
  def print_stack(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print('Stack name: {0} \nStack limit: {2}\n{0}: {1}\n'.format(self.get_name(), print_list, self.limit))

  

