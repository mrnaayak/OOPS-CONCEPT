try:
    fptr=open("C:/Users/Public/venkat.txt","r")
    data=fptr.read()
    print(data)
except IOError:
    print("file does not exist before read")
finally:
    print("file text is read successfully")
