def  myFunc():
    print("Hello World")
    
    
# myFunc()
# print(__name__)  # Prints the string '__main__' as it get
                   # executed on the same file where it is created i.e. module

if __name__ == "__main__":
    # if this code gets executed by running the file it's present in
    print("We are directly running this code")
    myFunc()
    print(__name__)
    