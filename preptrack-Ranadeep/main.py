# ==================================================
# PREPTRACK — BOILERPLATE CODE
# Complete every section marked TODO.
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# TODO: Validate that the student name is not empty.
student_name = input("Enter student name: ")
while not student_name:
    print("Student name cannot be empty")
    student_name = input("Enter student name: ")

registration_number = input("Enter registration number: ")
graduation_year = int(input("Enter graduation year: "))

# TODO: Validate attendance between 0 and 100.
attendance = float(input("Enter attendance percentage: "))
while attendance <0 or attendance>100:
    print("Invalid attendance. Enter a value between 0 and 100.")
    attendance = float(input("Enter attendance percentage: "))

# TODO: Accept only yes or no.
project_input = input("Has the student completed the required project? Enter yes or no: ")
while project_input != "yes" and project_input != "no":
    print("Invalid input. Enter yes or no.")
    project_input = input("Has the student completed the required project? Enter yes or no: ")



# TODO: Convert project_input into True or False.
project_completed = False
if project_input == "yes":
    project_completed = True
else:
    project_completed = False

# TODO: Accept only yes or no.
profile_input = input("Is the student profile verified? Enter yes or no: ")

while profile_input != 'yes' and profile_input != 'no':
    print("Invalid input. Enter yes or no.")
    profile_input = input("Is the student profile verified? Enter yes or no: ")


# TODO: Convert profile_input into True or False.
profile_verified = False
if profile_input=="yes":
    profile_verified=True
else:
    profile_verified=False


# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 101
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0


# --------------------------------------------------
# 3. PROCESS SEVEN PRACTICE DAYS
# --------------------------------------------------

for day in range(1, 8):
    # Accept only -1 or a score between 0 and 100
    score = int(input(f"Enter Day {day} score from 0 to 100, or -1 for absent: "))

    while score != -1 and (score < 0 or score > 100):
        print("Invalid score. Enter a value between 0 and 100, or -1 for absent.")
        score = int(input(f"Enter Day {day} score from 0 to 100, or -1 for absent: "))

    # TODO: Handle absence.
    # Increase absent_days and use continue.
    if score == -1:
        absent_days += 1
        continue

    # TODO: Increase attempted_days and total_score.
    attempted_days += 1
    total_score += score

    # TODO: Initialize or update:
    # highest_score, highest_score_day,
    if score > highest_score:
        highest_score = score
        highest_score_day = day
    # lowest_score and lowest_score_day.
    if score < lowest_score:
        lowest_score = score
        lowest_score_day = day

    # TODO: Classify the score:
    # 75–100  -> Strong
    # 60–74   -> Satisfactory
    # 40–59   -> Needs Improvement
    # 0–39    -> Critical
    if 75 <= score <= 100:
        strong_days+=1
    elif 60 <= score <= 74:
        satisfactory_days+=1
    elif 40 <= score <= 59:
        improvement_days+=1
    else:   
        critical_days+=1

    # TODO: Count passed and failed days.
    if score >= 40:
        passed_days += 1
    else:
        failed_days += 1


    # TODO: Store only the first critical day and score.
    if score < 40 and critical_score_found == False:
        first_critical_day = day
        first_critical_score = score
        critical_score_found = True


# --------------------------------------------------
# 4. CALCULATE THE AVERAGE
# --------------------------------------------------

# TODO: Prevent division by zero.
average_score = 0
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0


# --------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# --------------------------------------------------

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)


# --------------------------------------------------
# 6. DETERMINE FINAL STATUS
# --------------------------------------------------

# TODO: Check conditions in this priority:
# 1. No practice attempted
# 2. Critical score found
# 3. Fewer than six attempts
# 4. Fewer than four passed days
# 5. Average below 70
# 6. Attendance below 75
# 7. Graduation year not eligible
# 8. Project incomplete
# 9. Profile not verified
# 10. Ready for Mock Interview

final_status = ""
primary_blocker = ""
next_action = ""
if attempted_days == 0:
    final_status = "Not Ready"
    primary_blocker = "No practice attempted"
    next_action = "Start daily practice immediately."
elif critical_score_found:
    final_status = "Not Ready"
    primary_blocker = "Critical Score was found"
    next_action = "Revise weak topics and reattempt practice."
elif attempted_days < 6:
    final_status = "Not Ready"
    primary_blocker = "Fewer than six practice attempts"
    next_action = "Complete at least six practice sessions."
elif passed_days < 4:
    final_status = "Not Ready"
    primary_blocker = "Fewer than four passed days"
    next_action = "Improve consistency and pass more practice days."
elif average_score < 70:
    final_status = "Not Ready"
    primary_blocker = "Average score below 70"
    next_action = "Increase average score through targeted practice."
elif attendance < 75:
    final_status = "Not Ready"
    primary_blocker = "Attendance below 75%"
    next_action = "Improve attendance before the interview process."
elif graduation_year!=2025 and graduation_year!=2026:
    final_status = "Not Ready"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check eligibility criteria for current openings."
elif  project_completed==False:
    final_status = "Not Ready"
    primary_blocker = "Project incomplete"
    next_action = "Complete the required project."
elif  profile_verified==False:
    final_status = "Not Ready"
    primary_blocker = "Profile not verified"
    next_action = "Complete profile verification."
else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "All criteria satisfied"
    next_action = "Proceed to Mock Interview"

# --------------------------------------------------
# 7. DISPLAY FINAL REPORT
# --------------------------------------------------

print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)

print(f"Student Name           : {student_name}")
print(f"Registration Number    : {registration_number}")
print(f"Graduation Year        : {graduation_year}")
print(f"Attendance             : {attendance}%")

print()
print(f"Attempted Days         : {attempted_days}")
print(f"Absent Days            : {absent_days}")
print(f"Passed Days            : {passed_days}")
print(f"Failed Days            : {failed_days}")

print()
print(f"Strong Days            : {strong_days}")
print(f"Satisfactory Days      : {satisfactory_days}")
print(f"Needs Improvement Days : {improvement_days}")
print(f"Critical Days          : {critical_days}")

print()
print(f"Total Score            : {total_score}")
print(f"Average Score          : {average_score:.2f}")

# TODO: Display highest and lowest values only when
# at least one practice was attempted.
if attempted_days > 0:
    print(f"Highest Score          : {highest_score} ")
    print(f"Lowest Score           : {lowest_score} ")

# TODO: Display first critical details only when
# a critical score exists.
if critical_score_found:
    print(f"First Critical Day     : Day {first_critical_day}")
    print(f"First Critical Score   : {first_critical_score}")

print()
print(f"Final Status           : {final_status}")
print(f"Primary Blocker        : {primary_blocker}")
print(f"Next Action            : {next_action}")

print("=" * 50)