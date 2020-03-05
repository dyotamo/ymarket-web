from peewee import *

db = PostgresqlDatabase('d5g1qf9obgq8n1', user='tbufeyofxqgkoj', password='c3db0dc459116a8ab04650fd8857c1814509f1013f8f8f7097309017f1459d50',
                        host='ec2-18-215-99-63.compute-1.amazonaws.com', port=5432)


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
