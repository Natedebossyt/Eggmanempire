import sys

def get_object_memory_size(obj):
    """
    Get the memory size of an object in bytes.
    """
    return sys.getsizeof(obj)

# Example usage
my_list = ()
memory_size = get_object_memory_size(my_list)
print(f"Memory size of my_list: {memory_size} bytes")

import memorymanagement1