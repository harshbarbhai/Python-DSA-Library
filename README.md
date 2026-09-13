# Python-DSA-Library
Python Data Structures &amp; Algorithms library implemented from scratch using OOP.
# Python DSA Library

A simple Python project containing Data Structures and Algorithms implemented from scratch using Python.

## Data Structures & Algorithms

* Singly Linked List
* Singly Circular Linked List
* Doubly Linked List
* Doubly Circular Linked List
* Stack
* Queue
* Binary Search Tree
* Linear Search
* Binary Search
* Bubble Sort
* Selection Sort
* Insertion Sort

## Requirements

* Python 3.x
* No external libraries required

## Project Structure

```text
DSA Python/
│
├── DSAMain.py
│
└── library_DSA/
    ├── __init__.py
    └── DSA.py
```

## How to Run

### 1. Open Command Prompt

Open CMD and go to your project folder:

```cmd
cd "C:\Users\hp\Desktop\DSA Python"
```

### 2. Run the Program

```cmd
python DSAMain.py
```

### 3. Check Python Version

```cmd
python --version
```

## How to Save

Save the main program as:

```text
DSAMain.py
```

Save the DSA library as:

```text
library_DSA/DSA.py
```
## Output 
*****************************************************************
********************SinglyLL*************************************
*****************************************************************
Elements of LinkList are :
|  11  |-> |  21  |-> |  51  |-> |  101  |->
Number of elements in linklist are :  4
Elements of LinkList are :
|  11  |-> |  21  |-> |  51  |-> |  101  |-> |  111  |-> |  121  |->
Number of elements in linklist are :  6
Elements of LinkList are :
|  11  |-> |  21  |-> |  51  |-> |  75  |-> |  101  |-> |  111  |-> |  121  |->
Number of elements in linklist are :  7
Elements of LinkList are :
|  51  |-> |  75  |-> |  101  |-> |  111  |-> |  121  |->
Number of elements in linklist are :  5
Elements of LinkList are :
|  51  |-> |  75  |-> |  101  |-> |  111  |->
Number of elements in linklist are :  4
Elements of LinkList are :
|  51  |-> |  101  |-> |  111  |->
Number of elements in linklist are :  3
*****************************************************************
********************SinglyLL*************************************
*****************************************************************
Elements of LinkList are :
|  11  |-> |  21  |-> |  51  |-> |  101  |-> None
Number of elements in linklist are :  4
Elements of LinkList are :
|  11  |-> |  21  |-> |  51  |-> |  101  |-> |  111  |-> |  121  |-> None
Number of elements in linklist are :  6
Elements of LinkList are :
|  11  |-> |  21  |-> |  51  |-> |  75  |-> |  101  |-> |  111  |-> |  121  |-> None
Number of elements in linklist are :  7
Elements of LinkList are :
|  51  |-> |  75  |-> |  101  |-> |  111  |-> |  121  |-> None
Number of elements in linklist are :  5
Elements of LinkList are :
|  51  |-> |  75  |-> |  101  |-> |  111  |-> None
Number of elements in linklist are :  4
Elements of LinkList are :
|  51  |-> |  101  |-> |  111  |-> None
Number of elements in linklist are :  3
*****************************************************************
********************Doubly LL************************************
*****************************************************************
Elements of LinkList are :
|  21  |-> |  51  |-> |  101  |-> |  151  |-> None
Number of elements in linklist are :  4
Elements of LinkList are :
|  21  |-> |  51  |-> |  75  |-> |  101  |-> |  151  |-> None
Number of elements in linklist are :  5
Elements of LinkList are :
|  21  |-> |  51  |-> |  101  |-> |  151  |-> None
Number of elements in linklist are :  4
Elements of LinkList are :
|  51  |-> |  101  |-> |  151  |-> None
Number of elements in linklist are :  3
Elements of LinkList are :
|  51  |-> |  101  |-> None
Number of elements in linklist are :  2
Reverse Display :
|  101  |-> |  51  |-> None
*****************************************************************
********************Doubly Circular LL****************************
*****************************************************************
Elements of LinkList are :
|  21  |-> |  51  |-> |  101  |-> |  151  |-> Back to First
Number of elements in linklist are :  4
Elements of LinkList are :
|  21  |-> |  51  |-> |  75  |-> |  101  |-> |  151  |-> Back to First
Number of elements in linklist are :  5
Elements of LinkList are :
|  21  |-> |  51  |-> |  101  |-> |  151  |-> Back to First
Number of elements in linklist are :  4
Elements of LinkList are :
|  51  |-> |  101  |-> |  151  |-> Back to First
Number of elements in linklist are :  3
Elements of LinkList are :
|  51  |-> |  101  |-> Back to First
Number of elements in linklist are :  2
Reverse Display :
|  101  |-> |  51  |-> Back to Last
*****************************************************************
***************************Stack**********************************
*****************************************************************
Elements of Stack are :
|  151  |
|  101  |
|  21  |
|  51  |
Number of elements in Stack are :  4
Top element of Stack is :  151
Elements of Stack after Pop are :
|  101  |
|  21  |
|  51  |
Number of elements in Stack are :  3
Top element of Stack is :  101
*****************************************************************
***************************Queue**********************************
*****************************************************************
Elements of Queue are :
|  51  |-> |  21  |-> |  101  |-> |  151  |-> None
Number of elements in Queue are :  4
Front element of Queue is :  51
Elements of Queue after Dequeue are :
|  21  |-> |  101  |-> |  151  |-> None
Number of elements in Queue are :  3
Front element of Queue is :  21
*****************************************************************
***********************Binary Search Tree*************************
*****************************************************************
Number of elements in BST are :  7
Inorder Traversal :
5 21 31 51 75 101 151
Preorder Traversal :
51 21 5 31 101 75 151
Postorder Traversal :
5 31 21 75 151 101 51
Search 75 :  True
Search 100 :  False
*****************************************************************
************************ Linear Search ***************************
*****************************************************************
Elements of Array are :
10 20 30 40 50
Number of elements in Array are :  5
Element is found at position :  3
*****************************************************************
************************ Binary Search **************************
*****************************************************************
Elements of Array are : 10 20 30 40 50
Number of elements in Array are :  5
Element is found at position :  4
*****************************************************************
*************************** Bubble Sort **************************
*****************************************************************
Elements before sorting are : 50 20 40 10 30
Number of elements are :  5
Elements after sorting are : 10 20 30 40 50
*****************************************************************
************************ Selection Sort **************************
*****************************************************************
Elements before sorting are : 50 20 40 10 30
Number of elements are :  5
Elements after sorting are : 10 20 30 40 50
*****************************************************************
*********************** Insertion Sort ***************************
*****************************************************************
Elements before sorting are : 50 20 40 10 30
Number of elements are :  5
Elements after sorting are : 10 20 30 40 50

## Author
**Harsh Niesh Barbhai**

