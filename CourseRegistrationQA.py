from CourseRegistration import CourseRegistration


system = CourseRegistration()

# Valid registration
system.register(
    "S001", "M.Tech SE", 5,
    ["DBMS"],
    ["Programming"],
    8
)

# Missing prerequisite
system.register(
    "S002", "M.Tech SE", 5,
    ["DBMS"],
    [],
    8
)

# Credit-limit violation
system.register(
    "S003", "M.Tech SE", 5,
    ["DBMS", "AI", "ML"],
    ["Programming", "Data Structures", "Statistics"],
    6
)

# Timetable conflict
system.register(
    "S004", "M.Tech SE", 5,
    ["DBMS", "ML"],
    ["Programming", "Statistics"],
    8
)

# Full course
system.register(
    "S005", "M.Tech SE", 5,
    ["DBMS"],
    ["Programming"],
    8
)

# Duplicate registration
system.register(
    "S001", "M.Tech SE", 5,
    ["DBMS"],
    ["Programming"],
    8
)

# Invalid course
system.register(
    "S006", "M.Tech SE", 5,
    ["CyberSecurity"],
    [],
    8
)

# Semester restriction
system.register(
    "S007", "M.Tech SE", 4,
    ["DBMS"],
    ["Programming"],
    8
)

# Boundary credit values
system.register(
    "S008", "M.Tech SE", 5,
    ["DBMS", "AI"],
    ["Programming", "Data Structures"],
    8
)

print("Course Registration QA completed")
