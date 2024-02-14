from node import Node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  

  def get_head_node(self):
    return self.head_node
  

  def get_last_node(self):
    current_node = self.head_node
    
    while current_node: 
      if current_node.get_next_node() == None:
         return current_node  
         
      current_node = current_node.get_next_node()
  

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node


  def insert_end(self, new_value):
    current_node = self.head_node
    
    while current_node: 
      if current_node.get_next_node() == None:
         new_end = Node(new_value)
         current_node.set_next_node(new_end)
         break
         
      current_node = current_node.get_next_node()


  def string_linkedlist(self):
    string_list = ""
    current_node = self.head_node

    while current_node: 
      if current_node == self.head_node:
        string_list += str(current_node.value) 
        current_node = current_node.get_next_node()
      else:
        string_list += " -> " + str(current_node.value) 
        current_node = current_node.get_next_node()
      
    return string_list
  

  def remove_node(self, value_to_remove):
    current_node = self.head_node

    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()

    else:
      while current_node:
        next_node = current_node.get_next_node()

        if next_node.get_value() == value_to_remove:
          current_node.next_node = next_node.get_next_node()
          current_node = None
        else:
          current_node = next_node

          if next_node.get_next_node() == None:
            print(f'Node "{value_to_remove}" not found! Not possible to remove!')
            
            return value_to_remove  
  

  def replace_node(self,node_to_replace = None, new_value = None):
    current_node = self.head_node

    if current_node.get_value() == node_to_replace:
      current_node.value = new_value
    
    elif current_node.get_next_node() == None: 
      print(f'Node "{node_to_replace}" not found! Not possible to replace!')

      return node_to_replace
    
    else:
      while current_node:
        next_node = current_node.get_next_node()

        if next_node.value == node_to_replace:
          next_node.value = new_value  
          break
        else:
          current_node = next_node

          if next_node.get_next_node() == None:
            print(f'Node "{node_to_replace}" not found! Not possible to replace!')

            return node_to_replace


  def count_linkedlist(self):
    counter = 0
    current_node = self.head_node
    
    while current_node:
      counter += 1
      next_node = current_node.get_next_node()
      current_node = next_node

    print(f'Number of Nodes = {counter}.')

    return counter


  def sum_all_nodes(self):
    sum_nodes = 0
    current_node = self.head_node

    while current_node: 
      if type(current_node.value) == int:
        sum_nodes += current_node.value
        current_node = current_node.get_next_node()
      else:
        current_node = current_node.get_next_node()
    print(f'The sum of all node is {sum_nodes}.')

    return sum_nodes
  
  
  def reverse_linked_list(self):
    current_node = self.head_node
    reverse = []

    while current_node: 
      reverse.append(current_node.get_value())
      if current_node.get_next_node() == None:
         new_linkedlist = LinkedList(current_node.get_value())
         reverse.pop(-1)
         break   
      current_node = current_node.get_next_node()   

    for i in reverse[::-1]:
      new_linkedlist.insert_end(i)
      
    return new_linkedlist.string_linkedlist()
  