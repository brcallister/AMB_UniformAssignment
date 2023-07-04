# @author Brian Callister
# Written in 2023 for the AMB
# Largely assisted by ChatGPT

import os
try:
    import pandas as pd
except ModuleNotFoundError:
    print("Dependency not found: Please run (double click) 'Setup.bat' before running program.")
    exit(1)

from src.Student import Student
from src.Uniform import Uniform

def standardize_gender_str(gender):
    if isinstance(gender, str):
        lowercaseInput = gender.lower()
        if lowercaseInput.startswith('m') or lowercaseInput == 'boy':
            return 'Male'
        elif lowercaseInput.startswith('f') or lowercaseInput == 'girl':
            return 'Female'
    return gender

def read_students_data(filename):
    if not os.path.isfile(filename):
        print(f"Error: Input file '{filename}' does not exist.")
        print("Please make sure the file exists and try again.")
        exit(1)
    try:
        df = pd.read_excel(filename)
    except Exception as e:
        print(f"Error: Failed to read input file '{filename}'.")
        print("Please make sure the file is in the correct format and try again.")
        print("Please refer to the README or Template file for formatting help.")
        print(f"Error details: {str(e)}")
        exit(2)
    students_data = df.to_dict(orient='records')
    students = []
    for student in students_data:
        name = student['Name']
        height = student['Height']
        weight = student['Weight']
        gender = standardize_gender_str(student['Gender'])
        jacket_preference = student['Jacket_Preference']
        try:
            jacket_preference = int(jacket_preference)
        except ValueError:
            jacket_preference = None
        pants_preference = student['Pants_Preference']
        try:
            pants_preference = int(pants_preference)
        except ValueError:
            pants_preference = None

        student_obj = Student(name, height, weight, gender, jacket_preference, pants_preference)
        students.append(student_obj)
    return students

def read_uniforms_data(filename):
    if not os.path.isfile(filename):
        print(f"Error: Input file '{filename}' does not exist.")
        print("Please make sure the file exists and try again.")
        exit(1)
    try:
        df = pd.read_excel(filename)
    except Exception as e:
        print(f"Error: Failed to read input file '{filename}'.")
        print("Please make sure the file is in the correct format and try again.")
        print("Please refer to the README or Template file for formatting help.")
        print(f"Error details: {str(e)}")
        exit(2)
    uniforms_data = df.to_dict(orient='records')
    uniforms = []
    for uniform in uniforms_data:
        number = uniform['Number']
        height = uniform['Height']
        weight = uniform['Weight']
        gender = standardize_gender_str(uniform['Gender'])
        is_broken = True if isinstance(uniform['Is_Broken'], str) else False
        uniform_obj = Uniform(number, height, weight, gender, is_broken)
        uniforms.append(uniform_obj)
    return uniforms