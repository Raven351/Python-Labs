class Stack:
     def __init__(self):
         self.itemCount = 0
         print("Created stack")
    
     def addItem(self, item):
       if self.itemCount != 0:
        self.topItem = StackItem(item, self.topItem)
        self.itemCount += 1
       else:
        self.topItem = StackItem(item, False)
        self.itemCount += 1
       print("Added item into the stack")

     def getTop(self):
        return(self.topItem.item)

     def printTop(self):
        print(self.topItem.item)   

     def popTop(self):
        if self.itemCount !=0:
          var = self.topItem.item
          self.topItem = self.topItem.previousItem
          self.itemCount -=1
          print("Removed top item")
          return var
        else:
          print("Cannot pop item! Stack is empty!")
          
      
     def stackItemCount(self):
         return s.itemCount


class StackItem:
     def __init__(self, item, previousItem):
       self.item = item
       self.previousItem = previousItem

s = Stack()
s.addItem("Pierwszy")
s.addItem("Drugi")
s.addItem("Trzeci")
s.getTop()
s.printTop()    
print(s.popTop())
print(s.stackItemCount())
print(s.popTop())
print(s.stackItemCount())
print(s.popTop())
print(s.stackItemCount())
print(s.popTop())
print(s.stackItemCount())
print(s.popTop())
print(s.stackItemCount())
s.addItem(12345)
s.printTop() 
print(s.stackItemCount())

