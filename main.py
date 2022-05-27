list = []
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