from collections import Counter

def customSortString():
    order = "hucw"
    s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
    result = ""
    order_dict = {}
    s_dict = Counter(s)

    for i in range(len(order)):
        if order[i] in s_dict:
            order_dict[order[i]] = order_dict.get(order[i],i)
            result += order[i] * s_dict[order[i]]
            del s_dict[order[i]]

    for key,value in s_dict.items():
        result += key * value

    return result

print(customSortString())