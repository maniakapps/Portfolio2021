"""
    Fixed Length Records

        You will be passed the filename P, firstname F, lastname L, and a new birthday B.

        Load the fixed length record file in P, search for F,L in the first and change birthday to B.

        Then save the file.
"""
P = ""
F = ""
L = ""
B = ""

file = open(P, 'r+')
data = file.read()
file.close()
fileRecord = []
while len(data) > 0:
    record = [data[0:16], data[16:32], data[32:40]]
    fileRecord.append(record)
    data = data[40:]

output = ""
for i in range(len(fileRecord)):
    currentRecord = fileRecord[i]
    if currentRecord[0].strip() == "F" and currentRecord[1].strip() == "L":
        currentRecord[2] = B
    output += currentRecord[0] + currentRecord[1] + currentRecord[2]

print(output)
