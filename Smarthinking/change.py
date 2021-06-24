with open('file1.txt') as f1:
    file_Data = f1.read()

    file_Data = file_Data.replace("+", "|")

with open('file1.txt', 'w') as file:
    file.write(file_Data)