from passlib.hash import bcrypt
from termcolor import cprint
from pwn import *
import time

#predefined stuff
valid = []


def crack(valid, wordlist, name):
    for hash_value in valid:
        start = time.time()
        hash_value = hash_value.strip("\n")
        with log.progress(f"Attempting to crack {hash_value}") as p:
            attempts = 0
            with open(wordlist, "r", encoding="latin-1") as passwordlist:   
                for password in passwordlist:   
                    attempts += 1   
                    password = str(password)        
                    encoded_string = password.encode("ascii", "ignore")
                    password = encoded_string.decode()
                    password = password.strip("\n").encode('UTF8')
                    to_func = name + 'sumhex'
                    func = eval(to_func)
                    hashed = func(password)
                    p.status(f"[{attempts}] {password.decode('latin-1')}")
                    if (hashed == hash_value):
                        p.success(f"\nPassword found after {attempts} attempts\n")
                        cprint(f"The password is {password.decode('latin-1')}", 'green')
                        end = time.time()
                        break
            end = time.time()
            print('took '+ (format(end - start, ".2f")) + ' seconds\n')
            p.failure("the specified wordlist does not contain the password, maybe try another wordlist")


def bcry(valid, wordlist, name):
    done = False
    for hash_value in valid:
        start = time.time()
        hash_value = hash_value.strip("\n")
        if hash_value == "":
            continue
        print(f"[+] Attempting to crack {hash_value}")
        password_list = open(wordlist, "r", encoding="latin-1")
        lines = password_list.read().splitlines()
        password_list.close()
        attempts = 0
        for (index, password) in enumerate(lines):
            encoded_string = password.encode("ascii", "ignore")
            password = encoded_string.decode()
            attempts += 1
            print(f"\rtrying {password} ", end='')
            correct = bcrypt.verify(password, hash_value)
            if (correct):
                end = time.time()
                print(f"\nPassword found after {attempts} attempts")
                cprint(f"The password is {password}", 'green')
                print("it took " + format(end - start, ".2f")+ " seconds\n")
                done = True
                break
        if (done == False):
            print("the specified wordlist does not contain the password, maybe try another wordlist")


def passer(valid, wordlist, name):
    if (name == "bcrypt"):
        bcry(valid, wordlist, name)
    else :
        crack(valid, wordlist, name)


def notvalid(line, name):
    line = line.strip("\n")
    print(f'the hash {line} is not a valid {name} hash. proceeding without it')


def checker(the_file, wordlist, name):
    reading = open(the_file, "r")
    lines = reading.readlines()
    reading.close()
    for line in lines:
        if name == "md5":
            if len(line.strip("\n")) == 32:
                valid.append(line)
            elif line.strip("\n") == "":
                continue
            else:
                notvalid(line, name)

        elif name == "sha1":
            if len(line.strip("\n")) == 40:
                valid.append(line)
            elif line.strip("\n") == "":
                continue
            else:
                notvalid(line, name)
    
        elif name == "sha224":
            if len(line.strip("\n")) == 56:
                valid.append(line)
            elif line.strip("\n") == "":
                continue
            else:
                notvalid(line, name)

        elif name == "sha256":
            if len(line.strip("\n")) == 64:
                valid.append(line)
            elif line.strip("\n") == "":
                continue
            else:
                notvalid(line, name)

        elif name == "sha384":
            if len(line.strip("\n")) == 96:
                valid.append(line)
            elif line.strip("\n") == "":
                continue
            else:
                notvalid(line, name)

        elif name == "sha512":
            if len(line.strip("\n")) == 128:
                valid.append(line)
            elif line.strip("\n") == "":
                continue
            else:
                notvalid(line, name)

        elif name == "bcrypt":
            if len(line.strip("\n")) == 60:
                valid.append(line)
            elif line.strip("\n") == "":
                continue
            else:
                notvalid(line, name)
    passer(valid, wordlist, name)

