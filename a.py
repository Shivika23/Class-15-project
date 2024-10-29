with open('Sample_File.txt', 'r') as file:
    print(file.read())
    file.close()

with open('Sample_File.txt', 'r') as file:
    print(file.read(10))
    file.close()

with open('Sample_File.txt', 'r') as file:
    print(file.readline())
    file.close()

with open('Sample_File.txt', 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    file.close()

with open('Sample_File.txt', 'r') as file:
    for line in file:
        print(line)
    file.close()
