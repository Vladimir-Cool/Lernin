

my_list = [1, 2, 3, 4]

# my_iterator = iter(my_list)
my_iterator = my_list.__iter__()

print(type(my_iterator))

print(my_iterator.__next__())    #
print(my_iterator.__next__())    #
print(my_iterator.__next__())    #
print(my_iterator.__next__())    #
print(my_iterator.__next__())    #



