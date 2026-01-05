import os 
""" a built-in library that lets your Python script interact with the underlying operating system
 (like Windows, macOS, or Linux) to perform tasks like managing files, directories, environment variables,
   and running system commands """

""" folders = input("Enter the list of folders with spaces: ").split() 
# takes input from the user with spaces and splits the string into list
#print(folders)

for folder in folders:
    
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("the folder name provided " + folder + " is incorrect, Please provide the correct folder names")
    except NameError:
        print("the folder name provided " + folder + " is incorrect, Please provide the correct folder names")
    
    for file in files:
        print(file) """

#creating the same program using functions

def list_files_in_folder(folder_path):
#function to gets the files or try and catch the error using exception handling
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "folder not found"
    except NameError:
        return None, "folder not found"
    except PermissionError:
        return None, "folder not found"

def main():
#main function to define the input and get outputs
    folder_paths = input("enter the folder paths with spaces: ").split()

    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"files in {folder_path} are")
            for file in files:
                print(file)
        else:
            print(f"error message: {error_message}")
    
if __name__ == "__main__":
    main()
