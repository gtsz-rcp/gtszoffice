import pytest
import json
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
    'publishedtime': datetime.utcnow
}


def test_pages_without_id_get(client):
    rv = client.get('/pages', follow_redirects=True)
    assert rv.status == '200 OK'


def test_pages_without_id_post(client):
    rv = client.post('/pages', data=sample_data, follow_redirects=True)
    assert rv.status == '200 OK'
