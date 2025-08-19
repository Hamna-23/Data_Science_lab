import numpy as np

# -----------------------------
# 1. Create a matrix
# -----------------------------
A = np.array([[3, 1], [1, 3]])
print("Original Matrix A:\n", A)

# -----------------------------
# 2. Vectorized operation (e.g., element-wise square)
# -----------------------------
squared = A ** 2
print("\nElement-wise Squared Matrix:\n", squared)

# -----------------------------
# 3. Matrix transformation (Scaling and Rotation)
# -----------------------------
# Scaling matrix
scale = np.array([[2, 0], [0, 3]])

# Rotation matrix (45 degrees)
theta = np.radians(45)
rotate = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# Apply transformation: Rotate then Scale
transformed = scale @ rotate @ A
print("\nTransformed Matrix (Scaled + Rotated):\n", transformed)

# -----------------------------
# 4. Singular Value Decomposition (SVD)
# -----------------------------
U, S, VT = np.linalg.svd(A)

print("\nSVD Decomposition:")
print("U (Left Singular Vectors):\n", U)
print("S (Singular Values):\n", S)
print("VT (Right Singular Vectors Transposed):\n", VT)

# Reconstruct A using SVD
Sigma = np.zeros_like(A, dtype=float)
np.fill_diagonal(Sigma, S)
A_reconstructed = U @ Sigma @ VT

print("\nReconstructed A from SVD:\n", A_reconstructed)
