def karaca_encrypt(msg):
    msg = msg[::-1]
    vowel = ['a', 'e', 'i', 'o', 'u']
    replacement = ['0', '1', '2', '3', '4']
    for i in range(5):
        msg = msg.replace(vowel[i],replacement[i])
    msg += 'aca'
    return msg

def karaca_decrypt(msg):
    msg = msg[0:-3]
    replacement = ['0', '1', '2', '3', '4']
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in range(5):
        msg = msg.replace(replacement[i],vowel[i])
    msg = msg[::-1]
    return msg

if input('Encrypt(E) or Decrypt(D)?: ') == 'E':
    plain = input('Enter the message to be encrypted: ')
    print(karaca_encrypt(plain))
else:
    cipher = input('Enter the message to be decrypted: ')
    print(karaca_decrypt(cipher))

