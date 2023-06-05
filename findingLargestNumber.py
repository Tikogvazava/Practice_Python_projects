numbers=[5, 8, 6, 55, 42, 48, 6, 7, 9, 5]
unique=[]

for i in numbers:
    if i not in unique:
        unique.append(i)

print(unique)
