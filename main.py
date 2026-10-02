# ENDCODER
text = input("Enter your text:")

binary = []

for letter in text:
    a = ord(letter)
    b = bin(a)
    binary.append(b[2:].zfill(8))

print("Binary:"," ".join(binary))

