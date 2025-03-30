person = {
    'name': {
        'first': 'Иван',
        'middle': 'Иванович',
        'last': 'Иванов'
    },
    'age': 30,
    'job': 'Инженер',
    'address': {
        'street': 'ул. Ленина, 1',
        'city': 'Москва',
        'zip': '123456'
    },
    'email': 'ivan.ivanov@example.com',
    'phone': '+7 (495) 123-45-67'
}

print(f"Имя: {person['name']['first']}")
print(f"Отчество: {person['name']['middle']}")
print(f"Фамилия: {person['name']['last']}")
print(f"Возраст: {person['age']}")
print(f"Место работы: {person['job']}")
print(f"Адрес: {person['address']['street']}, {person['address']['city']}")
print(f"Email: {person['email']}")
print(f"Телефон: {person['phone']}")
