import numpy as np

def KeyExpansion(key):

    Nb = 4
    Nk = 4
    Nr = 10


    expandedKeys = np.zeros((Nb * (Nr + 1), ), dtype=np.uint32)
    temp = np.uint32(0)


    for i in range(Nk):
        expandedKeys[i] = key[i]


    for i in range(Nk, Nb * (Nr + 1)):
        temp = expandedKeys[i - 1]

        if i % Nk == 0:
            temp = SubWord(RotateWord(temp))
            temp = temp ^ Rcon[i // Nk]

        expandedKeys[i] = expandedKeys[i - Nk] ^ temp

    return expandedKeys

def SubWord(word):
    new_word = Sbox[word & 0xFF]
    for i in range(1, 4):
        word >>= 8
        new_word = np.append(new_word, Sbox[word & 0xFF])

    return np.uint32(new_word)

def RotateWord(word):
    return np.uint32((word << 8) | (word >> 24))

def AES_Encrypt(plaintext, key):

    expandedKeys = KeyExpansion(key)


    state = AddRoundKey(plaintext, expandedKeys[0])

    for round in range(1, 10):
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, expandedKeys[round])

    state = SubBytes(state)
    state = ShiftRows(state)
    state = AddRoundKey(state, expandedKeys[10])

    return state
