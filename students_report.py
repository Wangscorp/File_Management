import json
import csv
import os
from datetime import datetime

def task_7_json_and_csv_processing():
    """Task 7: Process JSON data and generate CSV report."""
    print("=" * 50)
    print("STUDENTS DATA PROCESSING - TASK 7")
    print("=" * 50)
    
    json_file = "students.json"
    csv_file = "report.csv"
    
    try:
        # Check if students.json exists
        if not os.path.exists(json_file):
            print(f"Error: File '{json_file}' not found.")
            print("Please ensure 'students.json' exists in the current directory.")
            return False
        
        # Read JSON file
        print(f"\nReading data from '{json_file}'...")
        with open(json_file, 'r') as file:
            students_data = json.load(file)
        
        # Validate JSON structure
        if not isinstance(students_data, list):
            print("Error: JSON file should contain a list of student objects.")
            return False
        
        # Process each student and calculate average
        processed_students = []
        
        for student in students_data:
            if "id" not in student or "name" not in student or "scores" not in student:
                print(f"Warning: Student record missing required fields: {student}")
                continue
            
            student_id = student["id"]
            name = student["name"]
            scores = student["scores"]
            
            # Calculate average score
            if len(scores) > 0:
                average = round(sum(scores) / len(scores), 2)
            else:
                average = 0
            
            processed_students.append({
                "id": student_id,
                "name": name,
                "average": average
            })
        
        # Sort by average in descending order
        processed_students.sort(key=lambda x: x["average"], reverse=True)
        
        # Write to CSV file
        print(f"Writing results to '{csv_file}'...")
        with open(csv_file, 'w', newline='') as csv_output:
            fieldnames = ["id", "name", "average"]
            writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write student data
            writer.writerows(processed_students)
        
        # Display results
        print(f"\nSuccessfully processed {len(processed_students)} students.")
        print(f"Results written to '{csv_file}':\n")
        print("ID\t| Name\t| Average")
        print("-" * 35)
        for student in processed_students:
            print(f"{student['id']}\t| {student['name']}\t| {student['average']}")
        
        return True
    
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{json_file}'")
        print(f"Details: {e}")
        return False
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = task_7_json_and_csv_processing()
    if success:
        print("\n" + "=" * 50)
        print("Task 7 completed successfully!")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("Task 7 encountered errors.")
        print("=" * 50)
