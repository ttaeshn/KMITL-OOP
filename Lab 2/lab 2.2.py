stored_list = []

def count_char_in_string(words, char):
    return [sum(1 for letter in word if letter == char) for word in words]

stored_list = input("Input: ").split()
character = input("Input Character: ")
result = count_char_in_string(stored_list, character)

if result:
    print(result)