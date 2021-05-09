def sort_string(input):
    originalStr = input.split()
    sortedStr = [word.lower() + word for word in originalStr]
    sortedStr.sort()
    sortedStr = [word[len(word) // 2:] for word in sortedStr]
    return ' '.join(sortedStr)

print(sort_string("BANANA apple orange"))