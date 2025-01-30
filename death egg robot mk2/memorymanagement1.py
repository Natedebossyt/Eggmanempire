
class MemoryBlock:
    def __init__(self, start_address, size):
        self.start_address = start_address
        self.size = size
        self.free = True

class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory_map = [MemoryBlock(0, total_memory)]

    def allocate_memory(self, size):
        for block in self.memory_map:
            if block.free and block.size >= size:
                block.free = False
                return block.start_address
        return None

    def deallocate_memory(self, address):
        for block in self.memory_map:
            if block.start_address == address:
                block.free = True
                return

    def display_memory_map(self):
        print("Memory Map:")
        for block in self.memory_map:
            print(f"Address: {block.start_address}, Size: {block.size}, Free: {block.free}")

# Example usage:
memory_manager = MemoryManager(1024)  # Total memory size is 1024 bytes
memory_manager.display_memory_map()

# Allocate memory
allocated_address = memory_manager.allocate_memory(128)
if allocated_address is not None:
    print(f"Allocated memory at address: {allocated_address}")
else:
    print("Failed to allocate memory")

# Display updated memory map
memory_manager.display_memory_map()

# Deallocate memory
memory_manager.deallocate_memory(allocated_address)
print("Memory deallocated")

# Display updated memory map
memory_manager.display_memory_map()

import cpumanagement1