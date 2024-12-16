def add_decoys_to_file(file_path, output_path, real_flag, decoys):
    # Read the original file content
    with open(file_path, "rb") as f:
        binary_data = f.read()
    
    # Combine the real flag and decoys
    decoys.append(real_flag)
    mixed_content = "\n".join(decoys).encode()

    # Append the decoys to the file and save the output
    with open(output_path, "wb") as f:
        f.write(binary_data + mixed_content)

# File paths
input_file = "chicago.jpg"
output_file = "chicago_bean_mystery.jpg"

# The real flag (Base64 encoded)
real_flag = "ZmxhZ3t5b3VfbGlrZV9iZWFucz9fSV9saWtlX2JlYW5zX3RoYXRfYV9iaWdfYmVhbl9ldG19"

# Decoy strings
decoys = [
    "flag{A_picture_is_worth_1000_words}", # Another long fake flag
    "TWF5YmUgdGhpcyBpcyBhIGZsYWcgdG8gZGlnIGRlZXBlcg==",  # Random Base64
    "U29tZSBwZW9wbGUganVzdCB3YW50IHRvIGxvb2sgYmFja3dhcmQ=",  # Random Base64
    "flag{cefmcec_okdeo_I_really_like_beans_do_you_?_the_bean_is_big_dcjenc4993ej}",  # Long fake flag
    
]

# Add decoys and save the output file
add_decoys_to_file(input_file, output_file, real_flag, decoys)
print(f"Decoys and real flag added to {output_file}")
