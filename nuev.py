def sNum():
    sNum = 0
    while sNum == 0:
        try:
            sNum = int(input())
            while sNum <= 0 or sNum >= 101:
                sNum = int(input())
        except ValueError:
            sNum = 0
    return sNum


def aStudents(nStudents, aSize):
    for index in range(0, aSize):
        print(nStudents[index])


def main():
    aSize = sNum()
    tSCore = [0] * aSize
    sName = [' '] * aSize

    for index in range(aSize):
        sName[index] = input("ENter name ")
        tSCore[index] = float(input())
    eFile = input("Enter a file")

    def cTotal():
        outfile = open(eFile, 'w')
        tSum = sum(tSCore);
        print("Total socre = ", tSum);
        outfile.write("Total score= ");
        return tSum

    cTotal()

    def aScore():
        tSUm = cTotal()
