from library_DSA import DSA as np


def main():

    print("*****************************************************************")
    print("********************SinglyLL*************************************")
    print("*****************************************************************")

    sobj = np.SinglyCC()

    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    print("Elements of LinkList are : ")
    sobj.Display()
    print("Number of elements in linklist are : ",sobj.Count())

    sobj.InsertLast(111)
    sobj.InsertLast(121)
    print("Elements of LinkList are : ")
    sobj.Display()
    print("Number of elements in linklist are : ",sobj.Count())

    sobj.InsertAtPos(75,4)
    print("Elements of LinkList are : ")
    sobj.Display()
    print("Number of elements in linklist are : ",sobj.Count())

    sobj.DeletFirst()
    sobj.DeletFirst()
    print("Elements of LinkList are : ")
    sobj.Display()
    print("Number of elements in linklist are : ",sobj.Count())

    sobj.DeletLast()
    print("Elements of LinkList are : ")
    sobj.Display()
    print("Number of elements in linklist are : ",sobj.Count())

    sobj.DeleteAtPos(2)
    print("Elements of LinkList are : ")
    sobj.Display()
    print("Number of elements in linklist are : ",sobj.Count())

    print("*****************************************************************")
    print("********************SinglyLL*************************************")
    print("*****************************************************************")

    bobj=np.SinglyLL()

    bobj.InsertFirst(101)
    bobj.InsertFirst(51)
    bobj.InsertFirst(21)
    bobj.InsertFirst(11)

    print("Elements of LinkList are : ")
    bobj.Display()

    print("Number of elements in linklist are : ",bobj.Count())

    bobj.InsertLast(111)
    bobj.InsertLast(121)

    print("Elements of LinkList are : ")
    bobj.Display()

    print("Number of elements in linklist are : ",bobj.Count())

    bobj.InsertAtPos(75,4)

    print("Elements of LinkList are : ")
    bobj.Display()

    print("Number of elements in linklist are : ",bobj.Count())

    bobj.DeletFirst()
    bobj.DeletFirst()
    print("Elements of LinkList are : ")
    bobj.Display()

    print("Number of elements in linklist are : ",bobj.Count())

    bobj.DeletLast()
    print("Elements of LinkList are : ")
    bobj.Display()

    print("Number of elements in linklist are : ",bobj.Count())

    bobj.DeleteAtPos(2)
    print("Elements of LinkList are : ")
    bobj.Display()

    print("Number of elements in linklist are : ",bobj.Count())

    print("*****************************************************************")
    print("********************Doubly LL************************************")
    print("*****************************************************************")

    obj = np.DoublyLL()

    obj.InsertFirst(51)
    obj.InsertFirst(21)
    obj.InsertLast(101)
    obj.InsertLast(151)

    print("Elements of LinkList are : ")
    obj.Display()

    print("Number of elements in linklist are : ",obj.Count())

    obj.InsertAtPos(75,3)

    print("Elements of LinkList are : ")
    obj.Display()

    print("Number of elements in linklist are : ",obj.Count())

    obj.DeleteAtPos(3)

    print("Elements of LinkList are : ")
    obj.Display()

    print("Number of elements in linklist are : ",obj.Count())

    obj.DeletFirst()

    print("Elements of LinkList are : ")
    obj.Display()

    print("Number of elements in linklist are : ",obj.Count())

    obj.DeletLast()

    print("Elements of LinkList are : ")
    obj.Display()

    print("Number of elements in linklist are : ",obj.Count())

    print("Reverse Display :")
    obj.DisplayReverse()

    print("*****************************************************************")
    print("********************Doubly Circular LL****************************")
    print("*****************************************************************")

    dCobj = np.DoublyCC()

    dCobj.InsertFirst(51)
    dCobj.InsertFirst(21)
    dCobj.InsertLast(101)
    dCobj.InsertLast(151)

    print("Elements of LinkList are : ")
    dCobj.Display()

    print("Number of elements in linklist are : ",dCobj.Count())

    dCobj.InsertAtPos(75,3)

    print("Elements of LinkList are : ")
    dCobj.Display()

    print("Number of elements in linklist are : ",dCobj.Count())

    dCobj.DeleteAtPos(3)

    print("Elements of LinkList are : ")
    dCobj.Display()

    print("Number of elements in linklist are : ",dCobj.Count())

    dCobj.DeletFirst()

    print("Elements of LinkList are : ")
    dCobj.Display()

    print("Number of elements in linklist are : ",dCobj.Count())

    dCobj.DeletLast()

    print("Elements of LinkList are : ")
    dCobj.Display()

    print("Number of elements in linklist are : ",dCobj.Count())

    print("Reverse Display :")
    dCobj.DisplayReverse()
    print("*****************************************************************")
    print("***************************Stack**********************************")
    print("*****************************************************************")

    stobj = np.Stack()

    stobj.Push(51)
    stobj.Push(21)
    stobj.Push(101)
    stobj.Push(151)

    print("Elements of Stack are : ")
    stobj.Display()

    print("Number of elements in Stack are : ",stobj.Count())

    print("Top element of Stack is : ",stobj.Peek())

    stobj.Pop()

    print("Elements of Stack after Pop are : ")
    stobj.Display()

    print("Number of elements in Stack are : ",stobj.Count())

    print("Top element of Stack is : ",stobj.Peek())

    print("*****************************************************************")
    print("***************************Queue**********************************")
    print("*****************************************************************")

    qobj = np.Queue()

    qobj.Enqueue(51)
    qobj.Enqueue(21)
    qobj.Enqueue(101)
    qobj.Enqueue(151)

    print("Elements of Queue are : ")
    qobj.Display()

    print("Number of elements in Queue are : ",qobj.Count())

    print("Front element of Queue is : ",qobj.Peek())

    qobj.Dequeue()

    print("Elements of Queue after Dequeue are : ")
    qobj.Display()

    print("Number of elements in Queue are : ",qobj.Count())

    print("Front element of Queue is : ",qobj.Peek())

    print("*****************************************************************")
    print("***********************Binary Search Tree*************************")
    print("*****************************************************************")

    biobj = np.BST()

    biobj.Insert(51)
    biobj.Insert(21)
    biobj.Insert(101)
    biobj.Insert(5)
    biobj.Insert(31)
    biobj.Insert(75)
    biobj.Insert(151)

    print("Number of elements in BST are : ",biobj.Count())

    print("Inorder Traversal : ")
    biobj.Inorder(biobj.root)
    print()

    print("Preorder Traversal : ")
    biobj.Preorder(biobj.root)
    print()

    print("Postorder Traversal : ")
    biobj.Postorder(biobj.root)
    print()

    print("Search 75 : ",biobj.Search(75))

    print("Search 100 : ",biobj.Search(100))

    print("*****************************************************************")
    print("************************ Linear Search ***************************")
    print("*****************************************************************")

    lsobj = np.Searching()

    print("Elements of Array are : ")
    lsobj.Display()

    print("Number of elements in Array are : ",lsobj.Count())

    ret = lsobj.LinearSearch(30)

    if(ret == -1):
        print("Element is not found")
    else:
        print("Element is found at position : ",ret + 1)


    print("*****************************************************************")
    print("************************ Binary Search **************************")
    print("*****************************************************************")

    Bsobj = np.BinarySearching()

    print("Elements of Array are : ",end="")
    Bsobj.Display()

    print("Number of elements in Array are : ",Bsobj.Count())

    ret = Bsobj.BinarySearch(40)

    if(ret == -1):
        print("Element is not found")
    else:
        print("Element is found at position : ",ret + 1)

    print("*****************************************************************")
    print("*************************** Bubble Sort **************************")
    print("*****************************************************************")

    bssobj = np.BubbleSorting()

    print("Elements before sorting are : ",end="")
    bssobj.Display()

    print("Number of elements are : ",bssobj.Count())

    bssobj.BubbleSort()

    print("Elements after sorting are : ",end="")
    bssobj.Display()

    print("*****************************************************************")
    print("************************ Selection Sort **************************")
    print("*****************************************************************")

    ssobj = np.SelectionSorting()

    print("Elements before sorting are : ",end="")
    ssobj.Display()

    print("Number of elements are : ",ssobj.Count())

    ssobj.SelectionSort()

    print("Elements after sorting are : ",end="")
    ssobj.Display()

    print("*****************************************************************")
    print("*********************** Insertion Sort ***************************")
    print("*****************************************************************")

    Isobj = np.InsertionSorting()

    print("Elements before sorting are : ",end="")
    Isobj.Display()

    print("Number of elements are : ",Isobj.Count())

    Isobj.InsertionSort()

    print("Elements after sorting are : ",end="")
    Isobj.Display()

if __name__ == "__main__":
    main()