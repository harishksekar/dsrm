import os
import time

def stress_disk(directory, file_size_MB):
    os.makedirs(directory, exist_ok=True)
    total_bytes = file_size_MB * 1024 * 1024 
    created_files = []

    try:
        while True:
            filename = os.path.join(directory, f"stress_file_{time.time()}.txt")
            with open(filename, 'wb') as f:
                f.write(os.urandom(total_bytes))
            created_files.append(filename)

    except KeyboardInterrupt:
        for file in created_files:
            os.remove(file)
        print("Temporary files removed.")

if __name__ == "__main__":
    directory = "disk_stress_test"  
    file_size_MB = 1024

    try:
        stress_disk(directory, file_size_MB)
    except KeyboardInterrupt:
        pass
