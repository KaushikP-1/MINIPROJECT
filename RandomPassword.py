import string
import random


LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def get_password_length():
	length = input("How long do you want your password: ")
	return int(length)


def password_generator(cbl, length=8):
	# create alphanumerical by fetching string constant
	printable = fetch_string_constant(cbl)

	# convert printable from string to list and shuffle
	printable = list(printable)
	random.shuffle(printable)

	# generate random password
	random_password = random.choices(printable, k=length)

	# convert generated password to string
	random_password = ''.join(random_password)
	return random_password


def password_combination_choice():
	# retrieve a user's password character combination choice
	want_digits = input("Want digits ? (True or False) : ")
	want_letters = input("Want letters ? (True or False): ")
	want_puncts = input("Want punctuation ? (True or False): ")

	# convert those choices from string to it's right boolean type
	try:
		want_digits = eval(want_digits.title())
		want_puncts = eval(want_puncts.title())
		want_letters = eval(want_letters.title())
		return [want_digits, want_letters, want_puncts]

	except NameError as e:
		print("Invalid value. Use either True or False")
		print("Invalidity returns a default, try again to regenerate")

	return [True, True, True]



def fetch_string_constant(choice_list):
	string_constant = ''
	string_constant += NUMBERS if choice_list[0] else ''
	string_constant += LETTERS if choice_list[1] else ''
	string_constant += PUNCTUATION if choice_list[2] else ''

	return string_constant



if __name__ == '__main__':
	length = get_password_length()
	choice_list = password_combination_choice()
	password = password_generator(choice_list, length)

	print(password)
