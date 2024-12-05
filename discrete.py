from datetime import datetime, timedelta

class Exam:
    def __init__(self, name, color, sections):
        self.name = name
        self.color = color
        self.sections = sections

# Define exams and their respective sections
exams = [
    Exam("Discrete Structure", "Red", ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S13", "S14"]),
    Exam("Operating System", "Yellow", ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S1T", "S2T"]),
    Exam("Object-Oriented Programming", "Orange", ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S1T", "S2T"]),
    Exam("Human Computer Interaction", "Green", ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S13", "S14", "S1T", "S2T", "S3T"]),
    Exam("Requirement Engineering", "Blue", ["S3", "S4", "S11"]),
    Exam("Software Security", "Purple", ["S1", "S2", "S10"]),
    Exam("Web Application", "Light Gray", ["S5", "S6", "S13"]),
    Exam("Computer Graphic", "Brown", ["S7", "S8", "S14"]),
    Exam("Mobile Application Development", "Pink", ["S2T"]),
    Exam("Entrepreneurship", "Dark Red", ["S1T"]),
]

# Function to check if a student can take an exam at a specific time
def is_valid(exam_schedule, current_exam, current_slot):
    for exam in exam_schedule:
        if exam_schedule[exam] == current_slot and any(section in current_exam.sections for section in exam.sections):
            return False

    student_count = sum(len(exam.sections) * 25 for exam in exam_schedule if exam_schedule[exam] == current_slot)
    if student_count + len(current_exam.sections) > 400:
        return False

    for exam, slot in exam_schedule.items():
        if slot == current_slot and any(section in current_exam.sections for section in exam.sections):
            return False

    if any(slot == current_slot for slot in exam_schedule.values()):
        return False

    return True

# Depth-First Search algorithm for scheduling exams
def schedule_exams(exam_schedule, current_exam_index, slots):
    if current_exam_index == len(exams):
        return True

    current_exam = exams[current_exam_index]
    for slot in slots:
        if is_valid(exam_schedule, current_exam, slot):
            exam_schedule[current_exam] = slot

            if schedule_exams(exam_schedule, current_exam_index + 1, slots):
                return True

            exam_schedule[current_exam] = None

    return False

def print_exam_schedule(schedule):
    print("Exam Schedule:\n")
    print("| {:<35} | {:<18} | {:<70} | {:<30} | {:<14} |".format("Exam Name", "Color", "Sections", "Time Slot", "Room Capacity"))
    print("|" + "-"*37 + "|" + "-"*20 + "|" + "-"*72 + "|" + "-"*32 + "|" + "-"*16 + "|")

    for exam, slot in schedule.items():
        sections = ', '.join(exam.sections)
        room_capacity = len(exam.sections) * 25

        print("| {:<35} | {:<18} | {:<70} | {:<30} | {:<14} |".format(exam.name, exam.color, sections, slot, room_capacity))

# Create an empty exam schedule
exam_schedule = {exam: None for exam in exams}

# Define available time slots for exams
# Slots are in the format "WxDy" where x is the week number (1-3) and y is the day number (1-4, Monday to Thursday)
time_slots = [f"W{i} {j} 9.00AM to 12.00PM" for i in range(1, 4) for j in ["Monday", "Tuesday","Wednesday","Thursday"]]

# Call DFS function to schedule exams
schedule_exams(exam_schedule, 0, time_slots)

# Print the exam schedule
print_exam_schedule(exam_schedule)
