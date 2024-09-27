#load the first file, and print the contents of 'nothing' starting at  
with open('90052.txt') as file:
     file.readlines()
     for i in file.readlines():
          nothing = int ( ''.join(filter(str.isdigit, nothing) ) ) #Store only the number portion of file contents 'nothing' as variable
          print(nothing)






