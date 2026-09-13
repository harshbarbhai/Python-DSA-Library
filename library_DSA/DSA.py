class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class SinglyCC:
    def __init__(self):
        self.first = None
        self.iCount = 0

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

    def InsertAtPos(self,no,pos):
        # invalid position
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

    def DeletFirst(self):
        if(self.first == None):
            return
        temp = self.first   #optional
        self.first = self.first.next

        temp1 = self.first
        while(temp1.next != temp):
            temp1 = temp1.next

        temp1.next = self.first 

        del temp

        self.iCount = self.iCount-1

    def DeletLast(self):
        if(self.first == None):  # LL is empty
            return
        
        if(self.first.next == self.first):  # if only one node in LL
            del self.first
            self.first = None
            self.iCount = 0
        else:                     # LL contatains more than one node
            temp = self.first   

            while(temp.next.next != self.first):
                temp = temp.next

            del temp.next
            temp.next = self.first

            self.iCount = self.iCount-1   

    def DeleteAtPos(self,pos):
        # invalid position
        if(pos < 1 or pos > (self.iCount)):
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

    def InsertFirst(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn
        # It contains Atleast one node
        else:
            newn.next = self.first
            self.first = newn

        self.iCount = self.iCount + 1
        

    def InsertLast(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn
        # It contains Atleast one node
        else:
            temp = self.first

            while(temp.next != None):
                temp = temp.next

            temp.next = newn
    
        self.iCount = self.iCount + 1

    def InsertAtPos(self,no,pos):
        # invalid position
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

    def DeletFirst(self):
        if(self.first == None):
            return

    # If only one node
        if(self.first.next == self.first):
            del self.first
            self.first = None
            self.iCount = 0

    # If more than one node
        else:
            temp = self.first   #optional
            self.first = self.first.next
            del temp  #optional

            self.iCount = self.iCount-1
    

    def DeletLast(self):
        if(self.first == None):  # LL is empty
            return
        
        if(self.first.next == None):  # if only one node in LL
            del self.first
            self.first = None
            self.iCount = 0
        else:                     # LL contatains more than one node
            temp = self.first   

            while(temp.next.next != None):
                temp = temp.next

            del temp.next
            temp.next = None

            self.iCount = self.iCount-1

    def DeleteAtPos(self,pos):
        # invalid position
        if(pos < 1 or pos > (self.iCount)):
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

    def Display(self):
        temp = self.first

        while(temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next

        print("None")

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

    def InsertFirst(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn

        # It contains Atleast one node
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn

        self.iCount = self.iCount + 1


    def InsertLast(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn

        # It contains Atleast one node
        else:
            temp = self.first

            while(temp.next != None):
                temp = temp.next

            temp.next = newn
            newn.prev = temp

        self.iCount = self.iCount + 1


    def InsertAtPos(self,no,pos):
        # invalid position
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


    def DeletFirst(self):
        if(self.first == None):
            return

        # If only one node
        if(self.first.next == None):
            self.first = None

        # If more than one node
        else:
            self.first = self.first.next
            self.first.prev = None

        self.iCount = self.iCount - 1


    def DeletLast(self):
        if(self.first == None):       # LL is empty
            return

        if(self.first.next == None):  # only one node
            self.first = None
            self.iCount = 0

        else:                         # more than one node
            temp = self.first

            while(temp.next != None):
                temp = temp.next

            temp.prev.next = None

            self.iCount = self.iCount - 1


    def DeleteAtPos(self,pos):
        # invalid position
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


    def Display(self):
        temp = self.first

        while(temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next

        print("None")


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


    def InsertFirst(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn

            newn.next = self.first
            newn.prev = self.first

        # It contains Atleast one node
        else:
            temp = self.first

            while(temp.next != self.first):
                temp = temp.next

            newn.next = self.first
            newn.prev = temp

            temp.next = newn
            self.first.prev = newn

            self.first = newn

        self.iCount = self.iCount + 1


    def InsertLast(self,no):
        newn = Node(no)

        # LL is empty
        if self.first == None:
            self.first = newn

            newn.next = self.first
            newn.prev = self.first

        # It contains Atleast one node
        else:
            temp = self.first

            while(temp.next != self.first):
                temp = temp.next

            newn.next = self.first
            newn.prev = temp

            temp.next = newn
            self.first.prev = newn

        self.iCount = self.iCount + 1


    def InsertAtPos(self,no,pos):
        # invalid position
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


    def DeletFirst(self):
        if(self.first == None):
            return

        # If only one node
        if(self.first.next == self.first):
            del self.first
            self.first = None
            self.iCount = 0

        # If more than one node
        else:
            temp = self.first

            while(temp.next != self.first):
                temp = temp.next

            self.first = self.first.next

            self.first.prev = temp
            temp.next = self.first

            del self.first.prev

            self.iCount = self.iCount - 1


    def DeletLast(self):
        if(self.first == None):       # LL is empty
            return

        # If only one node
        if(self.first.next == self.first):
            del self.first
            self.first = None
            self.iCount = 0

        # LL contains more than one node
        else:
            temp = self.first

            while(temp.next != self.first):
                temp = temp.next

            temp.prev.next = self.first
            self.first.prev = temp.prev

            del temp

            self.iCount = self.iCount - 1


    def DeleteAtPos(self,pos):
        # invalid position
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


    def DisplayReverse(self):
        if self.first == None:
            print("linkList is Empty")
            return

        temp = self.first

        while(temp.next != self.first):
            temp = temp.next

        print("| ",temp.data," |->",end=" ")
        temp = temp.prev

        while(temp != self.first.prev):
            print("| ",temp.data," |->",end=" ")
            temp = temp.prev

            if(temp == self.first):
                break

        print("Back to Last")


    def Count(self):
        return self.iCount

class Stack:
    def __init__(self):
        self.Arr = [0] * 100
        self.iCount = 0

    def Push(self,no):
        self.Arr[self.iCount] = no
        self.iCount = self.iCount + 1

    def Pop(self):
        if(self.iCount == 0):
            print("Stack is Empty")
            return

        self.iCount = self.iCount - 1

    def Peek(self):
        if(self.iCount == 0):
            print("Stack is Empty")
            return

        return self.Arr[self.iCount - 1]

    def Display(self):
        if(self.iCount == 0):
            print("Stack is Empty")
            return

        for i in range(self.iCount - 1,-1,-1):
            print("| ",self.Arr[i]," |")

    def Count(self):
        return self.iCount

class Queue:
    def __init__(self):
        self.Arr = [0] * 100
        self.iCount = 0

    def Enqueue(self,no):
        self.Arr[self.iCount] = no
        self.iCount = self.iCount + 1

    def Dequeue(self):
        if(self.iCount == 0):
            print("Queue is Empty")
            return

        for i in range(0,self.iCount-1):
            self.Arr[i] = self.Arr[i+1]

        self.iCount = self.iCount - 1

    def Peek(self):
        if(self.iCount == 0):
            print("Queue is Empty")
            return

        return self.Arr[0]

    def Display(self):
        if(self.iCount == 0):
            print("Queue is Empty")
            return

        for i in range(0,self.iCount):
            print("| ",self.Arr[i]," |->",end=" ")

        print("None")

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

    def Insert(self,no):
        newn = BSTNode(no)

        # BST is empty
        if(self.root == None):
            self.root = newn
            self.iCount = self.iCount + 1
            return

        temp = self.root

        while(True):

            # Data is smaller
            if(no < temp.data):

                if(temp.lchild == None):
                    temp.lchild = newn
                    self.iCount = self.iCount + 1
                    break

                else:
                    temp = temp.lchild

            # Data is greater
            elif(no > temp.data):

                if(temp.rchild == None):
                    temp.rchild = newn
                    self.iCount = self.iCount + 1
                    break

                else:
                    temp = temp.rchild

            # Duplicate
            else:
                print("Duplicate element")
                break


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


    def Inorder(self,temp):
        if(temp != None):
            self.Inorder(temp.lchild)
            print(temp.data,end=" ")
            self.Inorder(temp.rchild)


    def Preorder(self,temp):
        if(temp != None):
            print(temp.data,end=" ")
            self.Preorder(temp.lchild)
            self.Preorder(temp.rchild)


    def Postorder(self,temp):
        if(temp != None):
            self.Postorder(temp.lchild)
            self.Postorder(temp.rchild)
            print(temp.data,end=" ")


    def Count(self):
        return self.iCount

class Searching:
    def __init__(self):
        self.Arr = [10,20,30,40,50]
        self.iCount = 5

    def LinearSearch(self,no):
        for i in range(self.iCount):
            if(self.Arr[i] == no):
                return i

        return -1

    def Display(self):
        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()

    def Count(self):
        return self.iCount

class BinarySearching:
    def __init__(self):
        self.Arr = [10,20,30,40,50]
        self.iCount = 5

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

    def Display(self):
        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()

    def Count(self):
        return self.iCount

class BubbleSorting:
    def __init__(self):
        self.Arr = [50,20,40,10,30]
        self.iCount = 5

    def BubbleSort(self):
        for i in range(self.iCount - 1):
            for j in range(self.iCount - i - 1):

                if(self.Arr[j] > self.Arr[j + 1]):
                    temp = self.Arr[j]
                    self.Arr[j] = self.Arr[j + 1]
                    self.Arr[j + 1] = temp

    def Display(self):
        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()

    def Count(self):
        return self.iCount

class SelectcionSorting:
    def __init__(self):
        self.Arr = [50,20,40,10,30]
        self.iCount = 5

    def SelectionSort(self):
        for i in range(self.iCount - 1):

            iMin = i

            for j in range(i + 1,self.iCount):

                if(self.Arr[j] < self.Arr[iMin]):
                    iMin = j

            temp = self.Arr[i]
            self.Arr[i] = self.Arr[iMin]
            self.Arr[iMin] = temp

    def Display(self):
        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()

    def Count(self):
        return self.iCount

class InsertionSorting:
    def __init__(self):
        self.Arr = [50,20,40,10,30]
        self.iCount = 5

    def InsertionSort(self):
        for i in range(1,self.iCount):

            temp = self.Arr[i]
            j = i - 1

            while(j >= 0 and self.Arr[j] > temp):
                self.Arr[j + 1] = self.Arr[j]
                j = j - 1

            self.Arr[j + 1] = temp

    def Display(self):
        for i in range(self.iCount):
            print(self.Arr[i],end=" ")

        print()

    def Count(self):
        return self.iCount