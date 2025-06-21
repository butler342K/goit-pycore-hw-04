# Common decoration
def print_title(title):
    raw_length = 150
    name = 'Vitaly Kichenko'
    theme = 'Homework GoIT'
    print(' ')
    print('*'*raw_length)
    print(f'**{theme:^{raw_length-4}}**')
    print('**' + ' '*(raw_length-4) +'**')
    print(f'**{name:^{raw_length-4}}**')
    print('**' + ' '*(raw_length-4) +'**')
    print(f'**{title:^{raw_length-4}}**')
    print('*'*raw_length)
    print(' ')

def print_footer(message):
    raw_length = 150
    print('='*raw_length)
    print(f'{message:>{raw_length}}')
    print(' ')

# Task1. Salary analysis

# Gen random users and salary. Manual generation is too boring for me)
def generate_user():
    import faker
    import faker.config
    from faker import Faker
    fake = Faker(locale='uk_UA')
    user = fake.first_name() + ' ' + fake.last_name()
    return(user)

import random
user_list = []

with open('users.txt', 'w', encoding='utf-8') as file:
    for i in range(20):
        user = generate_user()
        salary = random.randint(20, 50) * 1000
        user_list.append((user, salary))
        file.write(user + ', ' + str(salary) + '\n')

# Function to calculate total and average salary from file
def total_salary(path):
    total = 0
    average = 0
    cnt = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            user, salary = line.strip().split(', ')
            total += int(salary)
            cnt += 1
        if cnt > 0:
            average = round(total / cnt)
    return (total, average)

# Task 2
def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                except ValueError:
                    print(f"Помилка читання рядка : {line.strip()}")
                    continue
                cats.append({
                    'id': id,
                    'name': name,
                    'age': int(age)
                })
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []
    return cats

# Task 3.

# Output results

print_title('Theme 6')
print('Завдання 1. Аналіз заробітної плати')
total, average = total_salary("users.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
print(' ')
print('Завдання 2. Інформація про котів')
cats_info = get_cats_info('cats_db.txt')
print(cats_info)


# print_footer('End of Homework')