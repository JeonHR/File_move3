import os 
import shutil


current_directory = os.getcwd()

for i in range(1, 17):
    os.makedirs(os.path.join(current_directory,f"site{i}") ,exist_ok=True)
    
    file_path = os.path.join(current_directory, f"pathloss_r2_BAZB_site{i}.txt")

    folder_path = os.path.join(current_directory,f"site{i}", f"site{i}.txt")

    shutil.copy2(file_path, folder_path)
    print(f"Copied pathloss_r2_BAZB_site{i}.txt to site_{i} folder.")