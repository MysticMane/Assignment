def ext(file):
    a=file.split(".")
    if len(a)>1:
        print("The extension of file is:",a[-1])
    else:
        print("No extension")
#main
file=input("Input the filename:")
ext(file)
