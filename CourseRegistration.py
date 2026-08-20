class CourseRegistration:

    def __init__(self):
        self.courses = {
            "DBMS": {
                "credits": 4,
                "prerequisite": "Programming",
                "capacity": 2,
                "semester": 5,
                "time": "09:00"
            },
            "AI": {
                "credits": 4,
                "prerequisite": "Data Structures",
                "capacity": 2,
                "semester": 5,
                "time": "10:00"
            },
            "ML": {
                "credits": 3,
                "prerequisite": "Statistics",
                "capacity": 2,
                "semester": 5,
                "time": "09:00"
            },
            "Cloud": {
                "credits": 3,
                "prerequisite": "Networking",
                "capacity": 2,
                "semester": 5,
                "time": "11:00"
            }
        }

        self.registrations = {}

    def register(self, student_id, program, semester,
                 selected_courses, completed_courses,
                 credit_limit):

        if student_id not in self.registrations:
            self.registrations[student_id] = []

        current = self.registrations[student_id]

        for course in selected_courses:

            if course not in self.courses:
                print("Invalid course:", course)
                continue

            if course in current:
                print("Duplicate registration:", course)
                continue

            details = self.courses[course]

            if semester != details["semester"]:
                print("Semester restriction:", course)
                continue

            prerequisite = details["prerequisite"]

            if prerequisite not in completed_courses:
                print("Missing prerequisite:", course)
                continue

            current_credits = sum(
                self.courses[c]["credits"] for c in current
            )

            if current_credits + details["credits"] > credit_limit:
                print("Credit limit exceeded")
                continue

            if len(current) >= details["capacity"]:
                print("Course capacity full:", course)
                continue

            clash = False

            for registered_course in current:
                if self.courses[registered_course]["time"] == details["time"]:
                    clash = True
                    break

            if clash:
                print("Timetable clash:", course)
                continue

            current.append(course)
            print("Registered successfully:", course)

        total_credits = sum(
            self.courses[c]["credits"] for c in current
        )

        print("Total registered credits:", total_credits)


registration = CourseRegistration()

registration.register(
    "S001",
    "M.Tech SE",
    5,
    ["DBMS"],
    ["Programming"],
    8
)

registration.register(
    "S001",
    "M.Tech SE",
    5,
    ["AI"],
    ["Programming", "Data Structures"],
    8
)

print(registration.registrations)
