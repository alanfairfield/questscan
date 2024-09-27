
#The purpose of this program is to reverse a basic "encryption" applied to a sentence. The rotation essentially "adds" two character-positions to a given character. So, K ->M, O ->Q, E->G, etc.
#the maketrans() method will come into play here

txt = "http://www.pythonchallenge.com/pc/def/map.html"
x = "abcdefghijklmnopqrstuvwxyz"
y = "cdefghijklmnopqrstuvwxyzab"
my_table = str.maketrans(x, y)
print(txt.translate(my_table))