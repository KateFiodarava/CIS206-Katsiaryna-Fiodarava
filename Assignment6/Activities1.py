def run_length_encode(input_string: str) -> str:
    """
    This function takes a string and converts it into a run-length encoded format.
    If a character repeats, it adds the count of repetitions after the character.
    For example, "AAABCC" becomes "A3BC2".
    Parameters: input_string (str): The string to be encoded.
    Returns: str: The RLE encoded string.
    """
    encoded_string = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i-1]:
            count += 1
        else:
            encoded_string += input_string[i-1] + (str(count) if count > 1 else "")
            count = 1

    # Add the last character and its count
    encoded_string += input_string[-1] + (str(count) if count > 1 else "")
    
    return encoded_string


def run_length_decode(encoded_string: str) -> str:
    """
    This function decodes a run-length encoded string.
    It takes a string like "A3BC2" and turns it back into "AAABCC".
    Parameters: encoded_string (str): The RLE encoded string.
    Returns: str: The decoded string.
    """
    decoded_string = ""
    i = 0
    
    while i < len(encoded_string):
        char = encoded_string[i]
        
        if i + 1 < len(encoded_string) and encoded_string[i+1].isdigit():
            count = ""
            while i + 1 < len(encoded_string) and encoded_string[i+1].isdigit():
                count += encoded_string[i+1]
                i += 1
            decoded_string += char * int(count)
        else:
            decoded_string += char
        
        i += 1
    
    return decoded_string


def process_string(input_string: str) -> str:
    """
    This function checks if the input is in RLE format (contains numbers) or needs encoding.
    If the string has numbers, it will decode it; if not, it will encode it.
    Parameters: input_string (str): The string to process.
    Returns: str: The encoded or decoded string.
    """
    if any(char.isdigit() for char in input_string):
        return run_length_decode(input_string)
    else:
        return run_length_encode(input_string)


# Main Program
try:
    user_input = input("Enter a string: ")
    result = process_string(user_input)
    print(f"Processed result: {result}")
except ValueError as e:
    print(f"Error: {e}")

