
from data_structure import Generator
import time
import data_structure as d
import random

print('Exp 1 \n')
g1 = Generator()
s1 = [g1.gen_element() for _ in range(int(0.1e6))]
g2 = Generator()
s2 = [g2.gen_element() for _ in range(int(0.2e6))]
g3 = Generator()
s3 = [g3.gen_element() for _ in range(int(0.5e6))]
g4 = Generator()
s4 = [g4.gen_element() for _ in range(int(0.8e6))]
g5 = Generator()
s5 = [g5.gen_element() for _ in range(int(1e6))]

def test_treap(s,n):
    a = time.time()
    t = d.Treap()
    for ele in s:
        t = d.insert(t, ele[0], ele[1])
    b = time.time()
    print('Time for treap in sequence '+ str(n) + ' is ' + str(b - a))

def test_array(s,n):
    a = time.time()
    da = d.DynamicArray()
    for ele in s:
        da = d.insert_a(da, ele[0], ele[1])
    b = time.time()
    print('Time for dynamic array in sequence ' + str(n) + ' is ' + str(b - a))

print('1')
test_treap(s1,1)
test_array(s1,1)
print('2')
test_treap(s2,2)
test_array(s2,2)
print('3')
test_treap(s3,3)
test_array(s3,3)
print('4')
test_treap(s4,4)
test_array(s4,4)
print('5')
test_treap(s5,5)
test_array(s5,5)


print('Exp 2 \n')

def generate_sequence(p):
    lst = []
    g = Generator()
    for _ in range(int(1e6)):
        if random.random() <= p:
            delete = g.gen_deletion()
            lst.append(delete)
        else:
            ele = g.gen_insertion()
            lst.append(ele)
    return lst

s21 = generate_sequence(0.001)
s22 = generate_sequence(0.005)
s23 = generate_sequence(0.01)
s24 = generate_sequence(0.05)
s25 = generate_sequence(0.1)

def run_treap(s,n):
    a = time.time()
    t = d.Treap()
    for id,ele in s:
        if id == 1:
            t = d.insert(t, ele[0], ele[1])
        else:
            t = d.delete(t,ele)
    b = time.time()
    print('Time for treap in sequence '+ str(n) + ' is ' + str(b - a))

def run_array(s,n):
    a = time.time()
    da = d.DynamicArray()
    for id,ele in s:
        if id == 1:
            da = d.insert_a(da, ele[0], ele[1])
        else:
            da = d.delete_a(da,ele)
    b = time.time()
    print('Time for dynamic array in sequence ' + str(n) + ' is ' + str(b - a))

run_treap(s21,1)
run_array(s21,1)
run_treap(s22,2)
run_array(s22,2)
run_treap(s23,3)
run_array(s23,3)
run_treap(s24,4)
run_array(s24,4)
run_treap(s25,5)
run_array(s25,5)

print('Exp 3 \n')

def generate_sequence3(p):
    lst = []
    g = Generator()
    for _ in range(int(1e6)):
        if random.random() <= p:
            ele = g.gen_search()
            lst.append(ele)
        else:
            ele = g.gen_insertion()
            lst.append(ele)
    return lst

s31 = generate_sequence3(0.001)
s32 = generate_sequence3(0.005)
s33 = generate_sequence3(0.01)
s34 = generate_sequence3(0.05)
s35 = generate_sequence3(0.1)

def run_treap3(s,n):
    a = time.time()
    t = d.Treap()
    for id,ele in s:
        if id == 1:
            t = d.insert(t, ele[0], ele[1])
        else:
            d.search(t,ele)
    b = time.time()
    print('Time for treap in sequence '+ str(n) + ' is ' + str(b - a))

def run_array3(s,n):
    a = time.time()
    da = d.DynamicArray()
    for id,ele in s:
        if id == 1:
            da = d.insert_a(da, ele[0], ele[1])
        else:
            d.search_a(da,ele)
    b = time.time()
    print('Time for dynamic array in sequence ' + str(n) + ' is ' + str(b - a))

run_treap3(s31,1)
run_array3(s31,1)
run_treap3(s32,2)
run_array3(s32,2)
run_treap3(s33,3)
run_array3(s33,3)
run_treap3(s34,4)
run_array3(s34,4)
run_treap3(s35,5)
run_array3(s35,5)

print('Exp 4 \n')

def generate_sequence4(L):
    lst = []
    g = Generator()
    for _ in range(int(L)):
        numb = random.random()
        if numb <= 0.05:
            ele = g.gen_deletion()
            lst.append(ele)
        elif numb <= 0.1:
            ele = g.gen_search()
            lst.append(ele)
        else:
            ele = g.gen_insertion()
            lst.append(ele)
    return lst

s41 = generate_sequence4(0.1e6)
s42 = generate_sequence4(0.2e6)
s43 = generate_sequence4(0.5e6)
s44 = generate_sequence4(0.8e6)
s45 = generate_sequence4(1e6)

def run_treap4(s,n):
    a = time.time()
    t = d.Treap()
    for id,ele in s:
        if id == 1:
            t = d.insert(t, ele[0], ele[1])
        elif id == 2:
            t = d.delete(t,ele)
        else:
            d.search(t,ele)
    b = time.time()
    print('Time for treap in sequence '+ str(n) + ' is ' + str(b - a))

def run_array4(s,n):
    a = time.time()
    da = d.DynamicArray()
    for id,ele in s:
        if id == 1:
            da = d.insert_a(da, ele[0], ele[1])
        elif id == 2:
            da = d.delete_a(da,ele)
        else:
            d.search_a(da,ele)
    b = time.time()
    print('Time for dynamic array in sequence ' + str(n) + ' is ' + str(b - a))

run_treap4(s41,1)
run_array4(s41,1)
run_treap4(s42,2)
run_array4(s42,2)
run_treap4(s43,3)
run_array4(s43,3)
run_treap4(s44,4)
run_array4(s44,4)
run_treap4(s45,5)
run_array4(s45,5)

