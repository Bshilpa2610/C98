def swapfiles():
    fileA = input("Enter your filename1 to swap")
    fileB = input("Enter your filename2 to swap")

    f1=open(fileA)
    f2=open(fileB)

    dataA =f1.read()
    dataB =f2.read()
    print(dataA)
    print(dataB)

    f1=open(fileA,'r+')
    f1.write(str(dataB))

    f2=open(fileB,'r+')
    f2.write(str(dataA))
swapfiles()



