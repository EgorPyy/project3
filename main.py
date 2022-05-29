list = []
with open('d:/data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list.append(line)
while True:
    thing = input ('Что у вас?')
    if thing:
        list.append(thing)
        print('Спасибо')
    if not thing:
        if len(list)>0:
            last_thing = list[-1]
            list.pop()
            print('Вот вам',last_thing)
        else:
            print('Извините,подойдите позже')
    if thing == 'QUIT':
        list.remove('QUIT')
        break
with open('d:/data.txt', 'w', encoding='utf-8') as f:
    f.writelines([i + '\n' for i in list])
