import faker

fake = faker.Faker()

def get_random_email():
    return fake.email()