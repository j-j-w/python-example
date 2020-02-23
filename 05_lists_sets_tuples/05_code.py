# lists
l = ['Apple', 'Banana', 'Mango']

# Add en element to the end of the list
l.append('Pineapple')
print(l)

# Remove en element from the list by value
l.remove('Banana')
print(l)

l[0] = 'Orange'
print(l)


# Sets
s = {'Apple', 'Banana', 'Mango'}

# Add en element to the list 
s.add('Orange')
print(s)

tws_me = {'mifo2', 'xiaomi', 'airpods'}
tws_more = {'soundpeats', 'mifo5', 'mifo2'}

want_new_tws = tws_more.difference(tws_me)
print(want_new_tws)
# {'soundpeats', 'mifo5'}
# Showing to tws more not yet in the my tws sets


# Tuples
t = ('Apple', 'Banana', 'Mango')
# tuples is not allow modify elements

print(t)
