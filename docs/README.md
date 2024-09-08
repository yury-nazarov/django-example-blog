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
  