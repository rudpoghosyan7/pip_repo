import os

# Show current directory
print("Current dir:", os.getcwd())

# List files
print("Files here:", os.listdir("."))

# Make a new folder
os.mkdir("test_folder")
print("Created folder test_folder")

# Change directory
os.chdir("test_folder")
print("Now inside:", os.getcwd())

# Go back
os.chdir("..")
print("Back to:", os.getcwd())

# Remove folder
os.rmdir("test_folder")
print("Removed folder test_folder")
