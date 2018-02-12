with open('data.txt') as f:
    data_txt = f.read()
    data_txt = data_txt.split(' ')


n = int(input())
p = int(input())
lst1 = []
lst2 = []
for i in range(len(data_txt)):
    data_txt[i] = int(data_txt[i])
    lst2.append(str(data_txt[i]**p))

    if (data_txt[i]) // n == (data_txt[i]) / n:
        lst1.append(str(data_txt[i]))


with open('out-1.txt', 'w') as fnew1:
    fnew1.write(" ".join(lst1))
with open('out-2.txt', 'w') as fnew2:
    fnew2.write(" ".join(lst2))
