def list_methods():
    my_list = []

    people: list[str] = ['Ralph', 'Maron', 'Cazmir']

    people.sort(key=lambda name: name.lower(), reverse=True)
    print(people)


list_methods()
