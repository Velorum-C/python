names = []

while True:
    try:
        current_name = input("Name: ")
        names.append(current_name)
    except EOFError:
        break

print("\nAdieu, adieu to", end=" ")
for name in names[0:-1]:
    print(name, end=", ")

print("and " + names[-1])
