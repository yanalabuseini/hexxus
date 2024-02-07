#!/usr/bin/env python3
import optparse
from helper import checker
from termcolor import cprint


#predefined stuff
file_name = __file__.split('/')[-1]
valid_hashes = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "bcrypt", "ntlm"]


def banner():
    print("\t\t _   _ _______  ____  ___   _ ____  ")
    print("\t\t| | | | ____\\ \\/ /\\ \\/ / | | / ___| ")
    print("\t\t| |_| |  _|  \\  /  \\  /| | | \\___ \\ ")
    print("\t\t|  _  | |___ /  \\  /  \\| |_| |___) |")
    print("\t\t|_| |_|_____/_/\\_\\/_/\\_\\____/|____/ ")
    print("\t\t           ")
    print("\t\tthe hash cracking tool written by ", end=''                    )
    cprint("_enigma146 " , "red")
    print()


def Main():
    banner()
    parser = optparse.OptionParser(f'Usage : python3 {file_name} -f <file> -w <wordlist> -n <hash name>')

    parser.add_option('-f', "--file", dest="file", type="string", help="The path to the file that contains the hash/es")
    parser.add_option('-n', "--name", dest="name", type="string", help="The hash type [available types are: bcrypt, ntlm, md5, sha1, sha224, sha256, sha384, sha512, sha512]")
    parser.add_option('-w', dest="wordlist", help="The path for the wordlist")

    (options, args) = parser.parse_args()

    if (options.name == None or options.file == None or options.wordlist == None):
        print(parser.usage)
        exit()

    the_file = options.file
    wordlist = options.wordlist
    name = options.name

    name = str(name)
    name = name.lower()

    if (name not in valid_hashes):
        print(f'The {name} type is not supported yet...')
        exit()

    checker(the_file, wordlist, name)

if __name__ == '__main__':
    Main()
