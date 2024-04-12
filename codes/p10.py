import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s =1.5265e-4 * s**4 / (s**8 + 0.1795*s**7 + 0.8112*s**6 + 0.1075*s**5 + 0.2396*s**4 + 0.0209*s**3 + 0.03052*s**2 + 0.00131*s + 0.00142)
# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)
