def is_valid_ip(s):
    if s == "":
        return False
    if s.find(",") != -1:
        return False
    if s.isalpha():
        return False
    quads = s.split(".")
    if len(quads) != 4:
        return False
    for quad in quads:
        # print("[{0}]".format(quad[0]))
        if quad[0] == "0" and int(quad) > 0:
            print("1. ", quad[0])
            return False
        elif quad.isalpha():
            print("Here 2")
            return False
        elif quad.find(" ") != -1:
            print("Here 3")
            return False
        elif int(quad) < 0:
            print("Here 4")
            return False
        elif int(quad) > 255:
            print("Here 5")
            return False
    return True


print(is_valid_ip('0.0.0.0'))
print(is_valid_ip('12.255.56.1'))
print(is_valid_ip(''))
