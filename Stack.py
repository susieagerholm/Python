class Stack:
    def __init__(self, my_string):
        self.my_list = LinkedList()
        self.my_string = my_string
        
    
    def checkBalance(self):
        curr_position = position_first_open = 0
        open = ['(', '[', '{']
        close = [')', ']', '}']   
                
        for char in self.my_string:
            curr_position += 1
            if char in open:
                if self.my_list.empty():
                    position_first_open = curr_position
                self.my_list.pushTop(char)
            elif char in close:
                print("In remove with " + char)
                if char == ')' and self.my_list.getTop() != '(':
                    print (str(curr_position) + " : " + char + " : " + self.my_list.getTop())
                    exit()
                elif char == ']' and self.my_list.getTop() != '[':
                    print (str(curr_position) + " : " + char + " : " + self.my_list.getTop())
                    exit()
                elif char == '}' and self.my_list.getTop() != '{':
                    print (str(curr_position) + " : " + char + " : " + self.my_list.getTop())
                    exit()
                else:
                    self.my_list.popTop()               
        if self.my_list.empty() is not True:
            print ("Checking if list is empty...") 
            print (self.my_list.empty())
            
        else:
            print ('Success')   
            self.my_list.printLinkedList()          


class LinkedList:
 
  def __init__(self):
    self.head = self.tail = None
    
  def empty(self):
    if self.head is None:
      return True
    else:
      return False 
      
  def pushTop(self, item):
    newNode = Node(item, None) 
    #print('New node created: ' + item )
    if self.head is None:      # if linked list is empty
        self.head = newNode
        self.tail = newNode
        print('New node added to stack: ' + item )
    else:
        newNode.next = self.head
        self.head = newNode
        print('New node added to stack: ' + item )     
  
  def getTop(self):
      return self.head.value
      
      
  def popTop(self):
    if self.head is not None:  # if linked list is not empty
      top = self.head
      if top.next is not None: # check if there is next Node in list
        self.head = top.next
      else:                    # reset linked list to empty state if no next Node
        self.head = None
        self.tail = None
      print('New node removed from stack: ' + top.value)    
      return top    
    else:
      return None

  def printLinkedList(self):
    if self.empty:
        print("List is empty")
    else:
        curr_node = self.head
        while (curr_node is not None):
            print (curr_node.value)
            if curr_node.next is None:
                break
            else:
                curr_node = curr_node.next      
        
  '''No further operations need to be implemented on LinkedList in order
  to perform as a Stack...'''       
    
        
class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next
 

 
if __name__ == '__main__':
  s1 = '{}[]'
  s2 = '[]'
  s3 = '{}[]' 
  s4 = '[()]'
  s5 = '(())'
  s6 = '{[]}()'
  s7 = '{{{('
  s8 = '{[}'
  s9 = 'foo(bar);' 
  s10 = 'foo(bar[i);' 
  my_stack = Stack(s6)
  my_stack.checkBalance()
  
  





