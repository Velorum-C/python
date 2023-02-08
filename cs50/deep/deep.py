result = input("What is the answer to Life, the Universe, and Everything? ")
if result.lower() in ["42", "forty-two", "forty two"]:
    print("Yes")
    exit()
print("No")
