from src.file_system import FileSystem, FreeSpaceManager, Directory
from src.optimization import LRUCache, visualize_disk_usage
from src.recovery import Journal, DiskCrashSimulator

def main():
    print("Welcome to the File System Recovery and Optimization Tool")

    # Initialize file system
    fs = FileSystem("virtual_fs")
    fsm = FreeSpaceManager(10)  # Assume 10 blocks for simplicity
    directory = Directory()
    
    # File operations
    print("\n--- File System Operations ---")
    fs.create_file("example.txt", "This is a sample file.")
    fs.list_files()
    fs.delete_file("example.txt")

    # Free space management
    print("\n--- Free Space Management ---")
    block = fsm.allocate_block()
    fsm.free_block(block)

    # Directory Management
    print("\n--- Directory Structure ---")
    directory.create_file("document.txt", 10)
    print(f"Files in directory: {list(directory.files.keys())}")

    # LRU Cache Optimization
    print("\n--- LRU Cache Optimization ---")
    cache = LRUCache(3)
    cache.access_file("file1.txt")
    cache.access_file("file2.txt")
    cache.access_file("file3.txt")
    cache.access_file("file4.txt")  # Evicts the least recently used file

    # Disk usage visualization
    print("\n--- Visualizing Disk Usage ---")
    visualize_disk_usage(30, 100)  # 30% used, 70% free

    # File System Recovery
    print("\n--- File System Recovery ---")
    journal = Journal()
    journal.log_operation("CREATE", "example.txt")
    print("Journal Logs:", journal.get_logs())

    # Disk Crash Simulation & Recovery
    print("\n--- Disk Crash Simulation & Recovery ---")
    simulator = DiskCrashSimulator()
    simulator.backup_files()
    crashed_files = simulator.simulate_crash()
    simulator.recover_files(crashed_files)

if __name__ == "__main__":
    main()
