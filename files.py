#/bin/python3
import os

GetOut = 50
name = input("Name of file:")

#Functions
def create(name):
	print("Creating....")
	f = open("./files/"+name+".txt", "a")
	f.close()

def add(name, text):
	print("Writing....")
	f = open("./files/"+name+".txt", "w")
	f.write(text)
	f.close()

def read(name):
	print("Reading....")
	f = open("./files/"+name+".txt", "r")
	print(f.read())

def remove(name):
	print("Removing....")
	os.remove("./files/"+name+".txt")

#Menu
while GetOut != 0:
	choose = int(input("0-Exit 1-Create 2-Add 3-Read 4-Remove:"))

	if choose == 0:
		print("Exit")
		GetOut = 0

	elif choose == 1:
		create(name)

	elif choose == 2:
		text = input("write:")
		add(name, text)

	elif choose == 3:
		read(name)

	elif choose == 4:
		remove(name)
