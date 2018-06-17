import staticjinja
import jinja2

index_context = {
    'page_name': 'index',
    'username': 'Леонид Федорович',
    'title': 'Главная страница| Поиск',
    'requests': 'Свежие заявки',
    'show_footer': True,
    'regions': ['Московская область', 'Ленинградская область', 'Новгородская область', 'Псковская область',
                'Мурманская область'],
    'feedback_list': [
        {
            'feedback_author': 'Кирилл, 29 лет, г. Барабинск',
            'feedback_text': '''Бла-бла, мне помогло, все супер! Бла-бла,
                мне помогло, все супер! Бла-бла, мне помогло,
                все супер! Бла-бла, мне помогло!'''
        },
        {
            'feedback_author': 'Петр, 31 год, г. Новосибирск',
            'feedback_text': '''Три-четыре, бла-бла, мне помогло, все супер! Бла-бла,
                мне непомогло, не все супер! Не все супер!
                Бла-бла, мне не помогло, не супер!'''
        },
        {
            'feedback_author': 'Анатолий, 45 лет, г. Криводановск',
            'feedback_text': '''Раз-два, бла-бла, Все быстро и качественно!
                Претензий нет. Все отлично, все супер!
                Все отлично, все супер!'''
        }]

}

comments_context = {
    'comment_list': [{
        'comment_time': 'позавчера, в 12:50',
        'request_text': '''30шт. ПК от 72-15  до ПК 21-15, Криводановка, с доставкой.''',
        'request_name': 'Петя',
        'count_views': '9'},
        {
            'comment_time': 'вчера, в 17:21',
            'request_text': '''12шт. ПК от 5-15  до ПК 11-25, ул. Ленина, без доставки.''',
            'request_name': 'Гена',
            'count_views': '11'},
        {
            'comment_time': 'сегодня, в 15:30',
            'request_text': '''56шт. ПК от 62-11  до ПК 211-15, Красный пр, с доставкой.''',
            'request_name': 'Алексей',
            'count_views': '6'}
    ]
}

requests_context = {
    'comments': 8,
    'title': 'Заявки',
    'username': 'Леонид Федорович'
}

catalog_context = {
    'username': 'Леонид Федорович',
    'title': 'Каталог организаций'
}

company_list_context = {
    'company_list': [
        {
            'company': 'ООО Монтаж',
            'working_place': 'Новосибирск',
            'production': 'Продукия: ЖБИ, бетон',
            'address': 'Адрес: Где-то на том же месте',
            'phone': 'Телефон: 00-00-01'
        },
        {
            'company': 'ООО Строй',
            'working_place': 'Новосибирск',
            'production': 'Продукия: ЖБИ, бетон',
            'address': 'Адрес: Примерно там',
            'phone': 'Телефон: 00-00-02'
        },
        {
            'company': 'ООО Космо',
            'working_place': 'Новосибирск',
            'production': 'Продукия: ЖБИ, бетон',
            'address': 'Адрес: Примерно там',
            'phone': 'Телефон: 00-00-03'
        },
        {
            'company': 'ООО Халупастрой',
            'working_place': 'Новосибирск',
            'production': 'Продукия: ЖБИ, бетон',
            'address': 'Адрес: Примерно там',
            'phone': 'Телефон: 00-00-04'
        },
        {
            'company': 'ООО Криворукий строитель',
            'working_place': 'Новосибирск',
            'production': 'Продукия: ЖБИ, бетон',
            'address': 'Адрес: Примерно там',
            'phone': 'Телефон: 00-00-02'
        }
    ]

}

company_context = {
    'username': 'Леонид Федорович',
    'title': 'Об организации'
}

profile_context = {
    'username': 'Леонид Федорович',
    'title': 'Личный кабинет'
}

# company_list_context.update(company_list)
company_context.update(company_list_context)
catalog_context.update(company_list_context)
index_context.update(comments_context)
requests_context.update(comments_context)

if __name__ == "__main__":
    site = staticjinja.make_site(outpath='static/', contexts=[
        ('index.html', index_context),
        ('requests.html', requests_context),
        ('catalog.html', catalog_context),
        ('companies.html', catalog_context),
        ('company.html', company_context),
        ('profile.html', profile_context)
    ])
    # enable automatic reloading
    site.render()
