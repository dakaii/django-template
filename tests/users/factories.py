
import factory

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: f'lennon{n}@thebeatles.com')
    password = factory.PostGenerationMethodCall(
        'set_password', 'johnpassword'
    )

    @factory.post_generation
    def has_default_group(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            default_group, _ = Group.objects.get_or_create(
                name='group'
            )
            self.groups.add(default_group)
