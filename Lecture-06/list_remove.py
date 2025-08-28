fruits_with_duplicates = ['apple', 'banana', 'apple', 'cherry', 'apple', 'kiwi']
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Fruits list after removing 'apple': {fruits_with_duplicates}")