def word_match(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr = ctr + 1
            lst.append(word)

    print(lst)
    return ctr 
count = word_match("cdc", "abc", "1234321")
print(count)
