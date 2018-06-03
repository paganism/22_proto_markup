import staticjinja
import jinja2

index_context = {
    'page_name': 'index',
    'username': 'Леонид Федорович',
    'title': 'Главная страница| Поиск',
    'requests': 'Свежие заявки',
    'comments': 4,
    'show_footer': True,
    'items': 3,
    'feedback_author': 'Кирилл, 29 лет, г. Барабинск',
    'feedback_text': '''Бла-бла, мне помогло, все супер! Бла-бла,
                мне помогло, все супер! Бла-бла, мне помогло,
                все супер! Бла-бла, мне помогло, все супер!
                Бла-бла, мне помогло, все супер!''',

}

comments_context = {
    'comment_time': 'вчера, в 12:50',
    'request_text': '''60шт. ПК от 72-15  до ПК 21-15, Криводановка, с доставкой.''',
    'request_name': 'Алексей',
    'count_views': '9'

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
    'company': 'ООО Строй-Скрвис-Монтаж',
    'working_place': 'Новосибирск',
    'production': 'Продукия: ЖБИ, бетон',
    'address': 'Адрес: Под часами, на том же месте',
    'phone': 'Телефон: 00-00-00',
    'items': 8
}

company_context = {
    'username': 'Леонид Федорович',
    'title': 'Об организации'
}

profile_context = {
    'username': 'Леонид Федорович',
    'title': 'Личный кабинет'
}

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
