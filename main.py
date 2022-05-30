list = []
with open('d:/data.txt', 'r', encoding='utf-8') as f:
    list = f.readline()
    if len(list)>0:
        user_dict = eval(list)
    else:
        user_dict = []
while True:
    thing = input('Что у вас?')
    if thing:
        number = int(input('Сколько ?'))
        d = dict(name=thing, amount=number)
        user_dict.append(d)
        print('Спасибо')
    if not thing:
        if len(user_dict) > 0:
            last_thing = user_dict[-1]
            last_name = last_thing.get('name')
            last_number = last_thing.get('amount')
            if last_number > 1:
                last_thing.update(amount = last_number - 1)
                last_number = 1
            else:
                user_dict.pop()
            print('Вот вам', last_name, last_number, '(шт)')
        else:
            print('Извините,подойдите позже')
    if thing == 'QUIT' and number == 0:
        user_dict.remove({'name': 'QUIT', 'amount': 0})
        break

list = str(user_dict)
with open('d:/data.txt','w',encoding='utf-8') as f:
    f.write(list)