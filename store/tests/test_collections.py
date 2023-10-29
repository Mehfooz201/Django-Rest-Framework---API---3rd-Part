from django.contrib.auth.models import User
from store.models import Collection
from rest_framework import status
from rest_framework.test import APIClient
import pytest
from model_bakery import baker



@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonyms_returns_401(self):
        #Arrange
        #Action
        client = APIClient()
        response = client.post('/store/collections/', {'title':'a'})
        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    

    def test_if_user_is_not_admin_returns_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title':'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_user_is_invalid_returns_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/store/collections/', {'title':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None 
    
    def test_if_user_is_valid_returns_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/store/collections/', {'title':'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_colleciton_exists_return_200(self, api_client):
        #arrange
        collection = baker.make(Collection)

        #Action
        response = api_client.get(f'/store/collections/{collection.id}/')

        #Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id' : collection.id,
            'title' : collection.title,
            'products_count' : 0
        }