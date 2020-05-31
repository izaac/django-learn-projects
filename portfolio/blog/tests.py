from blog.views import detail
import pytest


def test_first(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_details(rf):
    request = rf.get('/blog/')
    response = detail(request, 1)
    assert response.status_code == 200
