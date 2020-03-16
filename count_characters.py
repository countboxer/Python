from collections import Counter


# This is my solution. Lengthy!
def count(string):
    return_dict = {}
    for x in string:
        if x not in return_dict:
            return_dict[x] = 1
        else:
            return_dict[x] += 1
    return return_dict


# This solution uses the collections package
def count_container(string):
    return dict(Counter(string))


# This is an elegant and one line solution
def count_count(string):
    return {i: string.count(i) for i in string}


if __name__ == '__main__':
    print(count('aba'))
    print(count_container('aba'))
    print(count_count('aba'))
