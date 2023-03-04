import requests
from data import SLOTS, FACULTIES, COURSES, REGISTER_COURSES
import json

API_BASE = 'http://localhost:3000'
STUDENT_AUTH_TOKEN = 'ENTER STUDENT AUTH TOKEN HERE'
ADMIN_AUTH_TOKEN = 'ENTER ADMIN AUTH TOKEN HERE'

url = lambda path: API_BASE + path

def make_request(path, body=None, access_scope='student', request_type='POST'):
    try:
        headers = {
            'Authorization': '',
            'Content-Type': 'application/json'
        }
        if access_scope == 'student':
            headers['Authorization'] = STUDENT_AUTH_TOKEN
        elif access_scope == 'admin':
            headers['Authorization'] = ADMIN_AUTH_TOKEN

        request_function = None
        if (request_type == 'POST'):
            request_function = requests.post
        elif (request_type == 'GET'):
            request_function = requests.get
        else:
            raise NotImplementedError('Request type was not implemented.')

        print(path, body)
        json_body = json.dumps(body)
        r = request_function(url(path), json_body, headers=headers)
        response_data = r.json()
        return [r.status_code, response_data]
    except Exception as e:
        if isinstance(e, NotImplementedError):
            raise e
        return [400, {}]

def create_slot(body):
    return make_request('/admin/slot', body, access_scope='admin')

def create_faculty(body):
    return make_request('/admin/faculty', body, access_scope='admin')

def create_course(body):
    return make_request('/admin/course', body, access_scope='admin')

def create_student(body):
    return make_request('/admin/student', body, access_scope='admin')

def register_course(body):
    return make_request('/register', body)

def create_slots():
    for slot in SLOTS:
        create_slot({ "id": slot, "timings": SLOTS[slot]})

def create_faculties():
    for faculty in FACULTIES:
        create_faculty({ "name": faculty })

def create_courses():
    for course in COURSES:
        create_course(course)

def register_courses():
    responses = []
    for course in REGISTER_COURSES:
        responses.append(
            register_course(course)
        )

    for i in [1, 2, 3, 5]:
        if responses[i][1]['success']:
            raise Exception('Test failed!')

def timetable():
    [status_code, timetable_response] = make_request('/timetable', request_type='GET')
    print(timetable_response['data']['registered_courses'])

def main():
    create_slots()
    create_faculties()
    create_courses()
    register_courses()
    timetable()

if __name__ == '__main__':
    main()
