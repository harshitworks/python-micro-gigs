import os

def rename_files(folder_path):
    files = os.listdir(folder_path)
    count = 1

    for file in files:
        old_path = os.path.join(folder_path, file)

        # Skip folders, for specific files , that we does not want to rename
        if os.path.isdir(old_path):
            continue

        name, extension = os.path.splitext(file)
        new_name = f"file_{count}{extension}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        count += 1

    print("✅ Files renamed successfully!")


folder_path = input("Enter the folder path: ")
rename_files(folder_path)
