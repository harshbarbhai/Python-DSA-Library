class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class SinglyCC:
    def __init__(self):
        self.first = None
        self.iCount = 0

#---------------------------------------------------------------------
#   Function name : InsertFirst
#   Description :   It is use to insert node at the beginning of the list
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertFirst(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn
            newn.next = self.first

        # It contains Atleast one node
        else:
            temp = self.first

            while(temp.next != self.first):
                temp = temp.next

            temp.next = newn
            newn.next = self.first
            self.first = newn

        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : InsertLast
#   Description :   It is use to insert node at the end of the list
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertLast(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn
            newn.next = self.first

        # It contains Atleast one node
        else:
            temp = self.first

            while(temp.next != self.first):
                temp = temp.next

            temp.next = newn
            newn.next = self.first

        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : InsertAtPos
#   Description :   It is use to insert node at a particular position
#                   in the circular singly linked list
#   Parameters :    no (value to be inserted)
#                   pos (position at which node is to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertAtPos(self,no,pos):

        # invalid position
        if(pos < 1 or pos > (self.iCount + 1)):
            print("Invalid position ")
            return

        if(pos == 1):
            self.InsertFirst(no)
            return

        elif(pos == self.iCount + 1):
            self.InsertLast(no)
            return

        else:
            newn = Node(no)
            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn

            self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : DeletFirst
#   Description :   It is use to delete the first node from the list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeletFirst(self):

        if(self.first == None):
            return

        temp = self.first
        self.first = self.first.next

        temp1 = self.first

        while(temp1.next != temp):
            temp1 = temp1.next

        temp1.next = self.first

        del temp

        self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : DeletLast
#   Description :   It is use to delete the last node from the list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeletLast(self):

        if(self.first == None):
            return

        if(self.first.next == self.first):
            del self.first
            self.first = None
            self.iCount = 0

        else:
            temp = self.first

            while(temp.next.next != self.first):
                temp = temp.next

            del temp.next
            temp.next = self.first

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : DeleteAtPos
#   Description :   It is use to delete a node from a particular
#                   position in the circular singly linked list
#   Parameters :    pos (position of node to be deleted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeleteAtPos(self,pos):

        if(pos < 1 or pos > self.iCount):
            print("Invalid position ")
            return

        if(pos == 1):
            self.DeletFirst()
            return

        elif(pos == self.iCount):
            self.DeletLast()
            return

        else:
            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next

            temp.next = temp.next.next

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the circular
#                   singly linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        if self.first == None:
            print("linkList is Empty")
            return

        temp = self.first

        print("| ",temp.data," |->",end=" ")
        temp = temp.next

        while(temp != self.first):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next

        print("")


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of nodes present
#                   in the circular singly linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class SinglyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0

#---------------------------------------------------------------------
#   Function name : InsertFirst
#   Description :   It is use to insert node at the beginning of the list
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertFirst(self,no):
        newn = Node(no)

        if self.first == None:
            self.first = newn

        else:
            newn.next = self.first
            self.first = newn

        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : InsertLast
#   Description :   It is use to insert node at the end of the list
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertLast(self,no):
        newn = Node(no)

        if self.first == None:
            self.first = newn

        else:
            temp = self.first

            while(temp.next != None):
                temp = temp.next

            temp.next = newn

        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : InsertAtPos
#   Description :   It is use to insert node at a particular position
#                   in the singly linked list
#   Parameters :    no (value to be inserted)
#                   pos (position at which node is to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertAtPos(self,no,pos):

        if(pos < 1 or pos > (self.iCount + 1)):
            print("Invalid position ")
            return

        if(pos == 1):
            self.InsertFirst(no)
            return

        elif(pos == self.iCount+1):
            self.InsertLast(no)
            return

        else:
            newn = Node(no)
            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn

            self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : DeletFirst
#   Description :   It is use to delete the first node from the list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeletFirst(self):

        if(self.first == None):
            return

        # If only one node
        if(self.first.next == None):
            del self.first
            self.first = None
            self.iCount = 0

        # If more than one node
        else:
            temp = self.first
            self.first = self.first.next

            del temp

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : DeletLast
#   Description :   It is use to delete the last node from the list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeletLast(self):

        if(self.first == None):
            return

        if(self.first.next == None):
            del self.first
            self.first = None
            self.iCount = 0

        else:
            temp = self.first

            while(temp.next.next != None):
                temp = temp.next

            del temp.next
            temp.next = None

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : DeleteAtPos
#   Description :   It is use to delete a node from a particular
#                   position in the singly linked list
#   Parameters :    pos (position of node to be deleted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeleteAtPos(self,pos):

        if(pos < 1 or pos > self.iCount):
            print("Invalid position ")
            return

        if(pos == 1):
            self.DeletFirst()
            return

        elif(pos == self.iCount):
            self.DeletLast()
            return

        else:
            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next

            temp.next = temp.next.next

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the singly
#                   linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        temp = self.first

        while(temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next

        print("None")


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of nodes present
#                   in the singly linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class Node:
    def __init__(self,no):
        self.data = no
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0

#---------------------------------------------------------------------
#   Function name : InsertFirst
#   Description :   It is use to insert node at the beginning of the
#                   doubly linked list
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertFirst(self,no):
        newn = Node(no)

        if self.first == None:
            self.first = newn

        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn

        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : InsertLast
#   Description :   It is use to insert node at the end of the doubly
#                   linked list
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertLast(self,no):
        newn = Node(no)

        if self.first == None:
            self.first = newn

        else:
            temp = self.first

            while(temp.next != None):
                temp = temp.next

            temp.next = newn
            newn.prev = temp

        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : InsertAtPos
#   Description :   It is use to insert node at a particular position
#                   in the doubly linked list
#   Parameters :    no (value to be inserted)
#                   pos (position at which node is to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertAtPos(self,no,pos):

        if(pos < 1 or pos > (self.iCount + 1)):
            print("Invalid position")
            return

        if(pos == 1):
            self.InsertFirst(no)
            return

        elif(pos == self.iCount + 1):
            self.InsertLast(no)
            return

        else:
            newn = Node(no)
            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next

            newn.next = temp.next
            newn.prev = temp

            temp.next.prev = newn
            temp.next = newn

            self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : DeletFirst
#   Description :   It is use to delete the first node from the doubly
#                   linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeletFirst(self):

        if(self.first == None):
            return

        if(self.first.next == None):
            self.first = None

        else:
            self.first = self.first.next
            self.first.prev = None

        self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : DeletLast
#   Description :   It is use to delete the last node from the doubly
#                   linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeletLast(self):

        if(self.first == None):
            return

        if(self.first.next == None):
            self.first = None
            self.iCount = 0

        else:
            temp = self.first

            while(temp.next != None):
                temp = temp.next

            temp.prev.next = None

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : DeleteAtPos
#   Description :   It is use to delete a node from a particular
#                   position in the doubly linked list
#   Parameters :    pos (position of node to be deleted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeleteAtPos(self,pos):

        if(pos < 1 or pos > self.iCount):
            print("Invalid position")
            return

        if(pos == 1):
            self.DeletFirst()
            return

        elif(pos == self.iCount):
            self.DeletLast()
            return

        else:
            temp = self.first

            for i in range(1,pos):
                temp = temp.next

            temp.prev.next = temp.next
            temp.next.prev = temp.prev

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the doubly
#                   linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        temp = self.first

        while(temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next

        print("None")


#---------------------------------------------------------------------
#   Function name : DisplayReverse
#   Description :   It is use to display all elements of the doubly
#                   linked list in reverse order
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DisplayReverse(self):

        if(self.first == None):
            print("None")
            return

        temp = self.first

        while(temp.next != None):
            temp = temp.next

        while(temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.prev

        print("None")


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of nodes present
#                   in the doubly linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None


class DoublyCC:
    def __init__(self):
        self.first = None
        self.iCount = 0


#---------------------------------------------------------------------
#   Function name : InsertFirst
#   Description :   It is use to insert node at the beginning of the
#                   circular doubly linked list
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertFirst(self,no):
        newn = Node(no)

        if self.first == None:
            self.first = newn

            newn.next = self.first
            newn.prev = self.first

        else:
            last = self.first.prev

            newn.next = self.first
            newn.prev = last

            last.next = newn
            self.first.prev = newn

            self.first = newn

        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : InsertLast
#   Description :   It is use to insert node at the end of the circular
#                   doubly linked list
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertLast(self,no):
        newn = Node(no)

        if self.first == None:
            self.first = newn

            newn.next = self.first
            newn.prev = self.first

        else:
            last = self.first.prev

            newn.next = self.first
            newn.prev = last

            last.next = newn
            self.first.prev = newn

        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : InsertAtPos
#   Description :   It is use to insert node at a particular position
#                   in the circular doubly linked list
#   Parameters :    no (value to be inserted)
#                   pos (position at which node is to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertAtPos(self,no,pos):

        if(pos < 1 or pos > (self.iCount + 1)):
            print("Invalid position")
            return

        if(pos == 1):
            self.InsertFirst(no)
            return

        elif(pos == self.iCount + 1):
            self.InsertLast(no)
            return

        else:
            newn = Node(no)

            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next

            newn.next = temp.next
            newn.prev = temp

            temp.next.prev = newn
            temp.next = newn

            self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : DeletFirst
#   Description :   It is use to delete the first node from the
#                   circular doubly linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeletFirst(self):

        if(self.first == None):
            return

        if(self.first.next == self.first):

            del self.first
            self.first = None
            self.iCount = 0

        else:
            temp = self.first
            last = self.first.prev

            self.first = self.first.next

            self.first.prev = last
            last.next = self.first

            del temp

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : DeletLast
#   Description :   It is use to delete the last node from the
#                   circular doubly linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeletLast(self):

        if(self.first == None):
            return

        if(self.first.next == self.first):

            del self.first
            self.first = None
            self.iCount = 0

        else:
            temp = self.first.prev

            temp.prev.next = self.first
            self.first.prev = temp.prev

            del temp

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : DeleteAtPos
#   Description :   It is use to delete a node from a particular
#                   position in the circular doubly linked list
#   Parameters :    pos (position of node to be deleted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DeleteAtPos(self,pos):

        if(pos < 1 or pos > self.iCount):
            print("Invalid position")
            return

        if(pos == 1):
            self.DeletFirst()
            return

        elif(pos == self.iCount):
            self.DeletLast()
            return

        else:
            temp = self.first

            for i in range(1,pos):
                temp = temp.next

            temp.prev.next = temp.next
            temp.next.prev = temp.prev

            del temp

            self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the circular
#                   doubly linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        if self.first == None:
            print("linkList is Empty")
            return

        temp = self.first

        print("| ",temp.data," |->",end=" ")

        temp = temp.next

        while(temp != self.first):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next

        print("Back to First")


#---------------------------------------------------------------------
#   Function name : DisplayReverse
#   Description :   It is use to display all elements of the circular
#                   doubly linked list in reverse order
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def DisplayReverse(self):

        if self.first == None:
            print("linkList is Empty")
            return

        temp = self.first.prev

        print("| ",temp.data," |->",end=" ")

        temp = temp.prev

        while(temp != self.first.prev):

            print("| ",temp.data," |->",end=" ")

            temp = temp.prev

            if(temp == self.first):
                break

        print("Back to Last")


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of nodes present
#                   in the circular doubly linked list
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount

class Stack:
    def __init__(self):
        self.Arr = [0] * 100
        self.iCount = 0

#---------------------------------------------------------------------
#   Function name : Push
#   Description :   It is use to insert an element at the top of stack
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Push(self,no):
        self.Arr[self.iCount] = no
        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : Pop
#   Description :   It is use to remove the top element from the stack
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Pop(self):

        if(self.iCount == 0):
            print("Stack is Empty")
            return

        self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : Peek
#   Description :   It is use to return the top element of the stack
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Peek(self):

        if(self.iCount == 0):
            print("Stack is Empty")
            return

        return self.Arr[self.iCount - 1]


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the stack
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        if(self.iCount == 0):
            print("Stack is Empty")
            return

        for i in range(self.iCount - 1,-1,-1):
            print("| ",self.Arr[i]," |")


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of elements present
#                   in the stack
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class Queue:
    def __init__(self):
        self.Arr = [0] * 100
        self.iCount = 0

#---------------------------------------------------------------------
#   Function name : Enqueue
#   Description :   It is use to insert an element at the rear of queue
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Enqueue(self,no):
        self.Arr[self.iCount] = no
        self.iCount = self.iCount + 1


#---------------------------------------------------------------------
#   Function name : Dequeue
#   Description :   It is use to remove the front element from the queue
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Dequeue(self):

        if(self.iCount == 0):
            print("Queue is Empty")
            return

        for i in range(0,self.iCount-1):
            self.Arr[i] = self.Arr[i+1]

        self.iCount = self.iCount - 1


#---------------------------------------------------------------------
#   Function name : Peek
#   Description :   It is use to return the front element of the queue
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Peek(self):

        if(self.iCount == 0):
            print("Queue is Empty")
            return

        return self.Arr[0]


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the queue
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        if(self.iCount == 0):
            print("Queue is Empty")
            return

        for i in range(0,self.iCount):
            print("| ",self.Arr[i]," |->",end=" ")

        print("None")


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of elements present
#                   in the queue
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class BSTNode:
    def __init__(self,no):
        self.data = no
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self):
        self.root = None
        self.iCount = 0

#---------------------------------------------------------------------
#   Function name : Insert
#   Description :   It is use to insert a node into the binary search tree
#   Parameters :    no (value to be inserted)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Insert(self,no):
        newn = BSTNode(no)

        if(self.root == None):
            self.root = newn
            self.iCount = self.iCount + 1
            return

        temp = self.root

        while(True):

            if(no < temp.data):

                if(temp.lchild == None):
                    temp.lchild = newn
                    self.iCount = self.iCount + 1
                    break

                else:
                    temp = temp.lchild

            elif(no > temp.data):

                if(temp.rchild == None):
                    temp.rchild = newn
                    self.iCount = self.iCount + 1
                    break

                else:
                    temp = temp.rchild

            else:
                print("Duplicate element")
                break


#---------------------------------------------------------------------
#   Function name : Search
#   Description :   It is use to search an element in the binary
#                   search tree
#   Parameters :    no (value to be searched)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Search(self,no):
        temp = self.root

        while(temp != None):

            if(no == temp.data):
                return True

            elif(no < temp.data):
                temp = temp.lchild

            else:
                temp = temp.rchild

        return False


#---------------------------------------------------------------------
#   Function name : Inorder
#   Description :   It is use to display the nodes of the binary search
#                   tree using inorder traversal
#   Parameters :    temp (current node of the tree)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Inorder(self,temp):

        if(temp != None):
            self.Inorder(temp.lchild)
            print(temp.data,end=" ")
            self.Inorder(temp.rchild)


#---------------------------------------------------------------------
#   Function name : Preorder
#   Description :   It is use to display the nodes of the binary search
#                   tree using preorder traversal
#   Parameters :    temp (current node of the tree)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Preorder(self,temp):

        if(temp != None):
            print(temp.data,end=" ")
            self.Preorder(temp.lchild)
            self.Preorder(temp.rchild)


#---------------------------------------------------------------------
#   Function name : Postorder
#   Description :   It is use to display the nodes of the binary search
#                   tree using postorder traversal
#   Parameters :    temp (current node of the tree)
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Postorder(self,temp):

        if(temp != None):
            self.Postorder(temp.lchild)
            self.Postorder(temp.rchild)
            print(temp.data,end=" ")


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of nodes present
#                   in the binary search tree
#   Parameters :    None
#   Date :          12/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class Searching:
    def __init__(self):
        self.Arr = [10,20,30,40,50]
        self.iCount = 5

#---------------------------------------------------------------------
#   Function name : LinearSearch
#   Description :   It is use to search an element in the array using
#                   linear search technique
#   Parameters :    no (value to be searched)
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def LinearSearch(self,no):

        for i in range(self.iCount):

            if(self.Arr[i] == no):
                return i

        return -1


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of elements present
#                   in the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class BinarySearching:
    def __init__(self):
        self.Arr = [10,20,30,40,50]
        self.iCount = 5

#---------------------------------------------------------------------
#   Function name : BinarySearch
#   Description :   It is use to search an element in a sorted array
#                   using binary search technique
#   Parameters :    no (value to be searched)
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def BinarySearch(self,no):

        iStart = 0
        iEnd = self.iCount - 1

        while(iStart <= iEnd):

            iMid = (iStart + iEnd) // 2

            if(self.Arr[iMid] == no):
                return iMid

            elif(no < self.Arr[iMid]):
                iEnd = iMid - 1

            else:
                iStart = iMid + 1

        return -1


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of elements present
#                   in the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class BubbleSorting:
    def __init__(self):
        self.Arr = [50,20,40,10,30]
        self.iCount = 5

#---------------------------------------------------------------------
#   Function name : BubbleSort
#   Description :   It is use to sort the elements of the array using
#                   bubble sort technique
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def BubbleSort(self):

        for i in range(self.iCount - 1):

            for j in range(self.iCount - i - 1):

                if(self.Arr[j] > self.Arr[j + 1]):

                    temp = self.Arr[j]
                    self.Arr[j] = self.Arr[j + 1]
                    self.Arr[j + 1] = temp


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of elements present
#                   in the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class SelectionSorting:
    def __init__(self):
        self.Arr = [50,20,40,10,30]
        self.iCount = 5

#---------------------------------------------------------------------
#   Function name : SelectionSort
#   Description :   It is use to sort the elements of the array using
#                   selection sort technique
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def SelectionSort(self):

        for i in range(self.iCount - 1):

            iMin = i

            for j in range(i + 1,self.iCount):

                if(self.Arr[j] < self.Arr[iMin]):
                    iMin = j

            temp = self.Arr[i]
            self.Arr[i] = self.Arr[iMin]
            self.Arr[iMin] = temp


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of elements present
#                   in the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount



class InsertionSorting:
    def __init__(self):
        self.Arr = [50,20,40,10,30]
        self.iCount = 5

#---------------------------------------------------------------------
#   Function name : InsertionSort
#   Description :   It is use to sort the elements of the array using
#                   insertion sort technique
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def InsertionSort(self):

        for i in range(1,self.iCount):

            temp = self.Arr[i]
            j = i - 1

            while(j >= 0 and self.Arr[j] > temp):

                self.Arr[j + 1] = self.Arr[j]
                j = j - 1

            self.Arr[j + 1] = temp


#---------------------------------------------------------------------
#   Function name : Display
#   Description :   It is use to display all elements of the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Display(self):

        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()


#---------------------------------------------------------------------
#   Function name : Count
#   Description :   It is use to return the number of elements present
#                   in the array
#   Parameters :    None
#   Date :          13/09/2026
#   Author :        Harsh Niesh Barbhai
#---------------------------------------------------------------------
    def Count(self):
        return self.iCount