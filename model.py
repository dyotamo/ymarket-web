from os import environ
from dnsparse import parse
from peewee import *

url = parse(environ['DATABASE_URL'])

db = PostgresqlDatabase(url.scheme, user=url.username=, password=url.password,
                        host=url.host, port=url.port)


class Company(Model):
    name = CharField()
    category = CharField(null=True)
    place = CharField(null=True)
    address_phone = CharField(null=True)
    description = CharField(null=True)
    latitude = CharField(default='-25.979234')
    longitude = CharField(default='32.577744')
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
