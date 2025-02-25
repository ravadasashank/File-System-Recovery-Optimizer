import os
import shutil

class FileSystem:
    def __init__(self, root_directory):
        self.root = root_directory
        if not os.path.exists(self.root):
            os.makedirs(self.root)

    def create_file(self, filename, content=""):
        file_path = os.path.join(self.root, filename)
        with open(file_path, "w") as file:
            file.write(content)
        print(f"File '{filename}' created.")

    def delete_file(self, filename):
        file_path = os.path.join(self.root, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{filename}' deleted.")
        else:
            print(f"File '{filename}' not found.")

    def list_files(self):
        print("Files in system:", os.listdir(self.root))

# Example Usage
fs = FileSystem("virtual_fs")
fs.create_file("test.txt", "Hello World!")
fs.list_files()
fs.delete_file("test.txt")

class FreeSpaceManager:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.bitmap = [0] * total_blocks  # 0 = free, 1 = occupied

    def allocate_block(self):
        for i in range(self.total_blocks):
            if self.bitmap[i] == 0:
                self.bitmap[i] = 1
                print(f"Allocated block {i}")
                return i
        print("No free blocks available")
        return -1

    def free_block(self, block_number):
        if 0 <= block_number < self.total_blocks:
            self.bitmap[block_number] = 0
            print(f"Block {block_number} freed")

# Example Usage
fsm = FreeSpaceManager(10)
fsm.allocate_block()
fsm.free_block(0)
