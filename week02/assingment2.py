# week 2, assignment


# %% cryptography for Roman Emperors
def alphabet_lists(just_lower=False):
    """Helper function which gives two lists with [a, b, ..., z],  [A, ..., Z]"""
    # this in unpythonic, but I use it now
    lower_abc = []
    upper_abc = []
    for abc in range(26):
        lower_abc.append(chr(abc + ord("a")))
        upper_abc.append(chr(abc + ord("A")))
    # if other characters shall be ciphered, append them (å, ö, æ ...)
    if just_lower:
        return lower_abc
    else:
        return lower_abc, upper_abc


#%%


def cipher_lvl1(string, shift):
    """the first ceasar cipher, which just shifts the input"""
    cipher_list = []  # initialize cipher string-list
    lower_abc, upper_abc = alphabet_lists()
    if shift > len(lower_abc):  # checks if the shift is greater than the character list
        shift = shift % len(lower_abc)

    for ch in string:  # loop through the string

        if ch in upper_abc:  # check if ch is in A-Z
            ch_shift = upper_abc.index(ch) + shift
            if len(upper_abc) <= ch_shift:  # if the shift is too large, restart
                ch_shift = ch_shift - len(upper_abc)
            elif ch_shift < 0:  # if the shift is negative, go from the end of the list
                ch_shift = len(upper_abc) + ch_shift
            cipher_list.append(upper_abc[ch_shift])  # append the shifted char
        # some ugly copy-paste here
        elif ch in lower_abc:  # check if ch is in a-z
            ch_shift = lower_abc.index(ch) + shift
            if len(lower_abc) <= ch_shift:
                ch_shift = ch_shift - len(lower_abc)
            elif ch_shift < 0:
                ch_shift = len(lower_abc) + ch_shift
            cipher_list.append(lower_abc[ch_shift])

        else:  # if the ch is not in A-Z or a-z
            cipher_list.append(ch)
    return "".join(cipher_list)  # join the list of the ciphered characters


# %%


def cipher_script():
    """Script which encrypts or decrypts a message"""
    print(
        "Welcome to the encrypter and decrypter. For decryption, use Cipher shift *(-1)."
    )
    input_string = input("String to be ciphered: ")
    while True:  # while-loop to check if input is an integer
        try:
            cipher_shift = int(input("Cipher shift (integer):"))
            break
        except:
            print("Cipher shift must be an integer!")
    ciphered_string = cipher_lvl1(input_string, cipher_shift)
    print(f"Ciphered string: {ciphered_string}")


def decipher_unknown_shift_with_human():
    """First decipher of unknown shift, with a loop"""
    input_string = input("Ciphered string to be decrypted: ")
    decrypt_shift = 0
    while True:
        for i in range(5):
            decrypt_shift += 1
            decrypted_string = cipher_lvl1(input_string, decrypt_shift)
            print(f"Decryption (key = {decrypt_shift}): {decrypted_string}")
        human_decision = input(f"Try five more? (y/n)")
        if human_decision == "y":
            continue
        elif human_decision == "n":
            print("script ended")
            break
        else:
            print("Uncorrect input, please use y or n.")
            continue


#%%
def decipher_automated():
    """Automated decipher"""
    input_string = input("Ciphered string to be decrypted: ")
    input_searchwords = input("Seachwords, seperated by ' '")
    searchwords = input_searchwords.split(" ")
    decrypt_shift = 0
    search_again = True
    while search_again:
        decrypt_shift += 1
        decrypted_string = cipher_lvl1(input_string, decrypt_shift)
        print(decrypted_string)
        for word in searchwords:
            if word in decrypted_string.lower():
                print(
                    f"Match found! Shift = {decrypt_shift}\nDecryptet message: {decrypted_string}"
                )
                search_again = False  # break while loop
                break  # break for-loop
        if decrypt_shift == 50:
            print("no match found, search terminated")
            break


# decipher_automated()
# decipher_unknown_shift_with_human()
# cipher_script()

# Excercise A output:
# String to be ciphered: >? Pbatenghyngvbaf, lbh unir fhpprrqrq va qrpelcgvat gur fgevat.
# Cipher shift (integer):>? -13
# Ciphered string: Congratulations, you have succeeded in decrypting the string.
