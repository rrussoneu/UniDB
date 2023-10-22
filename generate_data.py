import random
import csv

'''
  A python script to generate some dummy data for use.
  There is obvious room for expansion as students are only taking courses in their majors, for example, and there are only so many courses listed.
'''


def main():
    # List of random names to pick from
    FIRST_NAMES = ["John", "Jane", "Alex", "Emily", "Chris", "Kate", "Robert", "Linda", "Michael", "Sarah",
                   "Daniel", "Nina", "Lucas", "Sophia", "Oliver", "Isabella", "William", "Mia", "James", "Amelia"]

    LAST_NAMES = ["Smith", "Doe", "Johnson", "Lee", "Brown", "Davis", "Rodriguez", "Martinez", "Garcia", "Wilson",
                  "Taylor", "Moore", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Young"]

    # Some typical university departments
    DEPARTMENTS = [
        {"DepartmentCode": "MATH", "DepartmentName": "Mathematics"},
        {"DepartmentCode": "ENGL", "DepartmentName": "English"},
        {"DepartmentCode": "PHYS", "DepartmentName": "Physics"},
        {"DepartmentCode": "CHEM", "DepartmentName": "Chemistry"},
        {"DepartmentCode": "BIO", "DepartmentName": "Biology"},
        {"DepartmentCode": "HIST", "DepartmentName": "History"}
    ]
    
    BUILDINGS = ["Schrute Hall", "Dyson Center", "Quadrangle Overlook"]
    
    # A few random courses for each department
    COURSES = {
        "MATH": ["Algebra", "Calculus", "Statistics", "Discrete Math"],
        "ENGL": ["Literature 101", "Creative Writing", "Literature 201", "Technical Writing"],
        "PHYS": ["Mechanics", "Electromagnetism", "Quantum Physics", "Thermal Physics"],
        "CHEM": ["Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Biochemistry"],
        "BIO": ["Botany", "Zoology", "Microbiology", "Genetics"],
        "HIST": ["World History", "European History", "American History", "Asian History"]
    }
    
    department_heads = {
      "Mathematics": -1,
      "English": -1,
      "Physics": -1,
      "Chemistry": -1,
      "Biology": -1,
      "History": -1,
      }

    # Some codes for the courses
    # e.g. Alegbra = MATH101    
    # In the future, it may be useful to dynamically generate codes based on the courses if more are added, but for now this will do since there are only a few

    COURSE_CODES = {
      "Algebra": 101, 
      "Calculus": 110,
      "Statistics": 120,
      "Discrete Math": 130,
      "Literature 101": 106, 
      "Creative Writing": 210,
      "Literature 201": 232,
      "Technical Writing": 235,
      "Mechanics": 100, 
      "Electromagnetism": 210, 
      "Quantum Physics": 320,
      "Thermal Physics": 430,
      "Organic Chemistry": 101,
      "Inorganic Chemistry": 102,
      "Physical Chemistry": 201,
      "Biochemistry": 202,
      "Botany": 101, 
      "Zoology": 110,
      "Microbiology": 210,
      "Genetics": 300,
      "World History": 100,
      "European History": 105,
      "American History": 111,
      "Asian History": 112
    }

    
    # A few past semesters and one future     
    SEMESTERS = ["Sp21", "Su21", "Fa21", "Sp22", "Su22", "Fa22", "Sp23", "Su23", "Fa23", "Sp24"]

    # Major/ Department to code
    MAJOR_TO_CODE = {
        "Mathematics": "MATH",
        "English": "ENGL",
        "Physics": "PHYS",
        "Chemistry": "CHEM",
        "Biology": "BIO",
        "History": "HIST"
    }

    # Generate random faculty members
    faculty_records = []
    for idx, _ in enumerate(range(30)):  # 30 faculty members
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        dob = f"19{random.randint(60, 99)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        email = f"{first_name.lower()}.{last_name.lower()}{idx + 1}@university.edu"
        faculty_records.append({
            "FacultyID": idx + 1,
            "FacultyFirstName": first_name,
            "FacultyLastName": last_name,
            "FacultyDOB": dob,
            "FacultyEmail": email
        })
        
 # Generate random students and their courses
    student_records = []
    for idx, _ in enumerate(range(500)):  # Generate 500 students and their courses
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        dob = f"20{random.randint(0, 2):02}-{random.randint(1, 12):02}-{random.randint(1, 28):02}" # Random birthdate
        grad_date = "2024"  # Assuming all are set to graduate in 2024 for simplicity
        email = f"{first_name.lower()}.{last_name.lower()}{idx}@university.edu"
        major = random.choice(DEPARTMENTS)["DepartmentName"] # Give them a random major
        student_records.append({
            "StudentID": idx + 1,
            "StudentFirstName": first_name,
            "StudentLastName": last_name,
            "StudentEmail": email,
            "StudentDOB": dob,
            "StudentGradDate": grad_date,
            "StudentMajor": major
        })

    # Days for course offerings
    DAYS_OF_WEEK = ["M", "T", "W", "R", "F"]

    # Store details for courses for consistency across students
    course_cache = {}
    classroom_cache = {}
    
    classroom_keys = []
    # Generate Classrooms
    for building in BUILDINGS:
      rms = []
      for i in range(1, 6):
        used = True
        while used:
          room_number = random.randint(10, 40)
          if room_number not in rms:
            rms.append(room_number)
            used = False
        classroom_key = f"{building}_{room_number}"
        capacity = random.randint(15, 90)
        if classroom_key not in classroom_cache:
          classroom_cache[classroom_key] = {
            "Building": building,
            "RoomNumber": room_number,
            "Capacity": capacity
          }
          classroom_keys.append(classroom_key)
    
    records = []
    
    # Assigning department heads randomly
    for d in DEPARTMENTS:
      needs_head = True
      while needs_head:
        faculty = random.choice(faculty_records)
        department_heads[d["DepartmentName"]] = faculty["FacultyID"] if faculty["FacultyID"] not in department_heads.values() else -1
        if (department_heads[d["DepartmentName"]] != -1):
          needs_head = False
    
    
    for student in student_records:
        #print(student)
        student_courses = random.sample(
            list(COURSES[MAJOR_TO_CODE[student["StudentMajor"]]]),
            min(len(COURSES[MAJOR_TO_CODE[student["StudentMajor"]]]), random.randint(2, 5)))
        semester = random.choice(SEMESTERS)

        for course_name in student_courses:
            #print(course_name)
            department_code = [d["DepartmentCode"] for d in DEPARTMENTS if d["DepartmentName"] == student["StudentMajor"]][0]
            department_name = [d["DepartmentName"] for d in DEPARTMENTS if d["DepartmentName"] == student["StudentMajor"]][0] # clean this up
            course_code = COURSE_CODES[course_name]
            course_key = f"{department_code}{course_code}_{semester}"  # Unique key for each course in a specific semester

            if course_key not in course_cache:
                faculty = random.choice(faculty_records)
                #if department_heads[department_name] == -1:
                  #needs_head = True
                  #while needs_head:
                  #department_heads[department_name] = faculty["FacultyID"] if faculty["FacultyID"] not in department_heads.values() else -1
                    #if (department_heads[department_name] != -1):
                      #needs_head = False
                    #else:
                      
                start_time = f"12:00"
                end_time = f"14:00"
                
                days_of_week = "".join(random.sample(DAYS_OF_WEEK, random.randint(1, 3)))
                #building = random.choice(BUILDINGS)
                classroom_key = random.choice(classroom_keys)
                #print(classroom_cache)
                # Store this in course_cache for consistent details across students
                course_cache[course_key] = {
                    "CourseName": course_name,
                    "DepartmentCode": department_code,
                    "DepartmentName": department_name,
                    "DepartmentHead": department_heads[department_name],
                    "CourseCode": course_code,
                    "FacultyID": faculty["FacultyID"],
                    "FacultyFirstName": faculty["FacultyFirstName"],
                    "FacultyLastName": faculty["FacultyLastName"],
                    "FacultyDOB": faculty["FacultyDOB"],
                    "FacultyEmail": faculty["FacultyEmail"],
                    "DaysOfWeek": days_of_week,
                    "StartTime": start_time,
                    "EndTime": end_time,
                    "Grade": None,  # Grade will be assigned later for past semesters and left null if they have not taken the course yet,
                    "Building": classroom_cache[classroom_key]["Building"],
                    "RoomNumber": classroom_cache[classroom_key]["RoomNumber"],
                    "Capacity": classroom_cache[classroom_key]["Capacity"]
                }

            # Fetching course details from cache
            cached_course_details = course_cache[course_key]

            record = {
                **student,  # Student details
                **cached_course_details,  # Cached course details
                "Semester": semester,
                "IsRequired": random.choice([True, False])  # Randomly setting if a course is required
            }

            # Assign a grade if the semester is in the past, assuming 67 is typical low end for passing a class
            if SEMESTERS.index(semester) <= SEMESTERS.index("Su23"): # At the present date, it is Fa23 semester
                record["Grade"] = round(random.uniform(67, 100), 2)
            records.append(record)

    # Headers for csv file
    headers = [
        "StudentID", "StudentFirstName", "StudentLastName", "StudentEmail", "StudentDOB", "StudentGradDate",
        "StudentMajor", "CourseName", "DepartmentCode", "DepartmentName", "DepartmentHead","CourseCode", "Semester",
        "FacultyID", "FacultyFirstName", "FacultyLastName", "FacultyDOB", "FacultyEmail",
        "DaysOfWeek", "StartTime", "EndTime", "IsRequired", "Grade", "Building", "RoomNumber", "Capacity"
    ]

    # Write data to a csv
    with open('generated_u_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

    print("CSV file written successfully!")

if __name__ == "__main__":
    main()
