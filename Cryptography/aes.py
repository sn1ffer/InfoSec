import io

rcon = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36)

sBox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
)

decrypt_sBox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
)

# x^8 + x^4 + x^3 + x + 1
stablePolynom = 0x11b


def galoisMultiply(a, b):
    result = 0
    for i in range(8):
        if b & 1:
            result = result ^ a
        a <<= 1
        if a & 0x100:
            a = a ^ stablePolynom
        b >>= 1
    return result


def readFromFile(name):
    f = io.open(name, 'rb')
    arr = f.read()
    f.close()
    return arr


def putToFile(name, message):
    f = io.open(name, "wb")
    tmp = []
    for i, arr in enumerate(message):
        for j, val in enumerate(arr):
            tmp.append(val)
    toWrite = bytearray(tmp)
    f.write(toWrite)
    f.close()


def addRoundKey(block, key):
    for i, value in enumerate(key):
        for j, number in enumerate(value):
            block[i][j] ^= number

    return block


def subBytes(block):
    for i, val in enumerate(block):
        for j, num in enumerate(val):
            block[i][j] = sBox[num]
    return block


def decrypt_subBytes(block):
    for i, val in enumerate(block):
        for j, num in enumerate(val):
            block[i][j] = decrypt_sBox[num]
    return block


def subBytesLine(block):
    for i, val in enumerate(block):
        block[i] = sBox[val]
    return block


def shiftRows(block):
    for k in range(4):
        block[k] = block[k][k:] + block[k][:k]

    return block


def decrypt_shiftRows(block):
    for k in range(4):
        block[k] = block[k][4 - k:] + block[k][:4 - k]

    return block


def mixColumns(block):
    for i in range(4):
        a = block[0][i]
        b = block[1][i]
        c = block[2][i]
        d = block[3][i]

        block[0][i] = galoisMultiply(a, 2) ^ galoisMultiply(b, 3) ^ c ^ d
        block[1][i] = a ^ galoisMultiply(b, 2) ^ galoisMultiply(c, 3) ^ d
        block[2][i] = a ^ b ^ galoisMultiply(c, 2) ^ galoisMultiply(d, 3)
        block[3][i] = galoisMultiply(a, 3) ^ b ^ c ^ galoisMultiply(d, 2)

    return block


def decrypt_mixColumns(block):
    for i in range(4):
        a = block[0][i]
        b = block[1][i]
        c = block[2][i]
        d = block[3][i]

        block[0][i] = galoisMultiply(a, 0x0e) ^ galoisMultiply(b, 0x0b) ^ galoisMultiply(c, 0x0d) ^ galoisMultiply(d,
                                                                                                                   0x09)
        block[1][i] = galoisMultiply(a, 0x09) ^ galoisMultiply(b, 0x0e) ^ galoisMultiply(c, 0x0b) ^ galoisMultiply(d,
                                                                                                                   0x0d)
        block[2][i] = galoisMultiply(a, 0x0d) ^ galoisMultiply(b, 0x09) ^ galoisMultiply(c, 0x0e) ^ galoisMultiply(d,
                                                                                                                   0x0b)
        block[3][i] = galoisMultiply(a, 0x0b) ^ galoisMultiply(b, 0x0d) ^ galoisMultiply(c, 0x09) ^ galoisMultiply(d,
                                                                                                                   0x0e)

    return block


def keyExpansion(key):
    longKey = key

    for i in range(11):

        if i == 0:
            continue

        for k in range(4):

            if k == 0:
                vertWord = [key[0][i * 4 - 1], key[1][i * 4 - 1], key[2][i * 4 - 1], key[3][i * 4 - 1]]
                tmp = subBytesLine(vertWord[1:] + vertWord[:1])
                tmp[0] ^= rcon[i - 1]
                for vert in range(4):
                    valToPush = tmp[vert] ^ longKey[vert][i * 4 + k - 4]
                    longKey[vert].append(valToPush)

            else:
                for vert in range(4):
                    valToPush = longKey[vert][i * 4 + k - 1] ^ longKey[vert][i * 4 + k - 4]
                    longKey[vert].append(valToPush)

    return longKey


def newArr(key, i):
    toReturn = []
    for pos in range(4):
        toReturn.append(key[pos][4 * i:4 * (i + 1)])
    return toReturn


def encryptBlock(block, key):
    key = keyExpansion(key)

    block = addRoundKey(block, newArr(key, 0))

    for i in range(9):
        block = subBytes(block)
        block = shiftRows(block)
        block = mixColumns(block)
        block = addRoundKey(block, newArr(key, i + 1))

    block = subBytes(block)
    block = shiftRows(block)
    block = addRoundKey(block, newArr(key, 10))

    return block


def decrypt_block(block, key):
    key = keyExpansion(key)

    block = addRoundKey(block, newArr(key, 10))

    for i in range(8, -1, -1):
        block = decrypt_shiftRows(block)
        block = decrypt_subBytes(block)
        block = addRoundKey(block, newArr(key, i + 1))
        block = decrypt_mixColumns(block)

    block = decrypt_shiftRows(block)
    block = decrypt_subBytes(block)
    block = addRoundKey(block, newArr(key, 0))

    return block


def encryptAes(file, key):
    encryptedMsg = []
    tempBlock = []
    i = 0

    headZeroes = abs(len(file) % 16 - 16) % 16
    for q in range(headZeroes):
        if q % 4 == 0:
            tempBlock.append([0])
        else:
            tempBlock[q // 4].append(0)
        i += 1

    for elem in file:

        if i % 4 == 0:
            tempBlock.append([elem])
        else:
            tempBlock[(i % 16) // 4].append(elem)

        i += 1

        if i % 16 == 0:
            encryptedMsg += encryptBlock(tempBlock, key)
            tempBlock = []

    return encryptedMsg


def decryptAes(encoded, key):
    decryptedMsg = []
    tempBlock = []
    i = 0

    for elem in encoded:

        if i % 4 == 0:
            tempBlock.append([elem])
        else:
            tempBlock[(i % 16) // 4].append(elem)

        i += 1

        if i % 16 == 0:
            decryptedMsg += decrypt_block(tempBlock, key)

            flag = False

            if i == 16:
                for k, arr in enumerate(decryptedMsg):
                    if flag:
                        break
                    modifier = 0
                    for j in range(4):
                        if arr[j + modifier] == 0:
                            arr.remove(0)
                            modifier -= 1
                        else:
                            flag = True
                            break

            tempBlock = []

    return decryptedMsg


def getKeyFromConsole():
    keyToReturn = []

    arrIn = list(map(int, input().split()))

    for q in range(4):
        for j in range(4):
            gotNum = arrIn[q * 4 + j]
            if j == 0:
                keyToReturn.append([gotNum % 256])
            else:
                keyToReturn[q].append(gotNum % 256)

    return keyToReturn


if __name__ == '__main__':

    print("Выберите вариант выполнения:\n 1 - Зашифрование\n 0 - Расшифрование")
    mode = input()
    while mode != "1" and mode != "0":
        print("Неверный ввод, повторите попытку:")
        mode = input()

    print("Введите название файла:")
    nameOfInput = input()
    print(
        "Введите 16 чисел в одну строку (от 0 до 255) для ключа:\n(при введении большего берётся остаток от деления на 256)")
    keyToRealize = getKeyFromConsole()
    print("Введите имя итогового файла")
    nameOfOutput = input()

    if mode == "1":

        msg = encryptAes(readFromFile(nameOfInput), keyToRealize)

        putToFile(nameOfOutput, msg)

    elif mode == "0":

        reverse = decryptAes(readFromFile(nameOfInput), keyToRealize)

        putToFile(nameOfOutput, reverse)

    print("Программа выполнена")