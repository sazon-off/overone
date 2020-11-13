from datetime import datetime


class Ad:
    count = 0

    def __init__(self):
        self.heading = input('Заголовок: ')
        self.description = input('Описание: ')
        self.author = input('Автор: ')
        self.date = datetime.now()

    def info(self):
        Ad.count += 1
        print(self.heading)
        print(self.description)
        print(self.author)
        print(self.date)
        print('Просмотры: ', Ad.count)

    def setRename(self):
        self.heading = input('Заголовок: ')

    def getRename(self):
        try:
            return self.heading
        except:
            return

    def setEdit(self):
        self.description = input('Описание: ')

    def getEdit(self):
        try:
            return self.description
        except:
            return


d = Ad()
d.info()
d.setRename()
d.info()
