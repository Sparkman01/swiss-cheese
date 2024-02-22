import os

filename = input("Please provide a file name to search and display:\n")
subproccess.run(["cat", filename])
command = "cat " + filename
os.system(command)
