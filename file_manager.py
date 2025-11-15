import os
import sys
import shutil
from datetime import datetime
import json

def log_activity(log_file_path, message):
    """Log an activity with timestamp to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    try:
        with open(log_file_path, 'a') as log:
            log.write(log_entry)
    except Exception as e:
        print(f"Error writing to log file: {e}")
        sys.exit(1)

def task_1_project_initialization():
    """Task 1: Check and create StudentFiles folder."""
    print("\n=== TASK 1: Project Initialization ===")
    try:
        folder_name = "StudentFiles"
        
        # Check if folder exists
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
        else:
            print(f"Folder '{folder_name}' already exists.")
        
        # Display absolute path
        absolute_path = os.path.abspath(folder_name)
        print(f"Absolute path: {absolute_path}")
        
        return absolute_path, folder_name
    
    except Exception as e:
        print(f"Error during folder creation: {e}")
        sys.exit(1)

def task_2_file_creation_and_writing(folder_name):
    """Task 2: Create file with student names and current date."""
    print("\n=== TASK 2: File Creation and Writing ===")
    try:
        # Generate filename with current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        file_name = f"records_{current_date}.txt"
        file_path = os.path.join(folder_name, file_name)
        
        # Prompt user for five student names
        print("Enter five student names (one per line):")
        student_names = []
        for i in range(5):
            name = input(f"Student {i+1}: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.")
                i -= 1
                continue
            student_names.append(name)
        
        # Write names to file
        with open(file_path, 'w') as file:
            for name in student_names:
                file.write(name + '\n')
        
        # Display success message with creation time
        creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nSuccess! File '{file_name}' created at {creation_time}")
        print(f"Location: {file_path}")
        
        return file_name, file_path
    
    except Exception as e:
        print(f"Error during file creation: {e}")
        sys.exit(1)

def task_3_reading_and_file_information(file_path):
    """Task 3: Read file contents and display file information."""
    print("\n=== TASK 3: Reading and File Information ===")
    try:
        # Read and display file contents
        print("File contents:")
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
        
        # Display file size
        file_size = os.path.getsize(file_path)
        print(f"File size: {file_size} bytes")
        
        # Display last modified date
        last_modified_timestamp = os.path.getmtime(file_path)
        last_modified_date = datetime.fromtimestamp(last_modified_timestamp)
        print(f"Last modified: {last_modified_date.strftime('%Y-%m-%d %H:%M:%S')}")
    
    except Exception as e:
        print(f"Error reading file information: {e}")
        sys.exit(1)

def task_4_backup_and_archiving(folder_name, file_name, file_path):
    """Task 4: Create backup and move to Archive folder."""
    print("\n=== TASK 4: Backup and Archiving ===")
    try:
        # Create backup copy
        backup_name = f"backup_{file_name}"
        backup_path = os.path.join(folder_name, backup_name)
        shutil.copy(file_path, backup_path)
        print(f"Backup created: {backup_name}")
        
        # Create Archive subfolder if it doesn't exist
        archive_folder = os.path.join(folder_name, "Archive")
        if not os.path.exists(archive_folder):
            os.makedirs(archive_folder)
            print(f"Archive folder created: {archive_folder}")
        else:
            print("Archive folder already exists.")
        
        # Move backup to Archive folder
        archive_backup_path = os.path.join(archive_folder, backup_name)
        shutil.move(backup_path, archive_backup_path)
        print(f"Backup moved to Archive folder: {backup_name}")
        
        # List all files in Archive
        archive_files = os.listdir(archive_folder)
        print(f"\nFiles in Archive folder:")
        for file in archive_files:
            print(f"  - {file}")
        
        return archive_folder
    
    except Exception as e:
        print(f"Error during backup and archiving: {e}")
        sys.exit(1)

def task_5_logging_system(folder_name, file_name):
    """Task 5: Create and manage activity log."""
    print("\n=== TASK 5: Logging System ===")
    try:
        log_file_path = os.path.join(folder_name, "activity_log.txt")
        log_message = f"{file_name} created and archived successfully."
        log_activity(log_file_path, log_message)
        print(f"Activity logged successfully.")
        print(f"Log file location: {log_file_path}")
    
    except Exception as e:
        print(f"Error in logging system: {e}")
        # Log the error if possible
        try:
            log_activity(os.path.join(folder_name, "activity_log.txt"), f"ERROR: {e}")
        except:
            pass
        sys.exit(1)

def task_6_advanced_file_operations(folder_name):
    """Task 6: Advanced file operations including file deletion."""
    print("\n=== TASK 6: Advanced File Operations ===")
    
    log_file_path = os.path.join(folder_name, "activity_log.txt")
    
    try:
        # Ask user if they want to delete a file
        delete_choice = input("Would you like to delete a file from StudentFiles? (Yes/No): ").strip()
        
        if delete_choice.lower() == "yes":
            # Display available files
            print("\nAvailable files in StudentFiles:")
            files = os.listdir(folder_name)
            for i, file in enumerate(files, 1):
                file_path = os.path.join(folder_name, file)
                if os.path.isfile(file_path):
                    print(f"  {i}. {file}")
            
            # Ask for filename to delete
            file_to_delete = input("\nEnter the file name to delete: ").strip()
            file_delete_path = os.path.join(folder_name, file_to_delete)
            
            if os.path.exists(file_delete_path) and os.path.isfile(file_delete_path):
                os.remove(file_delete_path)
                print(f"File '{file_to_delete}' deleted successfully.")
                
                # Log the deletion
                log_activity(log_file_path, f"File '{file_to_delete}' deleted.")
            else:
                print(f"File '{file_to_delete}' not found.")
                log_activity(log_file_path, f"Attempted to delete non-existent file: '{file_to_delete}'")
        
        # Display all remaining files
        print("\nRemaining files in StudentFiles:")
        remaining_files = os.listdir(folder_name)
        if remaining_files:
            for file in remaining_files:
                print(f"  - {file}")
        else:
            print("  No files in StudentFiles folder.")
    
    except Exception as e:
        print(f"Error during file operations: {e}")
        log_activity(log_file_path, f"ERROR in advanced file operations: {e}")
        sys.exit(1)

def main():
    """Main program flow."""
    print("=" * 50)
    print("FILE MANAGEMENT AND DATA PROCESSING UTILITY")
    print("=" * 50)
    
    try:
        # Task 1: Initialize project
        absolute_path, folder_name = task_1_project_initialization()
        
        # Task 2: Create file with student names
        file_name, file_path = task_2_file_creation_and_writing(folder_name)
        
        # Task 3: Read file and display information
        task_3_reading_and_file_information(file_path)
        
        # Task 4: Backup and archive
        archive_folder = task_4_backup_and_archiving(folder_name, file_name, file_path)
        
        # Task 5: Logging system
        task_5_logging_system(folder_name, file_name)
        
        # Task 6: Advanced file operations
        task_6_advanced_file_operations(folder_name)
        
        print("\n" + "=" * 50)
        print("All tasks completed successfully!")
        print("=" * 50)
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
