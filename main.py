# Словарь
books = [
    {'title': 'Реквием по мечте', 'author': 'Хьюберт Селби', 'year': '1978'},
    {'title': 'Бойцовский клуб', 'author': 'Чак Паланик', 'year': '1997'},
    {'title': 'На игле', 'author': 'Ирвин Уэлш', 'year': '1993'},
    {'title': 'Критика чистого разума', 'author': 'Иммануил Кант', 'year': '1781'},
    {'title': 'Метро 2033', 'author': 'Дмитрий Глуховский', 'year': '2002'},
]

# Перебор всех книг и вывод информации
for index in range(len(books)):
    print(f"**Книга {index + 1}***")
    print(f"Название: {books[index]['title']}, Автор: {books[index]['author']}")
    print(f"*** {books[index]['year']}***")
    print()