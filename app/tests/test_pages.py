import pytest
import uuid
from datetime import datetime
from manage import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


sample_data = {
    'id': 1,
    'type': 'page',
    'slug': 'test_case',
    'title': 'test case title',
    'subtitle': 'test case subtitle',
    'author': 1,
    'content': 'test case content',
    'publishedtime': datetime.utcnow()
}


def test_pages_without_id_get(client):
    rv = client.get('/pages', follow_redirects=True)
    assert rv.status == '200 OK'


def test_pages_without_id_post(client):
    sample_data['slug'] = uuid.uuid4().hex[:6].upper()
    rv = client.post('/pages/', data=sample_data, follow_redirects=True)
    assert rv.status == '200 OK'


def test_pages_with_slug_get(client):
    rv = client.get('/pages/test_page', follow_redirects=True)
    assert rv.status == '200 OK' or rv.status == '404 NOT FOUND'


def test_pages_with_id_get(client):
    rv = client.get('/pages/3', follow_redirects=True)
    assert rv.status == '200 OK'


def test_pages_with_id_put(client):
    sample_data['id'] = 3
    sample_data['slug'] = ''
    rv = client.put('/pages/3', data=sample_data, follow_redirects=True)
    assert rv.status == '200 OK'


def test_pages_with_id_delete(client):
    rv = client.delete('/pages/3', follow_redirects=True)
    assert rv.status == '200 OK'


def test_posts_without_id_get(client):
    rv = client.get('/posts', follow_redirects=True)
    assert rv.status == '200 OK'


def test_posts_without_id_post(client):
    sample_data['type'] = 'post'
    sample_data['slug'] = uuid.uuid4().hex[:6].upper()
    rv = client.post('/posts/', data=sample_data, follow_redirects=True)
    assert rv.status == '200 OK'


def test_posts_with_slug_get(client):
    rv = client.get('/posts/test_page', follow_redirects=True)
    assert rv.status == '200 OK' or rv.status == '404 NOT FOUND'


def test_posts_with_id_get(client):
    rv = client.get('/posts/3', follow_redirects=True)
    assert rv.status == '200 OK'


def test_posts_with_id_put(client):
    rv = client.put('/posts/3', follow_redirects=True)
    assert rv.status == '200 OK' or rv.status == '404 NOT FOUND'


def test_posts_with_id_delete(client):
    rv = client.delete('/posts/3', follow_redirects=True)
    assert rv.status == '200 OK' or rv.status == '404 NOT FOUND'
