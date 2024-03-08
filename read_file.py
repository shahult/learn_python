from sys import argv
script, file_name = argv

txt = open(file_name, "+a")
print("Here is the contents of your file >>")
txt.write("Hellooooooooooooooo Guys")
txt.close()

txt = open(file_name)
print("Here are the Updated contents :")
print(txt.read())
txt.close()
