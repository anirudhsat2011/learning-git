# Import necessary modules from FastAPI and Python standard library
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json  # To read/write JSON files
import os    # To check if a file exists

# Create a FastAPI app instance
app = FastAPI()

# Define the filename where student data will be saved
DATA_FILE = "students.json"

# Define the structure of a Student using Pydantic for validation
class Student(BaseModel):
    name: str     # Student's name
    age: int      # Student's age
    major: str    # Student's field of study

# Function to load students from the JSON file
def load_students():
    if os.path.exists(DATA_FILE):  # Check if the file exists
        with open(DATA_FILE, "r") as f:  # Open the file for reading
            return [Student(**s) for s in json.load(f)]  # Convert JSON data to list of Student objects
    return []  # Return empty list if file doesn't exist

# Function to save the current student list to the JSON file
def save_students():
    with open(DATA_FILE, "w") as f:  # Open the file for writing
        json.dump([s.dict() for s in students], f, indent=2)  # Convert Student objects to dicts and write to file

# Load student data from file at the start of the app
students = load_students()

# Home route to verify the API is running
@app.get("/")
def root():
    return {"Hello": "Student API"}  # Return a welcome message

# POST route to add a new student
@app.post("/students")
def create_student(student: Student):
    students.append(student)  # Add the new student to the list
    save_students()           # Save updated list to file
    return students           # Return the full list of students

# GET route to list all students with an optional limit
@app.get("/students/", response_model=list[Student])
def list_students(limit: int = 10):
    return students[0:limit]  # Return up to 'limit' number of students

# GET route to retrieve a specific student by index (ID)
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    if student_id < len(students):     # Check if the ID is valid
        return students[student_id]    # Return the student at that index
    else:
        raise HTTPException(status_code=404, detail="Student not found")  # Error if student doesn't exist
