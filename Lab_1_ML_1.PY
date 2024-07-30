def find_pairs_with_sum(arr, target_sum):
    pairs = []  

    visited = set()

    for num in arr:
        complement = target_sum - num
        if complement in visited:
            pairs.append((num, complement))
        visited.add(num)

    return pairs

arr = [2, 7, 4, 1, 3, 6]
target_sum = 10
result_pairs = find_pairs_with_sum(arr, target_sum)

if result_pairs:
    print(f"Pairs with sum {target_sum}:")
    for pair in result_pairs:
        print(pair)
else:
    print(f"No pairs found with sum {target_sum}.")

