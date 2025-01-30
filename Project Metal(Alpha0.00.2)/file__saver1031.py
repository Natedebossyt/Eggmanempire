import os
print("file location:")
my_dir = input()
print("file name:")
file_name = input()
fname = os.path.join(my_dir, file_name)
file = open(fname,'w')