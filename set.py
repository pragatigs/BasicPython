#does not store redundant values
#unique set (unordered)
s={5,7,8}
# print(s)
# l=[1,1,2,3,4,4]
# st=set(l) #eliminates duplicate elements

#traverse
s1={1,2,3,4,5}
# for i in s:
#     print(i," ",end=' ')

#cannot access using indexes
# print()
# print(len(s1))
#add a new element using add(ele)
# s1.add(6)
# print(s1)

#old_set.update(new_set)
# s1.update(s)
# print(s1)
'''
deletion
1. remove(ele)
2. pop()
3. discard(ele)
''' 
#remove(ele)
# s1.remove(2)
# print(s1)

#pop()
# print(s1.pop())

# print(id(s1))
#discard
# s1.discard(3)
# print(s1)

#union or |
# print(s1.union(s))
# print(s1|s)

#intersection or &
# print(s1 & s)
# print(s1.intersection(s))

#difference
print(s1.difference(s))
print(s1-s)