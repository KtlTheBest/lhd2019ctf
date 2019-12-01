flag = "flag{Knowing-JavaScript-Doesnt-Hurt-Much}"
res = []

for i, c in enumerate(flag):
    val = 0
    C = ord(c)
    if i == 0:
        val = C ^ 255
    else:
        val = (C ^ 255) ^ res[i - 1]
    res.append(val)

print(res)
