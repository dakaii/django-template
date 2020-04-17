from rest_framework.reverse import reverse

import pytest


@pytest.mark.django_db
@pytest.mark.parametrize(
    'email, password, status_code', [
        ('lennon1@thebeatles.com', 'johnpassword', 200),
        ('user@example.com', 'strong_pass', 401),
    ]
)
def test_login_data_validation(
    email, password, status_code, api_client_with_credentials, api_client
):
    # user_factory(has_default_group=True)
    url = reverse('login')
    data = {
        'email': email,
        'password': password
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status_code
