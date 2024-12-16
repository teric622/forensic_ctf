def embed_flag(image_file, output_file, flag):
    with open(image_file, 'rb') as f:
        data = f.read()
    insert_position = len(data) // 2
    modified_data = data[:insert_position] + flag.encode() + data[insert_position:]
    with open(output_file, 'wb') as f:
        f.write(modified_data)

    print(f"Flag embedded successfully into {output_file}")
image_file = "chicago_hidden.jpg"  
output_file = "chicago_bean.jpg"  
flag = "ZmxhZ3t5b3VfbGlrZV9iZWFuc18/X0lfbGlrZV9iZWFuc190aGFuc190aGVfdGhfYmVhfQ=="  

embed_flag(image_file, output_file, flag)

