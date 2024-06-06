###########################################################################
# New Change:                                                             #
#  + Improve the appearance of the menu and student display.              #
#  + Modify the dataSearch function to handle larger databases            #
#  + Include a Data Information section displaying:                       #
#    - The number of students in each year                                #
#    - The total number of students                                       #
#    - The number of students with a GPA over 3                           #
#    - The number of students with a GPA under 3.                         #
#  + Fix multiple syntax error, logical error                             #                         
###########################################################################
#STUDENT DATA MANAGEMENT
#Try and Expect from W3schools
#isdigit() and isalpha() from W3schools
#open file from W3schools
import datetime
def datainfoGPA(database):
    o3 = 0
    u3 = 0
    for i in database:
        if i['GPA'] >= 3.0:
            o3 += 1
        else:
            u3 += 1
    return o3, u3

def studentEachYear(database):
    f = 0
    s = 0
    j = 0
    sn = 0
    for student in database:
        if student['grade'].lower() == 'freshman':
            f += 1
        elif student['grade'].lower() == 'sophomore':
            s += 1
        elif student['grade'].lower() == 'junior':
            j += 1
        elif student['grade'].lower() == 'senior':
            sn += 1
    return f, s, j, sn, f + s + j + sn

def FileConvert():
    # Try this command when this program says "File does not exist."
    # This command works on VSC terminal. Usually, other IDEs will work if you place both the file and this code in the same directory.
    # Command: cd diskThatContainTheFile:\FolderThatContainFile:\SubFolder or you can search how to use cd command on terminal. :D
    # This also works if you want to run the program using the terminal.
    try:
        with open('student.txt', 'r') as file:
            studentContent = file.readlines()
            student = []
            for line in studentContent:
                line = line.strip()
                if line:
                    value = line.split('|')
                    if len(value) == 5:
                        name, grade, dob, id, GPA = value
                        student.append({'name': name, 'id': id, 'grade': grade, 'dob': dob, 'GPA': float(GPA)})
                    else:
                        print("Invalid format in line: " + line + ". Skipping the line.")
            return student
    except FileNotFoundError:
        print("The file 'student.txt' does not exist. Make sure that your terminal is in folder that contains the database")
        exit()

def AddStudent(name, grade, dob, id, GPA):
    with open("student.txt", "a") as file:
        file.write(name.title() + "|" + grade + "|" + dob + "|" + id + "|" + str(GPA) + "\n")

def nukeFile(choice):
    if choice == True:
        open('student.txt', 'w').close()
        print("Your file has been nuked")
    else:
        print("Your file is not nuked")
def dataSearch(database, datain, searchValue):
    i = {}
    for student in database:
        value = student[datain].lower()
        if value not in i:
            i[value] = []
        i[value].append(student)
    searchValue=searchValue.lower()
    if searchValue in i:
        students = i[searchValue]
        print("Data is in the database")
        if len(students) == 1:
            print("Found 1 student:")
        else:
            print("Found multiple students:")
        for student in students:
            print("╔══════════════════════════════════════════════╗")
            print(f"║   Name: {student['name'].title():<36} ║")
            print(f"║   Grade: {student['grade']:<35} ║")
            print(f"║   Dob: {student['dob']:<37} ║")
            print(f"║   ID: {student['id']:<38} ║")
            print(f"║   GPA: {student['GPA']:<37} ║")
            print("╚══════════════════════════════════════════════╝")
    else:
        print("No student with", datain, "=", searchValue, "in the database")

# Main code
while True:
    sy = ("freshman", "sophomore", "junior", "senior")
    mainData = FileConvert()
    print("╔═════════════════════════════════════╗")
    print("║          STUDENT MENU                ║")
    print("╠═════════════════════════════════════╣")
    print("║  A: Add Student                      ║")
    print("║  B: Search Student                   ║")
    print("║  C: Clear File                       ║")
    print("║  X: Exit the Menu                    ║")
    print("╚═════════════════════════════════════╝")
    print()
    print("Data Information")
    print("Total Students:          ", studentEachYear(mainData)[4])
    print("Students with GPA > 3.0: ", datainfoGPA(mainData)[0])
    print("Students with GPA < 3.0: ", datainfoGPA(mainData)[1])
    print()
    print("Number of Students in Each Year")
    print("Freshman:  ", studentEachYear(mainData)[0])
    print("Sophomore: ", studentEachYear(mainData)[1])
    print("Junior:    ", studentEachYear(mainData)[2])
    print("Senior:    ", studentEachYear(mainData)[3])
    choice = input("\nCommand: ").lower()
    if choice == "x":
        print("Shutting down...")
        break
    elif choice == "a":
        while True:
            name = input("What is the student's name?: ")
            if not name.replace(" ","").isalpha():
                print("Invalid value, try again")
                continue
            break
        while True:
            dobin = input("What is the student's dob? (January 01, 2000): ")
            try:
                dob = datetime.datetime.strptime(dobin, '%B %d, %Y').date()
            except ValueError:
                print("Invalid value")
                continue
            break
        while True:
            grade = input("What year is the student in? (Freshman/Sophomore/Junior/Senior): ")
            if grade.lower() not in sy:
                print("Invalid Value")
                continue
            break
        while True:
            idin = input("What is the student's ID number?: ")
            if not idin.isdigit():
                print("Invalid Value")
                continue
            break
        while True:
            gpain = input("What is the student's GPA?: ")
            try:
                gpain = float(gpain)
            except ValueError:
                print("Invalid Value")
                continue
            break
        AddStudent(name, grade, dobin, idin, gpain)
    elif choice == "b":
        todin = input("Search by?\n"
              "Options:\n"
              "  - Name (Please Enter Full Name)\n"
              "  - ID\n"
              "  - GPA\n"
              "  - Date of Birth (DOB)\n"
              "  - Grade: ")
        value = input("Search Value: ")
        dataSearch(mainData, todin, value)
    elif choice == "c":
        print("Are you sure you want to clear the file?")
        yn = input("(y/n): ")
        while not (yn == 'y' or yn == 'n'):
            print("Invalid input, try again")
            yn = input("(y/n): ")
        if yn == "y":
            nukeFile(True)
        elif yn == "n":
            nukeFile(False)
    else:
        print("Invalid command")