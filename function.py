import shutil
import os



def create_zip(file_path, new_folder):
    """Create a zip file. Select the path to the folder you want to zip and then select new path for the zipped folder."""
    shutil.make_archive(new_folder, 'zip', file_path )    
    if os.path.exists(new_folder + ".zip"):
        print("Folder Successfully Zipped")
    else:
        print("An error occurred during the operation")
    

if __name__ == "__main__":
    print('This is the function.py file')
    