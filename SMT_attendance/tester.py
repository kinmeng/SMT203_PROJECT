import requests
import os

base_url = 'http://127.0.0.1:5000/'
menu_url = base_url + 'menu/'
student_url = base_url + 'student/'

def test_create(id, desc, price):
    json = {'id':id, 'desc':desc, 'price':price}
    r = requests.post(menu_url, json=json)
    print(r.status_code)
    print(r.text)


# test_create(5, "why cat", 2)


def create_student(id, name, directory):
    for filename in os.listdir(directory):
        photo_path = directory + filename
        json = {'id':1234, 'name':filename.split('.')[0], 'photo':photo_path}
        requests.post(student_url, json=json)

directory = './student_photo/'
create_student(1234, 'kinmeng', directory)

