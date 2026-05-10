from constraint import Problem

# Create problem
problem = Problem()

# Regions
regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Colours
colours = ["Red", "Green", "Blue"]

# Add variables
for region in regions:
    problem.addVariable(region, colours)

# Constraints
constraints = [
    ("WA", "NT"),
    ("WA", "SA"),
    ("NT", "SA"),
    ("NT", "Q"),
    ("SA", "Q"),
    ("SA", "NSW"),
    ("SA", "V"),
    ("Q", "NSW"),
    ("NSW", "V"),
]

# Add constraints
for region1, region2 in constraints:
    problem.addConstraint(lambda x, y: x != y, (region1, region2))

# Get solution
solution = problem.getSolution()

# Print solution
print("Australia Map Colouring Solution:")
print(solution)