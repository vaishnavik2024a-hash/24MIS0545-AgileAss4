from InsuranceClaim import InsuranceClaim


system = InsuranceClaim()

# Valid claim
system.process_claim(
    "POL1001", "CUS001", "Health", 50000,
    "2025-01-01", "2026-01-01",
    0, 30, "Medical", True
)

# Expired policy / old incident example
system.process_claim(
    "POL1002", "CUS002", "Vehicle", 50000,
    "2025-01-01", "2025-06-01",
    0, 35, "Accident", True
)

# Claim before policy start
system.process_claim(
    "POL1003", "CUS003", "Health", 30000,
    "2026-01-01", "2025-12-01",
    0, 40, "Medical", True
)

# Excessive claim amount
system.process_claim(
    "POL1004", "CUS004", "Health", 150000,
    "2025-01-01", "2026-01-01",
    0, 40, "Medical", True
)

# Missing documents
system.process_claim(
    "POL1005", "CUS005", "Vehicle", 50000,
    "2025-01-01", "2026-01-01",
    0, 40, "Accident", False
)

# Multiple previous claims
system.process_claim(
    "POL1006", "CUS006", "Health", 50000,
    "2025-01-01", "2026-01-01",
    5, 40, "Medical", True
)

# Fraud scenario
system.process_claim(
    "POL1007", "CUS007", "Health", 150000,
    "2026-01-01", "2026-01-03",
    5, 40, "Medical", False
)

# Boundary claim amount
system.process_claim(
    "POL1008", "CUS008", "Health", 100000,
    "2025-01-01", "2026-01-01",
    0, 40, "Medical", True
)

# Invalid policy number
system.process_claim(
    "", "CUS009", "Health", 30000,
    "2025-01-01", "2026-01-01",
    0, 40, "Medical", True
)

# Invalid incident date
system.process_claim(
    "POL1010", "CUS010", "Health", 30000,
    "2025-01-01", "2024-01-01",
    0, 40, "Medical", True
)

print("Insurance Claim QA completed")
