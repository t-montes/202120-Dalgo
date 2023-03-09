from random import randint

#modify following two parameters
path = "./numbers10.txt"
numofnums = 10

min,max = 1000,9999

with open(path,'w+') as file:
    for i in range(numofnums):
        n = randint(min,max)
        file.write(f"{n}\n")
