# Caesar_Cipher

Caesar Cipher is one of the earliest encryption techniques known to humankind. It was used by Julius Caesar to talk to his loyal members without others understanding the message.

Look at the following example:

o FRUIT; Shift 2 -> HTWKV

Here, every letter is replaced with an alphabet that comes to two places after the original one.

Script commands:

To Encrypt a Message use 'encrypt' as an argument in your command:

python caesar cipher.py encrypt

To Decrypt a Message use 'decrypt'as an argument in your command:

python caesar cipher.py decrypt

To see more about the script use --help or -h:

python caesar cipher.py --help

output:

usage: Caesar Cipher.py [-h] crypt

Caeser Cipher is a method of Encrypt or Decrypt a message

positional arguments:
  crypt       Give 'encrypt' if you want to encrypt a message or Give 'decrypt' if you want to decrypt a message

optional arguments:
  -h, --help  show this help message and exit
