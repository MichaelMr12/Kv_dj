result = []
data = 'данные', '"данные, внутри которых есть запятая"', '"в этих ""данных, есть и запятая"" и кавычки"'
line = 'Анна Павловна Иванова,"[запись 1, запись 2, запись 3]", ,2'
sep = ','
res = line.split(sep)
count = 0
for d in res:
    if '"' in d:
        count+=1
        sp = d.split('"')
        temp = ''
        for s in sp:
            if s != '':
                temp+=s


    else:
        result.append(d)

print(result)
