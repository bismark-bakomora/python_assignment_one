# list of dictionaries storing student names and their scores
students = [
    {"name": "Ama", "Maths": 78, "Science": 82, "English": 74},
    {"name": "Kojo", "Maths": 65, "Science": 59, "English": 72},
    {"name": "Esi", "Maths": 90, "Science": 88, "English": 85}
]

# calculate average for each student using a loop
for student in students:
    maths_score = student["Maths"]
    science_score = student["Science"]
    english_score = student["English"]

    # calculate average
    average_score = (maths_score + science_score + english_score) / 3

    # store the average back into the dictionary using update()
    student.update({"Average": average_score})

# print each student's results
for student in students:
    print(
        f"{student['name']} - Maths: {student['Maths']}, "
        f"Science: {student['Science']}, English: {student['English']} "
        f"=> Average: {student['Average']:.2f}"
    )


# determine the student with the highest avegrgae
highest_avg_student = students[0]
for student in students:
    if student["Average"] > highest_avg_student["Average"]:
        highest_avg_student = student


print("\nStudent with the Highest Average:")
print(f"{highest_avg_student['name']} => {highest_avg_student['Average']:.3f}")