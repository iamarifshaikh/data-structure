def findCommonResponse():
    responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
    hashtable = {}
    print(responses)
    for response in responses:
        for comment in set(response):
            if comment not in hashtable:
                hashtable[comment] = 1
            else:
                hashtable[comment] += 1
    
    most_common_response = responses[0][0]

    for word,count in hashtable.items():
        if hashtable[most_common_response] < hashtable[word] or (hashtable[most_common_response] == count and word < most_common_response):
            most_common_response = word
    return most_common_response

result = findCommonResponse()
print(result)