import os

BLOCK_SIZE = 16

# S-box
SBOX = [
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
]

# Inverzní S-box
INV_SBOX = [
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
]

# Rcon – konstanty pro KeyExpansion
RCON = [
    0x00,  # dummy prvek, nevyužívá se
    0x01, 0x02, 0x04, 0x08,
    0x10, 0x20, 0x40, 0x80,
    0x1b, 0x36, 0x6c, 0xd8,
    0xab, 0x4d, 0x9a
]


# SubBytes – substituce každého bajtu přes SBOX
def sub_bytes(state: list[list[int]]) -> list[list[int]]:
    for i in range(4):
        for j in range(4):
            state[i][j] = SBOX[state[i][j]]
    return state


# Inverzní SubBytes – substituce přes INV_SBOX
def inv_sub_bytes(state: list[list[int]]) -> list[list[int]]:
    for i in range(4):
        for j in range(4):
            state[i][j] = INV_SBOX[state[i][j]]
    return state


# ShiftRows – cyklický posun řádků matice doleva o jejich index
def shift_rows(state: list[list[int]]) -> list[list[int]]:
    rows = [[state[col][row] for col in range(4)] for row in range(4)]
    for i in range(1, 4):
        rows[i] = rows[i][i:] + rows[i][:i]
    for row in range(4):
        for col in range(4):
            state[col][row] = rows[row][col]
    return state


# Inverzní ShiftRows – posun řádků doprava
def inv_shift_rows(state: list[list[int]]) -> list[list[int]]:
    rows = [[state[col][row] for col in range(4)] for row in range(4)]
    for i in range(1, 4):
        rows[i] = rows[i][-i:] + rows[i][:-i]
    for row in range(4):
        for col in range(4):
            state[col][row] = rows[row][col]
    return state


# Násobení v GF(2^8)
def xtime(a):
    return ((a << 1) ^ 0x1B) & 0xFF if (a & 0x80) else (a << 1)


# MixColumns – lineární transformace každého sloupce v GF(2^8)
def mix_columns(state: list[list[int]]) -> list[list[int]]:
    for col in range(4):
        a = state[col]
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        u = a[0]
        state[col][0] ^= t ^ xtime(a[0] ^ a[1])
        state[col][1] ^= t ^ xtime(a[1] ^ a[2])
        state[col][2] ^= t ^ xtime(a[2] ^ a[3])
        state[col][3] ^= t ^ xtime(a[3] ^ u)
    return state


# Inverzní MixColumns
def inv_mix_columns(state: list[list[int]]) -> list[list[int]]:
    for col in range(4):
        a = state[col]
        u = xtime(xtime(a[0] ^ a[2]))
        v = xtime(xtime(a[1] ^ a[3]))
        a[0] ^= u
        a[1] ^= v
        a[2] ^= u
        a[3] ^= v
    return mix_columns(state)


# AddRoundKey – XOR stavu s rundovým klíčem
def add_round_key(state: list[list[int]], round_key: list[int]) -> list[list[int]]:
    for col in range(4):
        for row in range(4):
            state[col][row] ^= round_key[col * 4 + row]
    return state


# Načte od uživatele délku klíče (128/192/256 bitů), vrátí počet bajtů
def get_key_length():
    while True:
        print("\nVyberte velikost klíče:")
        print("1. 128 bitů")
        print("2. 192 bitů")
        print("3. 256 bitů")
        volba = input("Zadejte volbu (1-3): ")
        if volba == "1":
            return 16
        elif volba == "2":
            return 24
        elif volba == "3":
            return 32
        else:
            print("Neplatná volba. Zadejte 1, 2 nebo 3.")


# Převede uživatelský klíč na bajty přesné délky (zkrátí nebo doplní opakováním)
def process_key(user_key: str, length: int) -> bytes:
    key_bytes = user_key.encode('utf-8')
    if len(key_bytes) > length:
        return key_bytes[:length]
    while len(key_bytes) < length:
        key_bytes += key_bytes[:length - len(key_bytes)]
    return key_bytes


# Převod 16 bajtů na matici 4x4
def bytes_to_matrix(block: bytes) -> list[list[int]]:
    return [list(block[i::4]) for i in range(4)]


# Převod matice 4x4 zpět na bajty
def matrix_to_bytes(matrix: list[list[int]]) -> bytes:
    return bytes(sum(zip(*matrix), ()))


# Zašifruje jeden 16bajtový blok pomocí key_schedule
def encrypt_block(block, key_schedule, number_of_rounds):
    state = bytes_to_matrix(block)
    state = add_round_key(state, key_schedule[:16])
    for r in range(1, number_of_rounds):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key_schedule[16 * r:16 * (r + 1)])
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_schedule[16 * number_of_rounds:16 * (number_of_rounds + 1)])
    return matrix_to_bytes(state)


# Dešifruje jeden 16bajtový blok pomocí key_schedule
def decrypt_block(block, key_schedule, number_of_rounds):
    state = bytes_to_matrix(block)
    state = add_round_key(state, key_schedule[16 * number_of_rounds:16 * (number_of_rounds + 1)])
    for r in range(number_of_rounds - 1, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, key_schedule[16 * r:16 * (r + 1)])
        state = inv_mix_columns(state)
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, key_schedule[:16])
    return matrix_to_bytes(state)


# PKCS7 padding na násobek BLOCK_SIZE
def pad(plaintext: bytes) -> bytes:
    padding_len = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE
    return plaintext + bytes([padding_len] * padding_len)


# Odstranění PKCS7 paddingu
def unpad(plaintext: bytes) -> bytes:
    padding_len = plaintext[-1]
    return plaintext[:-padding_len]


# AES šifrování – paddinguje data a šifruje po blocích
def aes_encrypt(data, key):
    key_schedule = key_expansion(key)
    number_of_rounds = {16: 10, 24: 12, 32: 14}[len(key)]
    data = pad(data)
    encrypted = []
    for i in range(0, len(data), BLOCK_SIZE):
        block = list(data[i:i + BLOCK_SIZE])
        encrypted.extend(encrypt_block(block, key_schedule, number_of_rounds))
    return bytes(encrypted)


# AES dešifrování – dešifruje po blocích a odstraní padding
def aes_decrypt(data, key):
    key_schedule = key_expansion(key)
    number_of_rounds = {16: 10, 24: 12, 32: 14}[len(key)]
    decrypted = []
    for i in range(0, len(data), BLOCK_SIZE):
        block = list(data[i:i + BLOCK_SIZE])
        decrypted.extend(decrypt_block(block, key_schedule, number_of_rounds))
    return unpad(bytes(decrypted))


# Generuje rozšířený klíč (key schedule) pro AES-128/192/256
def key_expansion(key: bytes) -> list[int]:
    key_length_to_number_of_rounds = {16: 10, 24: 12, 32: 14}

    def rot_word(word: int) -> int:
        return ((word << 8) & 0xFFFFFFFF) | (word >> 24)

    def sub_word(word: int) -> int:
        return (
                (SBOX[(word >> 24) & 0xFF] << 24) |
                (SBOX[(word >> 16) & 0xFF] << 16) |
                (SBOX[(word >> 8) & 0xFF] << 8) |
                SBOX[word & 0xFF]
        )

    key_symbols = list(key)
    key_length = len(key_symbols)

    assert key_length in key_length_to_number_of_rounds.keys(), "Invalid key length"

    words_in_key = key_length // 4
    number_of_rounds = key_length_to_number_of_rounds[key_length]
    words_in_block = 4

    w = [0] * (words_in_block * (number_of_rounds + 1))

    for i in range(words_in_key):
        w[i] = (key_symbols[4 * i] << 24) | (key_symbols[4 * i + 1] << 16) | (key_symbols[4 * i + 2] << 8) | \
               key_symbols[4 * i + 3]

    for i in range(words_in_key, words_in_block * (number_of_rounds + 1)):
        temp = w[i - 1]
        if i % words_in_key == 0:
            temp = sub_word(rot_word(temp)) ^ RCON[i // words_in_key]
        elif words_in_key > 6 and i % words_in_key == 4:
            temp = sub_word(temp)
        w[i] = w[i - words_in_key] ^ temp

    key_schedule = []
    for word in w:
        key_schedule.extend([
            (word >> 24) & 0xFF,
            (word >> 16) & 0xFF,
            (word >> 8) & 0xFF,
            word & 0xFF
        ])

    return key_schedule


# Zašifruje soubor a výsledek vypíše jako hex, případně uloží do souboru
def encrypt_file(input_file: str, key: bytes):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        encrypted = aes_encrypt(data, key)

        hex_output = encrypted.hex()
        print("Zašifrovaný obsah (hex):")
        print(hex_output)

        save = input("Chcete výsledek uložit do souboru? (a/n): ").lower()
        if save == 'a':
            output_file = input("Zadejte název výstupního souboru: ")
            if not os.path.splitext(output_file)[1]:
                output_file += ".txt"
            with open(output_file, 'w') as f:
                f.write(hex_output)
            print(f"Výstup uložen do {output_file}")
    except FileNotFoundError:
        print("Soubor nebyl nalezen!")
    except Exception as e:
        print("Chyba při šifrování souboru:", e)


# Dešifruje soubor (hex nebo binární AES výstup) a případně uloží výsledek
def decrypt_file(input_file: str, key: bytes):
    try:
        with open(input_file, 'rb') as f:
            hex_data = f.read()
        try:
            try:
                hex_data = bytes.fromhex(hex_data.decode('utf-8'))
            except UnicodeDecodeError:
                hex_data = hex_data
        except Exception:
            print("Chyba při čtení šifrovaného vstupu!")
            return

        decrypted = aes_decrypt(hex_data, key)

        text_output = decrypted.decode('utf-8')
        print("Dešifrovaný obsah:")
        print(text_output)

        save = input("Chcete výsledek uložit do souboru? (a/n): ").lower()
        if save == 'a':
            output_file = input("Zadejte název výstupního souboru: ")
            if not os.path.splitext(output_file)[1]:
                output_file += ".txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text_output)
            print(f"Výstup uložen do {output_file}")
    except FileNotFoundError:
        print("Soubor nebyl nalezen!")
    except Exception as e:
        print("Chyba při dešifrování souboru:", e)


# Zašifruje text zadaný z konzole a výsledek vypíše jako hex
def encrypt_console(text: str, key: bytes):
    encrypted = aes_encrypt(text.encode('utf-8'), key)

    hex_output = encrypted.hex()
    print("Zašifrovaný text (hex):")
    print(hex_output)

    save = input("Chcete výsledek uložit do souboru? (a/n): ").lower()
    if save == 'a':
        output_file = input("Zadejte název výstupního souboru: ")
        if not os.path.splitext(output_file)[1]:
            output_file += ".txt"
        with open(output_file, 'w') as f:
            f.write(hex_output)
        print(f"Výstup uložen do {output_file}")


# Dešifruje hex data zadaná z konzole a výsledek zobrazí
def decrypt_console(encrypted_data: bytes, key: bytes):
    try:
        decrypted = aes_decrypt(encrypted_data, key)
        text_output = decrypted.decode('utf-8')
        print("Dešifrovaný text:")
        print(text_output)

        save = input("Chcete výsledek uložit do souboru? (a/n): ").lower()
        if save == 'a':
            output_file = input("Zadejte název výstupního souboru: ")
            if not os.path.splitext(output_file)[1]:
                output_file += ".txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text_output)
            print(f"Výstup uložen do {output_file}")
    except Exception as e:
        print("Chyba při dekódování/dešifrování:", e)


def main():
    while True:
        print("\n=== AES Šifrovací Aplikace ===")
        print("1. Šifrovat soubor")
        print("2. Dešifrovat soubor")
        print("3. Šifrovat text z konzole")
        print("4. Dešifrovat text z konzole")
        print("5. Konec")

        volba = input("\nVyberte možnost (1-5): ")

        if volba == "5":
            print("Program ukončen.")
            break

        if volba not in ["1", "2", "3", "4"]:
            print("Neplatná volba. Zadejte 1, 2, 3, 4 nebo 5.")
            continue

        key_length = get_key_length()
        user_input_key = input("Zadejte svůj klíč (libovolná délka): ")
        key = process_key(user_input_key, key_length)

        print(f"\nPoužitý klíč ({key_length * 8} bitů): {key}, {key.hex()}")

        if volba == "1":
            input_file = input("\nZadejte název vstupního souboru nebo celou cestu: ")
            encrypt_file(input_file, key)
        elif volba == "2":
            input_file = input("\nZadejte název zašifrovaného souboru nebo celou cestu: ")
            decrypt_file(input_file, key)
        elif volba == "3":
            text = input("\nZadejte text pro šifrování: ")
            encrypt_console(text, key)
        elif volba == "4":

            encrypted_hex = input("Zadejte zašifrovaný text (v hex formátu): ")
            try:
                encrypted_data = bytes.fromhex(encrypted_hex)
                decrypt_console(encrypted_data, key)
            except ValueError:
                print("Neplatný hex řetězec!")

        else:
            print("Neplatná volba!")


if __name__ == "__main__":
    main()
