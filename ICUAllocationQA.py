from ICUAllocation import ICUAllocation


icu = ICUAllocation(2)

# Critical patient
icu.allocate_patient(
    "P001", 70, 85, 130, (85, 60), 39.5,
    ["Heart disease"]
)

# Normal patient
icu.allocate_patient(
    "P002", 30, 98, 80, (120, 80), 37,
    []
)

# Emergency case
icu.allocate_patient(
    "P003", 60, 88, 125, (90, 60), 38.5,
    ["Diabetes"], emergency=True
)

# No ICU beds
icu.allocate_patient(
    "P004", 50, 95, 90, (120, 80), 37,
    []
)

# Duplicate patient
icu.allocate_patient(
    "P001", 70, 90, 90, (120, 80), 37,
    []
)

# Invalid oxygen level
icu.allocate_patient(
    "P005", 40, 150, 90, (120, 80), 37,
    []
)

# Invalid heart rate
icu.allocate_patient(
    "P006", 40, 95, -10, (120, 80), 37,
    []
)

# Priority boundary values
icu.allocate_patient(
    "P007", 40, 93, 100, (120, 80), 37,
    []
)

# Multiple patients competing for beds
icu.allocate_patient(
    "P008", 55, 91, 125, (85, 60), 39,
    ["Asthma"]
)

print("ICU QA completed")
icu.show_status()
