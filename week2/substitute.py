import random
from assingment2 import alphabet_lists


# giving the string
cipher_string = input("Gimme a string: ")
abc_lower = alphabet_lists(just_lower=True)
abc_shuff = alphabet_lists(just_lower=True)

# easy way to add punctuations, whitespaces and also numbers
# can also add special chars like å, ø, ö, ä, etc
def split_string(string):
    """just splits a string on all characters"""
    return [char for char in string]


added_ch_string = (
    " ,.!:;'?+-/()0123456789øæåöä"  # characters we want to add to the ciphering
)
added_ch_list = split_string(added_ch_string)
abc_lower += added_ch_list
abc_shuff += added_ch_list


# selecting encrypt or decrypt
while True:  # while-loop to check if input is 'e' or 'd'
    selected = input("Encrypt (E) or decrypt (D) this string: ")
    try:
        if selected.lower() == "e" or selected.lower() == "d":
            break
    except:
        print("Your choice must be E or D.")

# selecting the seed
while True:  # while-loop to check if input is an integer
    try:
        seed = int(input("Select seed (any integer): "))
        random.seed(seed)
        break
    except:
        print("Cipher shift must be an integer!")


print(abc_lower)
(random.shuffle(abc_shuff))
print(abc_shuff)


if selected.lower() == "d":
    decrypted_list = []
    for ch in cipher_string:
        if ch in abc_lower:
            decrypted_list.append(abc_lower[abc_shuff.index(ch)])
        else:
            decrypted_list.append(ch)
    print(f'Decrypted string: {"".join(decrypted_list)}')


elif selected.lower() == "e":
    print("enc")
    encrypted_list = []
    for ch in cipher_string:
        if ch in abc_lower:
            encrypted_list.append(abc_shuff[abc_lower.index(ch)])
        else:
            encrypted_list.append(ch)
    print(f'Encrypted string: {"".join(encrypted_list)}')
