from datetime import datetime


class Ad:
    count = 0

    def __init__(self, heading = input('Заголовк:'), description = input('Описание: '), author = input('Автор: ')):
        self.heading = heading
        self.description = description
        self.author = author
        self.date = datetime.now()

    def info(self):
        Ad.count += 1
        print(self.heading)
        print(self.description)
        print(self.author)
        print(self.date)
        print('Просмотры: ', Ad.count)

    def setRename(self, heading):
        self.heading = heading

    def getRename(self):
            return self.heading

    def setEdit(self, description):
        self.description = description

    def getEdit(self):
            return self.description


d = Ad()
d.info()
d.setRename('aaa')
d.info()