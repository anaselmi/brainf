#January 23, 2018
#Brainfuck interpreter
from memory import memory
from linter import linter
from time import sleep

print("BRAINFUCK INTERPRETER:\nBy Anas Elmi ")
sleep(1.8)
print("Welcome to the Brainfuck Interpreter. Enter your Brainfuck code below, and it'll run in Python!")
sleep(1.8)
code  = input("Enter code here: " )
valid_code = linter(code)
mem_env = memory()
print(mem_env)

index = 0
while True:
    try:
        char = valid_code[index]
    
    #This runs at the end of our loop, printing the status of our tape and exitng the program
    except:
        print(mem_env)
        break

    if char == "+":
        mem_env.increase_cell()
        index += 1
        continue
    if char == "-":
        mem_env.decrease_cell()
        index += 1
        continue
    if char == ">":
        mem_env.increase_pointer()
        index += 1
        continue
    if char == "<":
        mem_env.decrease_pointer()
        index += 1
        continue
    if char == ",":
        try:
            cell_input = ord(input("What character would you like to input?"))
        except:
            while True:
                try:
                    cell_input = ord(input("Please input one character only."))
                except:
                    continue
                break
        mem_env.input_number(cell_input)
        index += 1
        continue
    if char == ".":
        print(chr(mem_env.current_value()))
        index += 1
        continue
    #This means that the character was "]"
    if type(char) == int:
        print("I ran!")
        if mem_env.current_value() == 0:
            index += 1
            continue
        else:
            index = char
            continue
    if char == "[":
        if mem_env.current_value() == 0:
            index = valid_code.index(index) + 1
            continue
        else:
            index += 1
            continue


