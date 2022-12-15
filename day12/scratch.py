list_1 = ['apple', 'banana', 'kiwi']
list_2 = ['melon', 'avocado', 'apple']

# ✅ check if a list contains ANY elements of another list

if any(item in list_2 for item in list_1):
    # 👇️ this runs
    print('list_2 contains at least 1 item present in list_1')
else:
    print('list_2 does NOT contain any of the items in list_1')

list_3 = ['apple', 'banana', 'kiwi']
list_4 = ['apple', 'banana', 'kiwi']