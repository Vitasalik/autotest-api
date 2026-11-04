import faker

fake = faker.Faker()

def get_random_email() -> str:
    return fake.email()