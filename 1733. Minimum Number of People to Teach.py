from collections import defaultdict,Counter

def minimumTeachings():
    # n = 3
    # languages = [[2],[1,3],[1,2],[3]]
    # friendships = [[1,4],[1,2],[3,4],[2,3]]
    n = 2
    languages = [[1],[2],[1,2]]
    friendships = [[1,2],[1,3],[2,3]]

    row = len(friendships)
    col = len(friendships[0])

    user_need_language = set()
    for user1,user2 in friendships:
        common_language = set(languages[user1-1]) & set(languages[user2 - 1])
        if not common_language:
            user_need_language.add(user1)
            user_need_language.add(user2)
    print(user_need_language)

    language_count = Counter()
    for user in user_need_language:
        for lanuage_id in languages[user - 1]:
            language_count[lanuage_id] += 1
            print(language_count)

    print(language_count)

    if language_count:
        return len(user_need_language) - max(language_count.values())
    else: return 0

    # cant_comm = []
    
    # for i in range(row):
    #     u,v = friendships[i]

    #     common_language = set(languages[u - 1]) & set(languages[v - 1])
    #     if not common_language:
    #         cant_comm.append(friendships[i])

    # min_friend_teach = float("inf")

    # for i in range(1,n+1):
    #     min_people_to_teach = set()

    #     for u,v in cant_comm:
    #         if i not in languages[u - 1]:
    #             min_people_to_teach.add(u)
            
    #         if i not in languages[v - 1]:
    #             min_people_to_teach.add(v)

    # return min_friend_teach

print(minimumTeachings())