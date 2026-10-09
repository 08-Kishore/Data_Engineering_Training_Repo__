file=open("employees.txt","r")

for line in file:
    print(line.strip())
file.close()

file=open("employees.txt","a")
file.write("104,Sara,Sales,68000\n")
file.close()

