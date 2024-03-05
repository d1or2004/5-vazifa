def birxil(data):
    if len(data) == 0:
        return ""

    a = data[0]
    for i in range(len(a)):
        for j in data[1:]:
            if i == len(j) or j[i] != a[i]:
                return a[0:i]

    return a


data = ['flow', 'flw', "flew"]
print(birxil(data))
