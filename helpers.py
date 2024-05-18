import faker


def get_order_data():
    fake = faker.Faker("ru_RU")
    name = fake.first_name()
    surname = fake.last_name()
    address = fake.street_address()
    telephone = fake.msisdn()
    calendar_date = fake.date()
    return name, surname, address, telephone, calendar_date

