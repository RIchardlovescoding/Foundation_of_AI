# pyrefly: ignore [missing-import]
from constraint import Problem

# Create CSP problem
problem = Problem()

# Nairobi sub-counties
subcounties = [
    "Westlands",
    "Dagoretti_North",
    "Dagoretti_South",
    "Langata",
    "Kibra",
    "Roysambu",
    "Kasarani",
    "Ruaraka",
    "Embakasi_North",
    "Embakasi_South",
    "Embakasi_Central",
    "Embakasi_East",
    "Embakasi_West",
    "Makadara",
    "Kamukunji",
    "Starehe",
    "Mathare",
]

# Colours available
colours = ["Red", "Green", "Blue"]

# Add variables
for subcounty in subcounties:
    problem.addVariable(subcounty, colours)

# Neighbour relationships
neighbours = [
    ("Westlands", "Dagoretti_North"),
    ("Westlands", "Starehe"),
    ("Westlands", "Mathare"),
    ("Westlands", "Kasarani"),
    ("Dagoretti_North", "Dagoretti_South"),
    ("Dagoretti_North", "Kibra"),
    ("Dagoretti_North", "Starehe"),
    ("Dagoretti_South", "Langata"),
    ("Dagoretti_South", "Kibra"),
    ("Langata", "Kibra"),
    ("Langata", "Embakasi_South"),
    ("Kibra", "Starehe"),
    ("Roysambu", "Kasarani"),
    ("Roysambu", "Ruaraka"),
    ("Kasarani", "Ruaraka"),
    ("Kasarani", "Mathare"),
    ("Kasarani", "Embakasi_North"),
    ("Ruaraka", "Mathare"),
    ("Ruaraka", "Embakasi_North"),
    ("Embakasi_North", "Embakasi_Central"),
    ("Embakasi_North", "Embakasi_East"),
    ("Embakasi_Central", "Embakasi_East"),
    ("Embakasi_Central", "Embakasi_West"),
    ("Embakasi_Central", "Makadara"),
    ("Embakasi_East", "Embakasi_South"),
    ("Embakasi_West", "Makadara"),
    ("Makadara", "Kamukunji"),
    ("Makadara", "Starehe"),
    ("Kamukunji", "Starehe"),
    ("Kamukunji", "Mathare"),
    ("Starehe", "Mathare"),
]

# Constraint:
# Adjacent regions cannot have same colour
for area1, area2 in neighbours:
    problem.addConstraint(lambda x, y: x != y, (area1, area2))

# Solve problem
solution = problem.getSolution()

# Display results
print("Nairobi Sub-Counties Colouring Solution:\n")

for subcounty, colour in solution.items():
    print(f"{subcounty}: {colour}")