print(5 == 5)
print(5 != 5)

print('----------')

# Compare by elements using "==" and "is"
# ex: one
lists_one = ['Jame', 'John']
lists_two = ['Jame', 'John']
print(lists_one == lists_two)
# True
print(lists_one is lists_two)
# False

print('----------')

# ex: two
lists_one = ['Jame', 'John']
lists_two = lists_one

print(lists_one == lists_two)
# True

print(lists_one is lists_two)
# True
