students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    print("Enter 3 subject marks:")
    m1 = float(input("Mark 1: "))
    m2 = float(input("Mark 2: "))
    m3 = float(input("Mark 3: "))
    marks = (m1, m2, m3)
    student = {"name": name, "age": age, "marks": marks}
    students.append(student)
    print(f"\nStudent '{name}' added successfully!\n")

def calculate_average(marks):
    return sum(marks) / len(marks)

def display_students():
    if not students:
        print("\nNo students found.\n")
        return
    print("\n" + "="*50)
    print(f"{'No':<4} {'Name':<15} {'Age':<5} {'Marks':<20} {'Average'}")
    print("="*50)
    for i, s in enumerate(students, 1):
        avg = calculate_average(s["marks"])
        print(f"{i:<4} {s['name']:<15} {s['age']:<5} {str(s['marks']):<20} {avg:.2f}")
    print("="*50 + "\n")

def find_topper():
    if not students:
        print("\nNo students found.\n")
        return
    topper = students[0]
    for s in students:
        if calculate_average(s["marks"]) > calculate_average(topper["marks"]):
            topper = s
    avg = calculate_average(topper["marks"])
    print("\nTopper Details")
    print("-"*30)
    print(f"Name    : {topper['name']}")
    print(f"Age     : {topper['age']}")
    print(f"Marks   : {topper['marks']}")
    print(f"Average : {avg:.2f}\n")

def main():
    print("\nStudent Management System")
    print("="*30)
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Find Topper")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            find_topper()
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter 1-4.\n")

main()
