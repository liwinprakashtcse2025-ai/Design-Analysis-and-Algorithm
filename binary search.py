arr = []
print("Enter 7 elements:")
for i in range(7):
    element = int(input(f"Element {i + 1}: "))
    arr.append(element)
arr.sort()
print("Sorted Array:", arr)
key = int(input("Enter the element to search: "))
low = 0
high = len(arr) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print(f"Element found at position {mid + 1}")
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("Element not found")