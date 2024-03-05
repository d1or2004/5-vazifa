rim = input("Rim raqam kiriting = ")
m = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
jami = 0
if len(rim) == 1:
    jami = m[rim]
else:
    item = 0
    i = 0
    while i < len(rim) - 1:
        if m[rim[i]] < m[rim[i + 1]]:
            item = m[rim[i + 1]] - m[rim[i]]
            i += 1
        else:
            item = m[rim[i]]
        jami = jami + item
        i += 1
if len(rim) > 1 and m[rim[len(rim) - 1]] <= m[rim[len(rim) - 2]]:
    jami = jami + m[rim[len(rim) - 1]]

print(jami)
