def partitionLabels():
    s = "ababcbacadefegdehijhklij"
    dictionary = {}
    for i in range(len(s)):
        if s[i] not in dictionary:
            dictionary[s[i]] = [i]
        else:
            dictionary[s[i]].append(i)

    print(dictionary)

partitionLabels()