# Opening the file & checking if the file exists
try:
    file = open("sample.txt", "r")
    data = file.read()
    
# Throws exception if the file doesn't exist
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
