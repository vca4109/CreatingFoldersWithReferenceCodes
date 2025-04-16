import os

# Define the base directory where the folders will be created
base_directory = r"C:\Users\ABC\Desktop\Python Program"  # Change to your desired location

# Base reference string and starting number
base_reference = "5567-ABC-XYZ-T-"
start_number = 2002
total_folders = 100  # Number of folders to create

# Create folders
for i in range(total_folders):
    # Construct the folder name
    folder_name = f"{base_reference}{start_number + i} - DTF-"
    # Define the full path
    folder_path = os.path.join(base_directory, folder_name)
    # Create the folder
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder_path}")

print("Folders created successfully!")
