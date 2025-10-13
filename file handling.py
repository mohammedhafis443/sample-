try:
    f=open("example.txt","r")
    contant=f.read()
    print(contant)
except FileNotFoundError:
    print("no such file")

# write to file
f=open("example.txt","a")
f.write("\n new line create")
f.close()

f=open("example.txt","w")
f.write("\n good morning")
f.close()