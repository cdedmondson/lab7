import csv

grades = []
grades_list = []
names = []
count = 0
c = 0


# This function prints the students name and total score
def getTotalScore(name, dictionary):
    if name not in dictionary:
        print("Error! name does not exist in dictionary.")
        return 0
    else:
        return print(name, "total score =", dictionary[name])


# Open planets csv file
with open('grades.csv', newline='') as file:
    reader = csv.reader(file)  # Read file into reader variable
    # Iterate through file row by row
    for row in reader:
        grades.append(row)  # Append row to grades list

file.close()  # Close file

# Create a name list
for i in grades:
    if count != 0:  # Ignore header
        names.append(' '.join(grades[count][0:2]))  # Grab the first and last name from the list
    count += 1

count = 0  # Reset count

# Create a grade list
for j in grades:
    if count != 0:  # Ignore header
        grades_list.append(list(grades[count][2:]))  # Grab scores
    count += 1

# Detect elements that are not digits and overwrite with 0.0
for i in range(len(grades_list)):
    for j in range(len(grades_list[i])):
        temp = str(grades_list[i][j])  # Store element as temporary string variable
        if not temp.isdigit():  # If temp string is not a digit replace with  0.0
            grades_list[i][j] = 0.0
            c += 1  # Count number of elements that are not digits
        grades_list[i][j] = float(grades_list[i][j])  # Convert to float and store in original position

for i in range(len(grades_list)):
    grades_list[i] = sum(grades_list[i])

dictionary = dict(zip(names, grades_list))  # Create dictionary key value pair

# Open new file myPlanets
with open('myGrades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dictionary.items())  # Write grades data to myGrades

file.close()  # Close file

# Tests
print("Test1")
getTotalScore('Edmondson Cameron', dictionary)
print("Test2")
getTotalScore('Daramola Oliver', dictionary)
print("Number of elements that are not digit:", c)
