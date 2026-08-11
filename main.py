from pathlib import Path

#Input directory (where the files will be coming from)
dir_path = Path(r"C:\Users\PCXPC\Documents\super secret hehehe\Proj\file-automation-project\Source")

#Output directory (where the unique folders will be created)
output_path = Path(r"C:\Users\PCXPC\Documents\super secret hehehe\Proj\file-automation-project\Output")

# Initial loop to check the unique file types and create the right folders accordingly
for file in dir_path.iterdir():

    entry = str(file) # Stringify the file name
    name, extension = entry.split(".") # split the file name by the "." and store in name and extension

    folder_name = "" # initialize empty dynamic folder_name placeholder
    
    if extension == "csv":
        folder_name = "csv" # if the extention name is csv, folder_name will be csv
    elif extension == "xlsx":
        folder_name = "excel" # if the extention name is xslx, folder name will be excel
    elif extension == "txt": 
        folder_name = "Text Files" # if the extention name is txt, folder name will be text files

    folder_path = output_path/folder_name # create the folder path pointing towards the output folder
    folder_path.mkdir(parents=True, exist_ok=True) # create the folder, bypass if already exists

# Globalize the list of files (avoid repeating internal directory loops)
