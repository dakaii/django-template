import pytest
from pytest_factoryboy import register

from .factories import UserFactory

register(UserFactory)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def api_client_with_credentials(db, user_factory, api_client):
    user = user_factory(has_default_group=True)
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)
