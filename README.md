# AMB Uniform Assignment

This program is designed to assign uniforms to students based on available uniform inventory. Using an Excel document of student information and an Excel document of available uniform information, it will generate an Excel file containing optimized uniform assignments.

## Setup

1. Ensure that Python is installed on your machine. You can download the latest version of Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. Run the `Setup.bat` batch script (by double clicking it) to install the required dependencies. This script will automatically install `pandas` and `openpyxl` packages if they are not already installed.

## Usage

1. Update the list of students and uniforms in the `input` folder. The students should be listed in the `Students.xlsx` file, and the uniforms in the `Uniforms.xlsx` file (See [Input File Format](#input-file-format)).

2. Run the `AssignUniforms.bat` batch script (by double clicking it) to assign uniforms to the students. This script will use the updated input files to generate the output file.

## Output

The program will generate an output file named `UNIFORM_ASSIGNMENTS.xlsx` in the `output` folder. This file will contain the assigned jacket and pants numbers for each student.  

Each time the program is run, `UNIFORM_ASSIGNMENTS.xlsx` will be overwritten - be sure you no longer need these assignments before re-running the program.

## Input File Format

- **Students.xlsx**: The Excel file must have the following columns:
  - Name: The name of the student.
  - Height: The height of the student (in inches).
  - Weight: The weight of the student (in lbs).
  - Gender: The gender of the student.
  - Jacket_Preference: The preferred jacket number for the student. If no preference, leave it blank.
  - Pants_Preference: The preferred pants number for the student. If no preference, leave it blank.

- **Uniforms.xlsx**: The Excel file must have the following columns:
  - Number: The number of the uniform.
  - Height: The recommended height for the uniform (in inches).
  - Weight: The recommended weight for the uniform (in lbs).
  - Gender: The gender fit of the uniform.
  - Is_Broken: Whether the uniform is broken. If the field has any value, it denotes an unusable uniform; otherwise, it is considered intact.

For the required format, you can refer to the provided template files located in the `input` folder: `TemplateStudents.xlsx` and `TemplateUniforms.xlsx`.
