#Find common elements in two lists.
l1=[1,2,3,4,5,9,8,7,6,3]
l2=[1,4,8,11,23]
s=set(l1).intersection(set(l2))
print(list(s))