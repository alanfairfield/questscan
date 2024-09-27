#load the first file, and print the contents of 'nothing' starting at  
with open('90052.txt') as file1:
     file1.readlines()
#nothing = int( ''.join(filter(str.isdigit, file.readlines()))) #Store 'nothing' as variable

#loop to navigate to 400 "nothings"
nothing = file1.readlines() #Store 'nothing' as variable

#n = 1 # increment value
#for i in range (0, 100000, n):
#    i += 1 #add 1 to i per loop iteration
#    print(f'Unpacked File ~ #{i}: {nothing}')
#    nothing = int( ''.join(filter(str.isdigit)))
