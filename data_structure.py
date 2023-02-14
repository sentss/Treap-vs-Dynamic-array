import random

class Generator:
    def __init__(self):
        self.id = 1
        self.id_next = 2
        self.pairs = {}


    def gen_element(self):
        key = random.randint(0,1e7)
        id_to_return = self.id
        self.pairs[id_to_return] = key
        self.id = self.id_next
        self.id_next += 1
        return (id_to_return, key)

    def gen_insertion(self):
        id,key = self.gen_element()
        return (1,(id,key))

    def gen_deletion(self):
        id = random.randint(1, self.id_next-1)
        #if id not been deleted
        if id not in self.pairs.keys():
            key = random.randint(0, 1e7)
        #if deleted, generate new key randomly
        else:
            key = self.pairs[id]
            del self.pairs[id]
        return (2,key)

    def gen_search(self):
        key = random.randint(0, 1e7)
        return (3,key)

class Treap:
    def __init__(self, id = None, key = None, left = None,right = None):
        self.priority = random.randint(0, 1e7)
        self.id = id
        self.key = key
        self.left = left
        self.right = right


#left rotate for treap
def left_rotate(root):
    #new root
    R = root.right
    t = root.right.left
    R.left = root
    root.right = t
    return R

#right rotate for treap
def right_rotate(root):
    L = root.left
    t = root.left.right
    L.right = root
    root.left = t
    return L

#insert for treap
def insert(root,id,key):
    if root is None or root.id == None:
        return Treap(id,key)
    #key no bigger than current key
    if key <= root.key:
        root.left = insert(root.left,id,key)
        #first if left root priority is smaller than root priority, or if equal but left root id is smaller than root id, we break the tie
        if root.left and (root.left.priority < root.priority or (root.left.priority == root.priority and root.left.id < root.id)):
            root=right_rotate(root)
    else:
        root.right = insert(root.right,id, key)
        if root.right and root.right.priority < root.priority:
            root = left_rotate(root)
    return root

#delete for treap
def delete(root,key):
    if not root or root.id == None:
        return None
    if key < root.key:
        root.left=delete(root.left,key)
    elif key > root.key:
        root.right = delete(root.right,key)
    #key == root.key
    else:
        if root.left == None and root.right == None:
            root = None
        #if the root has left and right subtree
        elif root.left != None and root.right != None:
            if root.left.priority < root.right.priority:
                root=right_rotate(root)
                root.right=delete(root.right,key)
            else:
                root=left_rotate(root)
                root.left=delete(root.left,key)
        # if the root only has one subtree
        else:
            if root.left != None:
                root = root.left
            else:
                root = root.right
    return root

#search for tree
def search(root,key):
    if not root or root.id == None:
        return None
    if root.key == key:
        return (root.id,root.key)
    elif key < root.key:
        return search(root.left,key)
    else:
        return search(root.right,key)

# method for print the tree, not used in this project
def printTree(root, level=0):
    if root != None:
        root.left.printTree(level + 1)
        print(' ' * 4 * level + '-> ' + str((root.priority,root.key)))
        root.right.printTree(level + 1)




class DynamicArray:
    def __init__(self,n = 0,capacity = 1):
        self.n = n
        self.capacity = capacity
        self.lst = [None] * capacity

#insert for dynamic array
def insert_a(array,id,key):
    c = array.capacity
    n = array.n
    #capacity is not full
    if n < c:
        array.lst[n] = (id,key)
        array.n += 1
        return array
    #capacity is full
    else:
        new_array = DynamicArray(0,2*c)
        #copy elements of old array to this new array
        for i in range(n):
            ele = array.lst[i]
            new_array.lst[i] = ele
            new_array.n += 1
        #insert the new element
        new_array.lst[n] = (id,key)
        new_array.n += 1
        return new_array


#delete for dynamic array
def delete_a(array,key):
    n = array.n
    for i in range(n):
        #loop to find the delete key
        if array.lst[i] and array.lst[i][1] == key:
            temp1 = array.lst[n-1]
            array.lst[i] = temp1
            array.lst[n-1] = None
            array.n -= 1
            if array.n >= 0.25 * array.capacity:
                return array
            #array length is smaller than 1/4
            else:
                new_array = DynamicArray(0,0.5*array.capacity)
                for i in range(array.n):
                    ele = array.lst[i]
                    new_array.lst[i] = ele
                    new_array.n += 1
                return new_array
            #if find the delete key and length is not smaller than 1/4
    #not find the delete key, do nothing
    return array


#search for dynamic array
def search_a(array,s_key):
    for i in range(array.n):
        id,key = array.lst[i]
        if key == s_key:
            return (id,key)
    return None