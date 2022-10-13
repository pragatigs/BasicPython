'''
1. built-in DS-list(mutable),tuples(immutable),sets(mutable),dictionaries(mutable,keys-immutable)
2. User defined DS
'''
#list
# l=[10,2.9,30,"hi",[1,2,3]]
# print(type(l))
# #length of the list
# print(len(l))
# #access
# print(l[0],l[4][1])
# #concatenation of 2 lists
# l1=[1,2,3]
# l2=[10,20,30]
# print(l1+l2)
# #repeatation 
# print(l1 *3)
#slicing
# l3=[1,2,3,4,5,6]
# #l3[start:stop:step]
# print(l3[3:6])
# print(l3[-1],l3[-2])
#reverse list using slicing
# print(l3[::-1])

# print(l3[2:])
# for i in l3:
#     print(i)
#find the index of an element in the list
# print(l3.index(4))
# #count the frequency
# print(l3.count(2))
# #list()
# strr="hello"
# l=list(strr)
# print(l)
# t=('a',1,2)
# l=list(t)
# print(l)
# s={1,2,1.1}
# print(st)
'''
insertion of element in a list
1. l.append(ele)-insert at the last
2. l.extend(ele)
3. l.insert(pos,ele)
'''
# #append
# l3.append(6)
# print(l3)

# #extend
# l3.extend([7,8])
# print(l3)

# #insert
# l3.insert(1,1.5)
# print(l3)
'''
Deletion
1. pop(index)
2. remove(ele)
3.clear()
4. del statement
'''
# #pop
# print(l3.pop(1))

# #remove
# l3.remove(3)
# print(l3)

#clear-empties the list
# l3=[1,2,3,4,5,6]
# l3.clear()
# print(l3)

# #del-deletes the complete list
# l3=[1,2,3,4,5,6]
# del l3
# print(l3) #error

#count
#reverse()
# l3=[1,2,3,4,5,6]
#print(l3[::-1])
# l3.reverse()
# print(l3)

#sort()
# l3=[2,44,1,6,10,0]
# l3.sort()
# print(l3)

# #sorted(ds)
# t=(2,44,3,68,0)
# ts=sorted(t)
# print(ts)

#sum(list)
l3=[1,2,3,4,5]
s=sum(l3)
print(s)

#min(list) and max(list)
print(min(l3),max(l3))
#in and not in