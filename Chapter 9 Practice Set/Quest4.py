word = "Donkey"

with open("file2.txt" , "r") as f:
    content = f.read()
    
contentNew = content.replace("Donkey" , "#####") 

with open("file2.txt" , "w") as f:
    f.write(contentNew)
    
