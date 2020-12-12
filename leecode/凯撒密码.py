def k(s: str, k: int):
    return ''.join(
        [chr((tr_letter - 65 + k) % 26 + 65) if ((tr_letter := ord(i)) <= 90) else chr((tr_letter - 97 + k) % 26 + 97)
         for i in s])
