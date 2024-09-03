class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        print(f'{self.name} отправил сообщение в {user.name}: {message}')

    def post(self, message):
        print(f'{self.name} выложил пост: {message}')

    def info(self):
        return ''

    def describe(self):
        print(f'Имя: {self.name}\n{self.info()}')


class Person(User):
    def __init__(self, name, birth_date):
        super().__init__(name)
        self.birth_date = birth_date

    def info(self):
        return f'Дата рождения: {self.birth_date}'

    def subscribe(self, user):
        print(f'{self.name} подписался на {user.name}')


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f'Описание: {self.description}'


person = Person('Neo', '19.10.1976')
community = Community('Комюнити', 'DevOooooops i did it again')
person.send_message(community, 'Алоха!')
person.post('Дратути!')
person.describe()
person.subscribe(community)
community.describe()
