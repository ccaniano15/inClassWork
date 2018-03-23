shape = input("triangle or rectangle?")
if shape == "triangle":
	width = int(input("what is the length?"))
	height = int(input("what is the height?"))
	print(width * height / 2)
elif shape == "rectangle":
	width = int(input("what is the length?"))
	height = int(input("what is the height?"))
	print(width * height)
else: 
	print("error")
