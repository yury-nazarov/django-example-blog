- [87-94. Пагинация](https://github.com/yury-nazarov/django-example-blog/commit/0b99cad654f4fed81f8cccb6fbfbb651f3d5f299)
  - https://docs.djangoproject.com/en/5.1/ref/paginator/
  - ```commandline
    with page=pages
    
    page.has_previous           - Bool. Предыдущая страница существует?
    page.has_next               - Bool. Следующая страница существует?
    page.previous_page_number   - int.  предыдущая страницы
    page.next.page_number       - int.  следующая страница 
    page.number                 - int.  текущая страницы
    page.paginator.num_pages    - int.  всего страниц
    ```
  - [95-97. Представление на основе классов](https://github.com/yury-nazarov/django-example-blog/commit/0b1a4f7a98523c71a8b83c72464ed2552c447b07)
    - ListView - типовое представлеие в Django
    - post_obj - передаваемая в шаблон переменная на основе объекта ListView
    - https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/