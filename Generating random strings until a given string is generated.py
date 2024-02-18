import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

target_string = input("Enter the target string: ")
counter = 0
while True:
    random_string = generate_random_string(len(target_string))
    counter += 1
    if random_string == target_string:
        print(f"Random string generated after {counter} attempts: {random_string}")
        break
