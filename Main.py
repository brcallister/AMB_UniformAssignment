# @author Brian Callister
# Written in 2023 for the AMB
# Largely assisted by ChatGPT

import os
from src.ReadInput import read_students_data, read_uniforms_data
from src.AssignUniforms import assign_uniforms

# Define input and output paths
INPUT_PATH = "input"
OUTPUT_PATH = "output"

# Define the file paths for the input Excel files
STUDENTS_FILE = os.path.join(INPUT_PATH, "Students.xlsx")
UNIFORMS_FILE = os.path.join(INPUT_PATH, "Uniforms.xlsx")

if __name__ == "__main__":
    # Read the students and uniforms data from Excel files
    students = read_students_data(STUDENTS_FILE)
    uniforms = read_uniforms_data(UNIFORMS_FILE)

    # Call the AssignUniforms file/function here
    assign_uniforms(students, uniforms, OUTPUT_PATH)
