from sympy import mod_inverse

# Input your values here
p = 219920443573698782845930677192261022747
q = 262725443219511029142449525203053232189
e = 65537
c = 19759948204827148967716452284363638954256347121332992994807595069379938069646

# Calculate n and φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# Compute private exponent d
d = mod_inverse(e, phi)

# Decrypt ciphertext
m = pow(c, d, n)

num_bytes = (m.bit_length() + 7) // 8
message_bytes = m.to_bytes(num_bytes, 'big')

message = message_bytes.decode('utf-8')  # or 'ascii' if you know it's ASCII
print(message)
