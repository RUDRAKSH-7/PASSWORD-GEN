from random import randint
import colorama
from os import system
from sys import exit


heading = r"""
  - - - -     
  |     |       -        - - - -      - - - -
  |     |     /   \      |            |           
  |- - -     /- - -\     - - - -      - - - - 
  |          |     |           |            |
  |          |     |     - - - -      - - - -              

                  - - - - -     - - - - -    - - - - -
|           |    |         |    |       |    |         \
|           |    |         |    |       |    |          |
|           |    |         |    |- - - -|    |          |
|    /\     |    |         |    |      \     |          |
\ _ /  \ _ /     - - - - -      |       \    |         /
                                              - - - - - 


"""
print("\033c"+colorama.Fore.CYAN+colorama.Style.BRIGHT+heading)

chars = 'abcdefghijklmnopqrstuvwxyz123456789!@#$&'

output_pw = ""

while True:
    try:
        size = int(input(colorama.Fore.WHITE+"\n\nSize of password : "))
        if size > 20:
            raise ValueError
        break
    except ValueError:
        system("cls")
        print(colorama.Fore.CYAN+colorama.Style.BRIGHT+heading)
        print(colorama.Fore.RED+"#RETRY")
while True:
    try:
        print(colorama.Fore.GREEN+"\n\n[1] EASY\t"+colorama.Fore.YELLOW+"[2] MEDIUM\t"+colorama.Fore.RED+"[3] STRONG ! ")
        strength = int(input(colorama.Fore.BLUE+"\nStrength of password : "))
        if strength > 3:
            raise ValueError
        break
    except ValueError:
        system("cls")
        print(colorama.Fore.CYAN+colorama.Style.BRIGHT+heading)
        print(colorama.Fore.RED+"#RETRY")


if strength == 1:
    for i in range(size):
        if i <= size//2:
            output_pw += chars[randint(0,25)]
        else:
            output_pw += chars[randint(26,35)]
if strength == 2:
    for i in range(size):
        random = randint(1,3)
        if random == 1:
            output_pw += chars[randint(0,25)]
        elif random == 2:
            output_pw += chars[randint(26,35)]
        else:
            output_pw += chars[randint(0,25)]
if strength == 3:
    for i in range(size):
        random = randint(1,4)
        if random == 1:
            output_pw += chars[randint(0,25)]
        elif random == 2:
            output_pw += chars[randint(26,35)]
        elif random ==3:
            output_pw += chars[randint(0,25)]
        else:
            output_pw += chars[randint(36,39)]

print(colorama.Fore.WHITE+"\n\nPASSWORD   :    "+colorama.Fore.GREEN+output_pw)
print(colorama.Style.RESET_ALL)
exit()