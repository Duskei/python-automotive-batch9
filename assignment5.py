#importing the os module
import os

#function to find the .txt file in a given directory/folder
def find_txt_files(start_directory):
    print(f"Searching for .txt files in: {start_directory}\n")  
    
    # os.walk gives: (current_folder, subfolders, files)
    #root -> The path to the current folder 
    #dirs -> A list of subfolders inside the current root
    #files -> A list of all files inside the current root
    for root, dirs, files in os.walk(start_directory):
        for filename in files:
            # checks if the file ends with .txt 
            if filename.endswith(".txt"):
                # Join the folder path and filename to get the full path
                full_path = os.path.join(root, filename)
                print(full_path)
            else:
                print("no file present")

# r -> tells Python to treat every character exactly as it is written.
search_path = r"C:\Users\srest\OneDrive\Desktop\new" 
find_txt_files(search_path)