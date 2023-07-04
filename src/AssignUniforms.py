# @author Brian Callister
# Written in 2023 for the AMB
# Largely assisted by ChatGPT

import os
try:
    import pandas as pd
except ModuleNotFoundError:
    print("Dependency not found: Please run (double click) 'Setup.bat' before running program.")
    exit(1)

def _make_assignments(students, uniforms):
    assigned_jackets = set()
    assigned_pants = set()

    # Filter out broken uniforms
    uniforms = [uniform for uniform in uniforms if not uniform.is_broken]

    # Assign students with uniform preferences first
    for student in students:
        if student.jacket_preference is not None:
            for uniform in uniforms:
                if uniform.number == student.jacket_preference and uniform.number not in assigned_jackets:
                    student.jacket_num = uniform.number
                    assigned_jackets.add(uniform.number)
                    break

        if student.pants_preference is not None:
            for uniform in uniforms:
                if uniform.number == student.pants_preference and uniform.number not in assigned_pants:
                    student.pants_num = uniform.number
                    assigned_pants.add(uniform.number)
                    break

    # Assign students without preferences or unable to get their preferred uniforms
    students_without_uniforms = [student for student in students if student.jacket_num is None or student.pants_num is None]
    students_without_uniforms.sort(key=lambda s: (s.height, s.weight))

    for student in students_without_uniforms:
        # Find the best fitting uniform
        best_jacket_fit = None
        best_pants_fit = None

        for uniform in uniforms:
            if uniform.number not in assigned_jackets and _will_uniform_fit(student, uniform):
                if best_jacket_fit is None:
                    best_jacket_fit = uniform
                else:
                    # Compare heights
                    if uniform.height < best_jacket_fit.height:
                        best_jacket_fit = uniform
                    elif uniform.height == best_jacket_fit.height:
                        # Compare gender
                        if best_jacket_fit.gender == student.gender and uniform.gender != student.gender:
                            continue
                        elif best_jacket_fit.gender != student.gender and uniform.gender == student.gender:
                            best_jacket_fit = uniform
                        else:
                            # Compare weight
                            if abs(student.weight - uniform.weight) < abs(student.weight - best_jacket_fit.weight):
                                best_jacket_fit = uniform

        # If the jacket has been assigned and matching pants are available, they are the best fit 
        if best_jacket_fit != None and best_jacket_fit.number not in assigned_pants:
            best_pants_fit = best_jacket_fit
        else:
            for uniform in uniforms:
                if uniform.number not in assigned_pants and _will_uniform_fit(student, uniform):
                    if best_pants_fit is None:
                        best_pants_fit = uniform
                    else:
                        # Compare heights
                        if uniform.height < best_pants_fit.height:
                            best_pants_fit = uniform
                        elif uniform.height == best_pants_fit.height:
                            # Compare gender
                            if best_pants_fit.gender == student.gender and uniform.gender != student.gender:
                                continue
                            elif best_pants_fit.gender != student.gender and uniform.gender == student.gender:
                                best_pants_fit = uniform
                            else:
                                # Compare weight
                                if abs(student.weight - uniform.weight) < abs(student.weight - best_pants_fit.weight):
                                    best_pants_fit = uniform

        # Assign the best fitting uniforms to the student
        if student.jacket_num is None and best_jacket_fit is not None:
            student.jacket_num = best_jacket_fit.number
            assigned_jackets.add(best_jacket_fit.number)

        if student.pants_num is None and best_pants_fit is not None:
            student.pants_num = best_pants_fit.number
            assigned_pants.add(best_pants_fit.number)
    
    return students


def _will_uniform_fit(student, uniform):
    # These values allow for fine tuning:
    min_uniform_height = student.height
    max_uniform_height = student.height + 3
    min_uniform_weight = student.weight - 10
    max_uniform_weight = student.weight + 15

    return (
        min_uniform_height <= uniform.height <= max_uniform_height
        and min_uniform_weight <= uniform.weight <= max_uniform_weight
    )

def assign_uniforms(students, uniforms, output_path):
    # Make the student uniform assignments
    students = _make_assignments(students, uniforms)

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Define the output file path
    output_file = os.path.join(output_path, "UNIFORM_ASSIGNMENTS.xlsx")

    # Generate the uniform assignments DataFrame
    data = []
    for student in students:
        # Append the student's uniform assignment information to the data list
        data.append([student.name, student.jacket_num, student.pants_num])

    # Create a DataFrame from the data list
    df = pd.DataFrame(data, columns=["Name", "Jacket Number", "Pants Number"])

    # Save the DataFrame to an Excel file
    try:
        df.to_excel(output_file, index=False)
    except PermissionError:
        print(f"Cannot write output file - Please close or delete: '{output_path}/UNIFORM_ASSIGNMENTS.xlsx' and rerun the program.")
        exit(1)

    print(f"Uniform assignments saved to {output_file}")
