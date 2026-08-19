from dataclasses import dataclass
from typing import List


@dataclass
class Course:
    course_name: str
    duration: int
    fee: float

    def category(self) -> str:
        # 6 months or less = Short-Term
        # More than 6 months = Long-Term
        if self.duration <= 6:
            return "Short-Term"
        else:
            return "Long-Term"

    def display(self):
        print(
            f"Course: {self.course_name} | "
            f"Duration: {self.duration} months | "
            f"Fee: ₹{self.fee:.2f} | "
            f"Category: {self.category()}"
        )


class Institute:

    def __init__(self, institute_name):
        self.institute_name = institute_name
        self.courses: List[Course] = []

    def add_course(self, course: Course):
        # Check duplicate course
        for c in self.courses:
            if c.course_name.lower() == course.course_name.lower():
                print("❌ Course already exists.")
                return

        self.courses.append(course)
        print("✅ Course added successfully.")

    def display_all_courses(self):
        if not self.courses:
            print("❌ No courses available.")
            return

        print("\n========== ALL COURSES ==========")
        for course in self.courses:
            course.display()

    def display_category(self, category):
        found = False

        print(f"\n========== {category.upper()} COURSES ==========")

        for course in self.courses:
            if course.category().lower() == category.lower():
                course.display()
                found = True

        if not found:
            print("No courses found.")

    def search_course(self, name):
        found = False

        for course in self.courses:
            if name.lower() in course.course_name.lower():
                course.display()
                found = True

        if not found:
            print("❌ Course not found.")

    def total_courses(self):
        print(f"\nTotal Courses: {len(self.courses)}")


def get_course_details():

    try:
        course_name = input("Enter Course Name: ").strip()

        duration = int(
            input("Enter Duration (in months): ")
        )

        fee = float(
            input("Enter Course Fee: ")
        )

        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")

        if fee < 0:
            raise ValueError("Fee cannot be negative.")

        return Course(course_name, duration, fee)

    except ValueError as error:
        print(f"❌ Invalid input: {error}")
        return None


def main():

    institute = Institute("ABC Institute")

    while True:

        print("\n===================================")
        print("     COURSE MANAGEMENT SYSTEM")
        print("===================================")

        print("1. Add Course")
        print("2. Display All Courses")
        print("3. Search Course")
        print("4. Display Short-Term Courses")
        print("5. Display Long-Term Courses")
        print("6. Total Courses")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            course = get_course_details()

            if course:
                institute.add_course(course)

        elif choice == "2":

            institute.display_all_courses()

        elif choice == "3":

            name = input("Enter course name to search: ")
            institute.search_course(name)

        elif choice == "4":

            institute.display_category("Short-Term")

        elif choice == "5":

            institute.display_category("Long-Term")

        elif choice == "6":

            institute.total_courses()

        elif choice == "7":

            print("Thank you for using Course Management System!")
            break

        else:

            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
