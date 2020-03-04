from peewee import *

db = SqliteDatabase('company.db')


class Company(Model):
    name = CharField()
    category = CharField(null=True)
    place = CharField(null=True)
    address_phone = CharField(null=True)
    image = CharField(null=True)

    def __repr__(self):
        return '{}: {}'.format(self.id, self.name,)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name,)

    class Meta:
        database = db


class CurrentPage(Model):
    page = IntegerField(default=1)

    def __repr__(self):
        return str(self.page)

    def __str__(self):
        return str(self.page)

    class Meta:
        database = db


if __name__ == '__main__':
    db.create_tables([Company, CurrentPage, ])
