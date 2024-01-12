# Some ANSI escape sequences for colours and effects
#
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

#Use RESET to cancel the effect
#print(RED,"This will be red")
#print("And this as well")  #Continues to print red until we cancel it 


def colour_print(text:str,effect:str):
    output_string = "{0}{1}{2}".format(effect,text,RESET)
    print(output_string)

print(colour_print("Hello World",BLACK))
print(colour_print("Hello World",RED))
print(colour_print("Hello World",GREEN))
print(colour_print("Hello World",YELLOW))
print(colour_print("Hello World",BLUE))
print(colour_print("Hello World",MAGENTA))
print(colour_print("Hello World",CYAN))
print(colour_print("Hello World",WHITE))
print(colour_print("Hello World",BOLD))
print(colour_print("Hello World",UNDERLINE))
print(colour_print("Hello World",REVERSE))
