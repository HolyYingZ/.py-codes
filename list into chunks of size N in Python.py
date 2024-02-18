def chunk_list(input_list, chunk_size):
    for i in range(0, len(input_list), chunk_size):
        yield input_list[i:i + chunk_size]

# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
result = list(chunk_list(original_list, chunk_size))

# Display the result
print("Original list:", original_list)
print(f"List broken into chunks of size {chunk_size}:", result)
