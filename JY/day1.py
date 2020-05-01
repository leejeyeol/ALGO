import copy
def find_partner(found_list):
    for i in range(n):
        if i not in found_list:
            friend_list = friend_dict[str(i)]
            for friend in friend_list:
                if friend > i:
                    if friend not in found_list:
                        found_list_ = copy.deepcopy(found_list)
                        found_list_.append(i)
                        found_list_.append(friend)
                        if len(found_list_) == n:
                            global count
                            count += 1
                            print(found_list_)
                        else:
                            find_partner(found_list_)

with open("../data/day1.txt") as f:
    num = int(f.readline())
    for _ in range(num):
        l = [int(i) for i in f.readline().split()]
        n, m = l
        friends = [int(i) for i in f.readline().split()]
        friend_dict = {}
        for i in range(n):
            friend_dict[str(i)] = []


        for i in range(0, len(friends), 2):
            friend_dict[str(friends[i])].append(friends[i+1])
            friend_dict[str(friends[i+1])].append(friends[i])
        for key in friend_dict.keys():
            friend_dict[key].sort()
        print(friend_dict)

        count = 0
        found_list = []
        find_partner(found_list)
        print(count)



