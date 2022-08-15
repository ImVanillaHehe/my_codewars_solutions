def solution(s):
    final_str = []
    for letter in s:
        if letter.islower():
            final_str.append(letter)
        elif letter.isupper():
            final_str.append(' ' + letter)
    return ''.join(final_str)
