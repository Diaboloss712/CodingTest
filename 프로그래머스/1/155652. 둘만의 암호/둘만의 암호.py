def solution(s, skip, index):
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    result = []
    for char in s:
        pos = alphabet.index(char)
        new_char = alphabet[(pos + index) % len(alphabet)]
        result.append(new_char)
    return ''.join(result)