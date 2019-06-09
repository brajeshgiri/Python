f = open("./files/demofile.txt", "r")
print(f.read())
# print(f.read(5))
f.close()

f = open("./files/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("./files/demofile2.txt", "r")
print(f.read())


f = open("./files/demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("./files/demofile3.txt", "r")
print(f.read())
