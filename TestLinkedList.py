#  File: TestLinkedList.py

#  Description: writing various helper methods for singly linked lists 

#  Student Name: Aiman Lakhani

#  Student UT EID: al54554

#  Partner Name: Parul Gupta

#  Partner UT EID: pg25945 

#  Course Name: CS 313E

#  Unique Number: 58023

#  Date Created: 3/27/2023

#  Date Last Modified: 3/30/2023

class Link (object):
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.first = None

  # get number of links 
  def get_num_links (self):
    count = 0 
    curr = self.first
    while(curr):
      count += 1
      curr = curr.next
    return count 
  
  # add an item at the beginning of the list
  def insert_first (self, data):
    new_link = Link(data)
    new_link.next = self.first
    self.first = new_link 

  # add an item at the end of a list
  def insert_last (self, data): 
    new_link = Link(data)
    current = self.first 
    if(current == None):
        self.first = new_link 
        return 
    while(current.next != None):
        current = current.next
    # now you are at the last 
    current.next = new_link

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
    new_link = Link(data)
    if(not self.first):
      self.first = new_link
      return 
    curr = self.first
    prev = self.first
    while(new_link.data > curr.data and curr != None):
      prev = curr
      curr = curr.next
      if(curr == None):
        break
    # if the data is greater than everything else
    if(curr == None):
      prev.next = new_link
      return
    # previous is less than the data and curr is greater than the data
    prev.next = new_link
    new_link.next = curr

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    curr = self.first
    if(not curr):
      return None
    while (curr.data != data):
      if(curr.next == None):
        return None
      curr = curr.next
    return curr

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    curr = self.first

    if(not curr):
      return None
    while(curr.data != data):
      if(curr.next == None):
        return None
      # this means that we've skipped over where data would be
      elif(curr.data > data):
        return None
      curr = curr.next  
    return curr

  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
    prev = self.first
    curr = self.first
    if(not curr):
      return None
    
    while(curr.data != data):
      if(curr.next == None):
        return None
      prev = curr
      curr = curr.next
    if (curr == self.first):
      self.first = curr.next
    # delete the node by re assingings previous' pointer
    else:
      prev.next = curr.next
    return curr

  def __str__ (self):
    s = ""
    curr = self.first
    count = 1
    while(curr):
      # so we only print 10 numbers per line
      if(count % 10 != 0): 
        if(curr.next == None):
            s += str(curr.data)
        else:
            s += str(curr.data) + "  "
      elif(count % 10 == 0):
        s += str(curr.data) 
        if (curr.next != None): 
            s += "\n"
      curr = curr.next
      count += 1
    return s

  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
    new_list = LinkedList()
    if(self.first == None):
        return LinkedList()
    curr = self.first 
    while(curr): 
        # put the link in the last node of the new list
        new_list.insert_last(curr.data)
        curr = curr.next
    return new_list

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self): 
    if(self.first == None):
        return None
    
    newList = LinkedList()
    curr = self.first
    while(curr != None):
        # put the next elements in the first position in the new list
        newList.insert_first(curr.data)
        curr = curr.next
    return(newList)

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
    new_list = LinkedList()
    if (self.first == None):
        return new_list
     
    # make a copy that we can delete links from once we use them
    copy = self.copy_list()
    mini = copy.first
    curr = copy.first
    # find what goes first in the newlist
    while(curr):
      if(curr.data < mini.data):
        mini = curr
      curr = curr.next
    new_list.first = Link(mini.data)
    copy.delete_link(mini.data)
    
    new_curr = new_list.first
    # while there are still elements that need to be sorted
    while(not copy.is_empty()):
      curr = copy.first 
      mini = copy.first 
      while(curr):
        if(curr.data < mini.data):
          mini = curr
        curr = curr.next
      new_curr.next = Link(mini.data)
      new_curr = new_curr.next
      copy.delete_link(mini.data)
    
    return new_list

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    curr = self.first
    # if the list is zero or one element
    if(not curr):
      return True
    elif(curr.next == None):
      return True 
    while(curr.next.data > curr.data):
      if(curr.next.next == None):
        return True
      curr = curr.next
    return False

  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    return not self.first
  
  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
    new_list = LinkedList()
    curr1 = self.first
    curr2 = other.first
    if(curr1.data < curr2.data):
      new_link = Link(curr1.data)
      curr1 = curr1.next
    else:
      new_link = Link(curr2.data)
      curr2 = curr2.next
    new_list.first = new_link
    new_curr = new_list.first

    while(curr1 or curr2):
      # if one has elements and not the other
      if(curr1 and not curr2):
        new_curr.next = Link(curr1.data)
        curr1 = curr1.next
      elif(curr2 and not curr1):
        new_curr.next = Link(curr2.data)
        curr2 = curr2.next
      # compare the data to see which is less
      elif(curr1.data < curr2.data):
        new_curr.next = Link(curr1.data)
        curr1 = curr1.next
      else:
        new_curr.next = Link(curr2.data)
        curr2 = curr2.next
      new_curr = new_curr.next
    
    return new_list

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    if(self.first == None and other.first == None):
        return True 
    
    curr1 = self.first
    curr2 = other.first
    while(curr1 != None and curr2 != None): 
        if(curr1.data != curr2.data):
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    return True 
    
  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
    if(self.first == None):
        return None
    curr = self.first
    new_list = LinkedList()
    while(curr != None): 
        # if we can't find the node in the list, then insert it
        if(new_list.find_unordered(curr.data) == None):
            new_list.insert_last(curr.data)
        curr = curr.next
    return new_list

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
    linked = LinkedList()
    linked.first = Link(0)
    curr = linked.first
    for i in range(1,20):
        curr.next = Link(i)
        curr = curr.next
    print(linked, 1)
  # Test method insert_last()

  # Test method insert_in_order()

  # Test method get_num_links()

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 

  # Test method copy_list()

  # Test method reverse_list()

  # Test method sort_list()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  # Test method is_empty()

  # Test method merge_list()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Test remove_duplicates()

if __name__ == "__main__":
  main()