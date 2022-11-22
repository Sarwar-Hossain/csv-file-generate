import csv
from django.http import HttpResponse


# install csv : pip install python-csv
# https://www.codingem.com/python-write-to-csv-file/

def csv(request):
    student_header = ['name', 'age', 'major', 'minor']

    student_data = [
        {'name': 'Jack', 'age': 23, 'major': 'Physics', 'minor': 'Chemistry'},
        {'name': 'Sophie', 'age': 22, 'major': 'Physics', 'minor': 'Computer Science'},
        {'name': 'John', 'age': 24, 'major': 'Mathematics', 'minor': 'Physics'},
        {'name': 'Jane', 'age': 30, 'major': 'Chemistry', 'minor': 'Physics'}
    ]

    with open('students.csv', 'w') as file:

        # Create a CSV dictionary writer and add the student header as field names
        writer = csv.DictWriter(file, fieldnames=student_header)

        # Use writerows() not writerow()
        writer.writeheader()
        # writer.writerow(student_data) # for single data
        writer.writerows(student_data)

    return HttpResponse('csv file generated!')
