# file = open("my_file.txt") # open an existing file in the current folder*
# with open("my_file.txt") as file: # alternative (store in the "file" variable)
#     contents = file.read()
#     print(contents)
#     # you can modify the file here 
#     file.close() # free the ressources on the computer involved to open the file


with open("/home/antokl/proj/100_days_python_bootcamp/100_Days_Python_Bootcamp/day24 - Files and Paths/my_file.txt", mode="w") as file: # r : read / w : write / a : append
    file.write("\nNew text.")
    contents = file.read()
    print(contents)