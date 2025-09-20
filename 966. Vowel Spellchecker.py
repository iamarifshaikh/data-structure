from collections import Counter

# wordList = ["ae","aa"]
# queries = ["UU"]
wordList = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
vowels = {"A","a","E","e","I","i","O","o","U","u"}
set_list = set(wordList)

def spellchecker():
    vowels = {"A","a","E","e","I","i","O","o","U","u"}
    set_list = set(wordList)
    answer = []
    case_sensitive_table = {}
    vowel_error_table = {}

    for word in wordList:
        if word.lower() not in case_sensitive_table: case_sensitive_table[word.lower()] = word

    for word in wordList:
        string = ""

        for w in range(len(word)):
            if word[w] in vowels: string += "*"
            else: string += word[w]
        
        if string.lower() not in vowel_error_table: vowel_error_table[string.lower()] = word

    for query in queries:
        if query in set_list:
            answer.append(query)
            continue

        if query.lower() in case_sensitive_table:
            answer.append(case_sensitive_table[query.lower()])
            continue

        string = ""
        for q in range(len(query)):
            if query[q] not in vowels: string += query[q]
            else: string += "*"

        if string.lower() in vowel_error_table: answer.append(vowel_error_table[string.lower()])
        else: answer.append("")

    return answer
print(spellchecker())