# Initialize a 3x3 identity matrix
identity_matrix = []

for i in range(3):
    row = []
    for j in range(3):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    identity_matrix.append(row)

# Print the matrix
for row in identity_matrix:
    print(row)
