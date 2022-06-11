# def test_example():
#     assert False, "Just test example"
import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory()

    response = client.get('/api/v1/courses/1/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course.name


@pytest.mark.django_db
def test_get_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_by_id(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/?id='+str(courses[0].id))
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_filter_by_name(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/', {'name': courses[0].name})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/api/v1/courses/', data={'name': 'test course'})

    assert response.status_code == 201
    assert Course.objects.count() == 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory()

    response = client.patch('/api/v1/courses/'+str(course.id)+'/', data={'name': 'updated name'})
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'updated name'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()

    response = client.delete('/api/v1/courses/' + str(course.id) + '/')
    assert response.status_code == 204
