import os
import time
import atexit

def stress_disk(directory, file_size_MB):
    os.makedirs(directory, exist_ok=True)
    total_bytes = file_size_MB * 1024 * 1024 
    created_files = []

    def cleanup():
        print("\nRemoving temporary files...")
        for file in created_files:
            try:
                os.remove(file)
            except Exception as e:
                print(f"Error removing file {file}: {e}")
        print("Temporary files removed.")

    atexit.register(cleanup)

    try:
        while True:
            filename = os.path.join(directory, f"stress_file_{time.time()}.txt")
            with open(filename, 'wb') as f:
                f.write(os.urandom(total_bytes))
            created_files.append(filename)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    directory = "disk_stress_test"  
    file_size_MB = 1024

    try:
        stress_disk(directory, file_size_MB)
    except KeyboardInterrupt:
        pass
