import random

# chars - alphabet + digits + special characters
chars = ["a", "b", "c", "d", "e", "f", "g", "h",
         "i", "j", "k", "l", "m", "n", "o", "p",
         "q", "r", "s", "t", "u", "v", "w", "x",
         "y", "z", "A", "B", "C", "D", "E", "F",
         "G", "H", "I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z", "0", "1", "2", "3",
         "4", "5", "6", "7", "8", "9", "!", "@",
         "#", "$", "%", "^", "&", "*", "(", ")",
         "_", "+", "-", "=", "{", "}", "[", "]",
         "|", ":", ";", "'", "<", ">", ",", ".", ]


# generate random string of length n
def gen_string(n):
    return ''.join(random.choice(chars) for i in range(n))


for i in range(10000):
    print(gen_string(random.randint(8, 12)), file=open("data.txt", "a"))
