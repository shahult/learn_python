from sys import argv
script, file_name = argv

#### Truncating File

txt = open(file_name, "w")
print(f"We're going to truncate the file {file_name}")
print("Truncating is going to happen now, Please press Ctrl+C or Ctrl+Z if you want to stop it.")
txt.truncate()
txt.close()

#### Inserting Input and write it to the file

prompt = " > "
print("Enter line 1 ")
line1 = input(prompt)
print("Enter line 2 ")
line2 = input(prompt)
print("Enter line 3 ")
line3 = input(prompt)
txt = open(file_name, "+a")

print("Writing these lines to the file")
txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.close()