# AES Encryptor

Implementace šifrování AES (Advanced Encryption Standard) v čistém Pythonu bez externích závislostí. Podporuje šifrování a dešifrování souborů i textu zadaného z konzole.

## Funkce

- AES-128, AES-192, AES-256
- Šifrování a dešifrování souborů
- Šifrování a dešifrování textu z konzole
- Výstup v hexadecimálním formátu
- Volitelné uložení výsledku do souboru

## Spuštění

```bash
python AESencryptor.py
```

Po spuštění se zobrazí interaktivní menu:

```
=== AES Šifrovací Aplikace ===
1. Šifrovat soubor
2. Dešifrovat soubor
3. Šifrovat text z konzole
4. Dešifrovat text z konzole
5. Konec
```

## Použití

1. Vyberte operaci (1–4)
2. Zvolte délku klíče (128 / 192 / 256 bitů)
3. Zadejte klíč libovolné délky – program ho automaticky upraví na požadovanou délku
4. Zadejte vstupní soubor nebo text
5. Výsledek se zobrazí v konzoli a volitelně uloží do souboru

## Poznámky

- Šifrovaný výstup je v hex formátu (textový soubor `.txt`)
- Pro dešifrování souboru je nutné zadat stejný klíč a délku klíče jako při šifrování
- Klíč kratší než zvolená délka se doplní opakováním, delší se zkrátí

## Technologie

- Python 3.10+
- Žádné externí závislosti
