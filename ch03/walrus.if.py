value = 42
modulus = 11

# Without assignment expression:
remainder = value % modulus
if remainder:
    print(f"Not divisible! The remainder is {remainder}.")


# Rewritten with assignment expression:
if remainder := value % modulus:
    print(f"Not divisible! The remainder is {remainder}.")
