import string

word = "Hello World"
cipher_word = ""
shift = 2

for char in word:
	if char == ' ':
		cipher_word += char
	elif char.isupper():
		cipher_word += chr((ord(char)+shift-65)%26+65)
	else:
		cipher_word += chr((ord(char)+shift-97)%26+97)

# def caesar(text, shift, alphabets):
# 	def shift_alpha(alphabet):
# 		return alphabet[shift:] + alphabet[:shift]

# 	shifted_alphas = tuple(map(shift_alpha, alphabets))
# 	final_alphabet = ''.join(alphabets)
# 	final_shifted_alpha = ''.join(shifted_alphas)
# 	table = str.maketrans(final_alphabet,final_shifted_alpha)
# 	print(alphabets)
# 	print(shifted_alphas)
# 	print(final_alphabet)
# 	print(final_shifted_alpha)
# 	print(table)
# 	return text.translate(table)

# shifted = 2
# # shifted = 26-2
# # shifted %= 26

# print(caesar(word, shifted, [string.ascii_lowercase, string.ascii_uppercase]))
print(cipher_word)
