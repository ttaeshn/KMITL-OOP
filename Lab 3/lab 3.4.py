def char_count(str):
    return {char: str.count(char) for char in str}

print(char_count('language'))