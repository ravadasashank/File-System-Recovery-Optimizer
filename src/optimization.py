from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def access_file(self, filename):
        if filename in self.cache:
            self.cache.move_to_end(filename)  # Mark as recently used
            print(f"File '{filename}' accessed from cache")
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)  # Remove least recently used item
            self.cache[filename] = "File Data"
            print(f"File '{filename}' loaded into cache")

# Example Usage
cache = LRUCache(3)
cache.access_file("file1.txt")
cache.access_file("file2.txt")
cache.access_file("file3.txt")
cache.access_file("file4.txt")  # This will remove the oldest file (file1.txt)
