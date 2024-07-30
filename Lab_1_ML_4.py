def find_max_occurrence(input_string):
    char_count = {}
    
    for char in input_string:
        if char.isalpha():  
            char_count[char] = char_count.get(char, 0) + 1
    
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    
    return max_char, max_count

input_string = input("Enter the string")
max_char, max_count = find_max_occurrence(input_string)
print(f"The most occurring character is '{max_char}' with a count of {max_count}.")
