file_path = "chicago_bean_mystery_2.jpg"
def extract_long_strings(file_path, min_length=20):
    with open(file_path, "rb") as file:
        binary_data = file.read()
    readable_strings = "".join(chr(byte) if 32 <= byte <= 126 else " " for byte in binary_data)
    long_strings = [s for s in readable_strings.split() if len(s) >= min_length]
    return long_strings
min_length = 20
long_strings = extract_long_strings(file_path, min_length)
print(f"Strings {min_length} characters or longer:")
for string in long_strings:
    print(string)
