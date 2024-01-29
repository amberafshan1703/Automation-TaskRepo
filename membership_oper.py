'''
Membership operator -
in - return true if a value is found in the sequence
not in - returns true if a value is not found in the sequence
'''

my_list = [1,2,3,4,5,6] # list is a collection of unordered orders

print(54 in my_list) # True or False
print(54 not in my_list)

'''
identity operators 
is Returns True if both variables are the same object
is not Returns True if both variables are not the same object 
'''

x = [1,3,5,6]
y = [1,3,5,6]


print(x is y)
print(id(x))
print(id(y))
print(x is not y)