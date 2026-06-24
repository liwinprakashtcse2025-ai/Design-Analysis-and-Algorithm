arr = []
print("Enter 7 elements:")
for i in range(7):
    element = int(input(f"Element {i + 1}: "))
    arr.append(element)
key = int(input("Enter the element to search: "))
found = False
for i in range(7):
    if arr[i] == key:
        print(f"Element found at position {i + 1}")
        found = True
        break
if not found:
    print("Element not found")