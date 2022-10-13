d={'Name' : 'Pragati', 'Branch': 'ISE'}
# print(d)

#access
# print(d['Name'])

#traversing
# for i in d:
#     print(i,d[i])

#length- len(d)

#addition of elements 
d1={1:10,2:30,3:30}
# d1[4] = 40
# print(d1)

#update element in the dictionary
d1={1:10,2:30,3:30}
d1[2]=20
print(d1)

#old_dic.update(new_dic)
# d1.update(d)
# print(d1)

'''
Deletion
1. pop(key)
2. del statement
'''
#pop
# print(d1.pop(2))

#del
# del d1
# print(d1)

#items(),#keys(),#values()
print(d1.items())
print(d1.keys())
print(d1.values())