'''
ogrenciler = {
    '120': {
        'ad' : 'Nurdan',
        'soyad' : 'Kolay',
        'age' : '30'
    },
    '121': {
        'ad' : 'Nuray',
        'soyad' : 'Kolay',
        'age' : '33'
    }
}

'''

students = {}

number = input("Student ID: ")
name = input("Student Name: ")
surname = input("Student Surname: ")

students[number] = {
    'name': name,
    'surname': surname
}

print(students)

print('*'*50)

student = students[number]

print(f"This student {number} ID Student Name: {student['name']} Surname: {student['surname']}")
