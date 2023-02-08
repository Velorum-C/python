result = input("Greeting: ")

if result[0].lower() != "h":
    print("$100")
    exit()

if result.split()[0].lower() != "hello":
    print("$20")
    exit()

print("$0")
