import os
old_name=input("Enter the name of the old file: ")
old_path=fr"D:\\{old_name}"
new_name=input("Enter New file name: ")
new_path=fr"D:\\{new_name}"
if os.path.exists(old_path):
    os.rename(old_path,new_path)
    print(f"File named {old_name} is renamed as {new_name}")
else:
    print(f"File named {old_name} doesn't found" )
    