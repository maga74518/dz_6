my_list = [5, 3, 2, 5, 10, 15, 10, 8, 3, 8]

def get_unic(my_list):
    num = []
    for i in range(len(my_list)):
        if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
            num.append(my_list[i])
    return num

print(get_unic(my_list))