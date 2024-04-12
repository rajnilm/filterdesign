from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.439
B_val =0.0931

# Define s_L in terms of s, omega0, and B
s_L = (s**2 + omega0_val**2) / (B_val * s)

# Given roots
s1 = -0.1326+0.9777j
s2 = -0.3200+0.4050j
s3 = -0.3200-0.4050j 
s4 = -0.1326-0.9777j

# Define the given polynomial expression
polynomial_expr = 0.227/ ((s_L - s1) * (s_L - s2) * (s_L - s3) * (s_L - s4))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
