nums = [45, 89, 34, 29, 98]
largest = nums[0]
smallest = None
for num in nums:
    if num > largest:
        largest = num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num  

print(f'Largest: {largest}')
print(f'Largest: {smallest}')

