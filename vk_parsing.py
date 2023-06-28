import requests
import config
def VKrequest(user_id):
    response = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': config.VK_TOKEN,
                                'v': config.VK_API_VERSION,
                                'user_ids': user_id,
                            'fields': 'about,bdate,education,sex,books,career,city,contacts,counters,common_count,interests,photo_max_orig'       #Писать через запятую
                            }
                            )
    data = response.json()['response'][0]
    #print(data)
    return Request_processing(data)


    #return data
def Request_processing(data):
    alldata = []
    alldata.append(data['first_name'])
    alldata.append(data['last_name'])
    if data['sex'] != '':
        if int(data['sex']) == 1:
            alldata.append('Пол: Женщина')
        elif int(data['sex']) == 2:
            alldata.append('Пол: Мужчина')
        else:
            alldata.append('Пол: Не указан')
    else:
        alldata.append('Пол: Не указан')
    try:
        if data['bdate'] != '':
            alldata.append('День рождения: ' + str(data['bdate']))
        if data['about'] != '':
            alldata.append('О пользователе: ' + str(data['about']))
    except:
        pass
    if data['mobile_phone'] == '' and data['home_phone'] == '':
        alldata.append('Номер не указан')

    elif data['mobile_phone'] != '' or data['home_phone'] != '':
        if data['mobile_phone'] != '':
            alldata.append('Номер телефона: ' + str(data['mobile_phone']))
        if data['home_phone'] != '':
            alldata.append('Номер домашнего телефона: ' + str(data['home_phone']))
    try:
        alldata.append('Друзья: '+str(data['counters']['friends']))
        alldata.append('Подписчики: '+str(data['counters']['followers']))
        alldata.append('Общие друзья: '+str(data['common_count']))
    except:
        alldata.append('Ошибка получения доп данных о друзьях')

    try:
        alldata.append('сохранённые страницы: '+str(data['counters']['pages']))
        alldata.append('Музыкальные записи: ' + str(data['counters']['audios']))
    except:
        alldata.append('Ошибка получения доп данных об аккаунте')
    try:
        alldata.append('Посты: ' + str(data['counters']['posts']))
    except:
        pass
    try:
        if data['city']['title'] != '':
            alldata.append('Город: ' + str(data['city']['title']))
    except:
        alldata.append('Город не указан')
    try:
        if data['books'] != '':
            alldata.append('Книги пользователя: ' + str(data['books']))
    except:
        alldata.append('Книги не указаны')
    try:
        if data['university_name'] != '':
            alldata.append('Университет: ' + str(data['university_name']))
        if data['faculty_name'] != '':
            alldata.append('Факультет: ' + str(data['faculty_name']))
    except:
        alldata.append('ВУЗ не указан')

    print(data)
    #print(len(alldata),alldata)
    return alldata



#VKrequest('rekryt98')
print(1)



