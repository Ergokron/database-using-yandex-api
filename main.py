import yadisk
import os
class Ergokron_database:
    def __init__(self, token=None, db=None):
        if token == None:
            raise ValueError('The "token" parameter is None')
        token = str(token)
        y = yadisk.YaDisk(token=token)
        if not y.check_token():
            raise ValueError('You need use valid token')

        self.y = y
        if db == None:
            db = 'Ergokron_DB_1'

        if not y.is_dir(db):
            y.mkdir(db)
        self.general_path = db


    def set(self, key, value=None):
        if value == None:
            value = ''
        y = self.y
        general_path = self.general_path+'/'
        a = open(key+'.txt', 'w', encoding='utf-8')
        a.write(value)
        a.close()
        y.upload(key+'.txt', general_path+key+'.txt')
        os.remove(key+'.txt')
        return True

    def get(self, key):
        general_path = self.general_path+'/'
        y = self.y
        if not y.is_file(general_path+key+'.txt'):
            return None

        y.download(general_path+key+'.txt', key+'.txt')
        a = open(key+'.txt', 'r', encoding='utf-8')
        readed = a.read()
        a.close()
        os.remove(key+'.txt')
        return readed.strip()

    def append(self, key, value):
        general_path = self.general_path + '/'
        y = self.y
        if not y.is_file(general_path + key + '.txt'):
            return None

        y.download(general_path + key + '.txt', key + '.txt')
        a = open(key + '.txt', 'r', encoding='utf-8')
        readed = a.read().strip()
        a.close()
        os.remove(key + '.txt')

        a2 = open(key + '.txt', 'w', encoding='utf-8')
        a2.write(readed+value)
        a2.close()

        if y.is_file(general_path+key+'.txt'):
            y.remove(general_path+key+'.txt')
        y.upload(key+'.txt', general_path+key+'.txt')
        os.remove(key+'.txt')

        return True

    def delete(self, key):
        general_path = self.general_path + '/'
        y = self.y

        y.remove(general_path+key+'.txt')
        return True




key = ''#your yandex disk api key
db = Ergokron_database(key, 'database_name')

db.get('mykey') #                     read text from 'mykey'
db.set('mykey', 'value') #            set new value in key 'mykey'
db.append('mykey', 'value') #         add new text in key 'mykey'
db.delete('mykey') #                  delete key 'mykey'
