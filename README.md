# Hexxus
<p align="center">
<img width="560" height="300" src="https://github.com/yanalabuseini/hexxus/blob/main/hexxus.webp">
 </p>
<p align="center">
  <a href="https://github.com/FerasHamam/LegacyWallpapers">
  </a>

 


<p align="center"> <strong>
 Hexxus is a fast hash cracking tool which checks more than 30 thousand passwords in under 4 seconds and can crack the following types
 </strong>
 <ul>
    <li>bcrypt</li>
     <li>NTLM</li>
     <li>sha512</li>
     <li>sha384</li>
     <li>sha256</li>
     <li>sha224</li>
     <li>sha1</li>
     <li>md5</li>
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About Hexxus

<p>Hexxus is the evil spirit of destruction who embodies everything that is toxic to nature. As such, his only goal in existence is to cause destruction, decay and death in any way he can</p>

### Built With

* [python](https://www.python.org/)


### Installation

   ```sh
   cd /opt
   git clone https://github.com/yanalabuseini/hexxus.git
   cd hexxus/
   chmod +x hexxus.py
   cd /usr/bin 
   sudo cp -s /opt/hexxus/hexxus.py ./hexxus
   ```
   
 


<!-- USAGE EXAMPLES -->
## Usage
```sh
👾 ~ $hexxus -h
         _   _ _______  ____  ___   _ ____  
        | | | | ____\ \/ /\ \/ / | | / ___| 
        | |_| |  _|  \  /  \  /| | | \___ \ 
        |  _  | |___ /  \  /  \| |_| |___) |
        |_| |_|_____/_/\_\/_/\_\____/|____/ 
                   
        the hash cracking tool written by _enigma146 
Usage: Usage : python3 hexxus -f <file> -w <wordlist> -n <hash name>

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  the path to the file that contains the hash/es
  -n NAME, --name=NAME  the hash name or type
  -w WORDLIST           the path for the wordlist
```
## Testing Hexxus
the password is in line 200,000 in rockyou
```sh
👾 ~ $hexxus -f hash -n md5 -w /usr/share/wordlists/rockyou.txt 
         _   _ _______  ____  ___   _ ____  
        | | | | ____\ \/ /\ \/ / | | / ___| 
        | |_| |  _|  \  /  \  /| | | \___ \ 
        |  _  | |___ /  \  /  \| |_| |___) |
        |_| |_|_____/_/\_\/_/\_\____/|____/ 
                   
        the hash cracking tool written by _enigma146 
[+]  Attempting to crack 26026774eeaeb53d6e66a53bfbf0a49d: 
    Password found after 200000 attempts
 the password is juelma
took 26.92 seconds
```
## Disclaimer
please note that bcrypt takes more time depending on the way it was built

<!-- CONTACT -->
## Contact

[@_enigma146](https://twitter.com/_enigma146) - yoabuseini@gmail.com

Project Link: [https://github.com/yanalabuseini/hexxus](https://github.com/yanalabuseini/hexxus)


