f = open("midterm2020.txt", "r")
data = f.read().split()

for element in data:
    print(str(element))