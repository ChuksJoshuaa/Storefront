from store.models import Collection
from django.contrib.auth.models import User
from rest_framework import status
import pytest
from model_bakery import baker


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.fixture
def authenticate_user(api_client):
    def do_authenticate_user(user):
        return api_client.force_authenticate(user)
    return do_authenticate_user


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate_user, create_collection):
        authenticate_user(user={})
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticate_user, create_collection):
        authenticate_user(user=User(is_staff=True))
        response = create_collection({'title': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, authenticate_user, create_collection):
        authenticate_user(user=User(is_staff=True))
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get('id') > 0


@pytest.mark.django_db
class TestRetrieveColledction:
    def test_if_collection_exists_returns_200(self, api_client):

        collection = baker.make(Collection)

        response = api_client.get(f'/store/collections/{collection.id}')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }

# before using python -m pytest, make sure pytest-django is installed. if not
# then run python -m pip install pytest-django
# after that run your test now
