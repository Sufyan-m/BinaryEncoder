# ENDCODER - Convert normal text into binary

def text_to_binary(text: str) -> str:
    """Converts text into clean 8-bit binary blocks using format()."""
    binary_values = []
    
    for letter in text:
        # format(ord(letter), '08b') automatically converts to binary,
        # removes '0b', and pads it to 8 bits (no slicing or zfill needed!)
        binary_bits = format(ord(letter), '08b')
        binary_values.append(binary_bits)
        
    return " ".join(binary_values)

def main():
    # Get text from the user
    text = input("Enter your text: ").strip()
    
    # Validation: Check if the user just pressed Enter without typing anything
    if not text:
        print("Error: Please enter some valid text!")
        return
        
    # Get the binary result and print it
    result = text_to_binary(text)
    print(f"Binary: {result}")

# Standard entry point for professional Python scripts
if __name__ == "__main__":
    main()
