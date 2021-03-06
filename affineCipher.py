# Affine Cipher
# http://inventwithpython.com/codebreaker (BSD Licensed)

import sys, pyperclip, cryptomath

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    myMessage = 'A computer would deserve to be called intelligent if it could deceive a human into believing that it was human. -Alan Turing'
    myKeyA, myKeyB = 5, 7
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

    myMessage = myMessage.upper()

    if myMode == 'encrypt':
        translated = encryptMessage(myKeyA, myKeyB, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKeyA, myKeyB, myMessage)

    print('%sed text:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (myMode))


def encryptMessage(keyA, keyB, message):
    # key strength and validity checks
    if keyA == 1:
        sys.exit('The affine cipher becomes incredibly weak when keyA is set to 1. Choose a different key.')
    if keyB == 0:
        sys.exit('The affine cipher becomes incredibly weak when keyB is set to 0. Choose a different key.')

    if cryptomath.gcd(keyA, len(LETTERS)) != 1:
        sys.exit('The key (%s) and the size of the alphabet (%s) are not relatively prime. Choose a different key.' % (keyA, len(LETTERS)))

    ciphertext = ''
    for symbol in message:
        if symbol in LETTERS:
            # encrypt this symbol
            symIndex = LETTERS.find(symbol)
            ciphertext += LETTERS[(symIndex * keyA + keyB) % len(LETTERS)]
        else:
            # just append this symbol unencrypted
            ciphertext += symbol
    return ciphertext


def decryptMessage(keyA, keyB, message):
    if cryptomath.gcd(keyA, len(LETTERS)) != 1:
        sys.exit('The key (%s) and the size of the alphabet (%s) are not relatively prime. Choose a different key.' % (keyA, len(LETTERS)))

    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(LETTERS))

    for symbol in message:
        if symbol in LETTERS:
            # decrypt this symbol
            symIndex = LETTERS.find(symbol)
            plaintext += LETTERS[(symIndex - keyB) * modInverseOfKeyA % len(LETTERS)]
        else:
            # just append this symbol unencrypted
            plaintext += symbol
    return plaintext


# If affineCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()