import uuid

rain = 10000
length = 10


def my_random_string(string_length=10):

    # Convert UUID format to a Python string.
    random = str(uuid.uuid4())

    # Make all characters uppercase.
    random = random.upper()

    # Remove the UUID '-'.
    random = random.replace("-", "")

    # Return the random string.
    return random[0:string_length]


for x in range(rain):
    print(my_random_string(10))
