# ENDCODER 🐍
# Convert normal text into binary

# Get text from the user
text = input("Enter your text: ")

# Empty list to store binary values
binary = []

# Go through each character in the text
for letter in text:
    # Convert character into its number (ASCII/Unicode)
    a = ord(letter)

    # Convert the number into binary
    b = bin(a)

    # Remove "0b" and make it at least 8 bits
    binary.append(b[2:].zfill(8))

# Print all binary values separated by spaces
print("Binary:", " ".join(binary))
