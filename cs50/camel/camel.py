camel = list(input("camelCase: "))
result = []
for i in range(0, len(camel)):
    if camel[i].isupper():
        result.append("_")
    result.append(camel[i].lower())

snake = "".join(result)
print(f"snake_case: {snake}")
