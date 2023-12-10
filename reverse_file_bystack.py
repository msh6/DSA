from arraystack import ArrayStack

def reverse_file(filename):
    '''Overwrite given file with its content line by line reversed.'''
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.strip('\n'))            # we will re-insert newlines when writing
    original.close()
    
    # now we overwrite the contents in LIFO order 
    output = open(filename, 'w')            # reopening the file overwrites the original
    while not S.is_empty():
        output.write(S.pop() + '\n')        # re-insert newline characters
    output.close()

text_file = "sample_text.txt"

# Print the original content
print("Original content:")
with open(text_file, 'r') as file:
    for line in file:
        print(line, end='')

# Reverse the file
reverse_file(text_file)

# Print the reversed content
print("\nReversed content:")
with open(text_file, 'r') as file:
    for line in file:
        print(line, end='')