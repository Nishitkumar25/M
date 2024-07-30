def calculate_range(numbers):
    if len(numbers) < 3:
        return "Range determination not possible"
    
    min_val = min(numbers)
    max_val = max(numbers)
    return max_val - min_val

input_count = int(input("Input the total number of elements in the list: "))
input_list = []
for i in range(input_count):
    input_value = float(input(f"Enter value {i + 1}: "))
    input_list.append(input_value)

result = calculate_range(input_list)
print(f"Range: {result}")

