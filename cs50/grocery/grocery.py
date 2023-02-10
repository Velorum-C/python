grocery_list = {}
while True:
    try:
        result = input().upper()
    except EOFError:
        break
    else:
        if result in grocery_list:
            grocery_list[result] += 1
        else:
            grocery_list[result] = 1


for key, value in sorted(grocery_list.items()):
    print(value, " ", key)
