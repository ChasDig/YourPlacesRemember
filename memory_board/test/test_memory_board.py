from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from ..models import MemoryPlacesModel


# ----- Test: Memory ----- #

class MemoryTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):

        # Create test users:
        cls.USER_PASSWORD = "random_123"
        cls.UserModel = get_user_model()

        COUNT_USERS = 3

        cls.UserModel.objects.bulk_create([

            cls.UserModel(
                username=f'username_{item}',
                email=f'username_{item}@mail.ru',
                password=f'password_{item}',
            ) for item in range(3)
        ])

        cls.all_test_users = cls.UserModel.objects.all()

        # Create memory for test users:

        COUNT_MEMORIES_USER = 3

        for test_user in cls.all_test_users:
            all_memories_test_user = [
                    MemoryPlacesModel(
                        title=f'title_{test_user.username}_{item}',
                        description=f'description_{test_user.username}_{item}',
                        review=f'review_{test_user.username}_{item}',
                        address=f'address_{test_user.username}_{item}',
                        user=test_user,
                        slug=f'slug_{test_user.username}_{item}',
                    ) for item in range(COUNT_MEMORIES_USER)
                ]
            MemoryPlacesModel.objects.bulk_create(all_memories_test_user)

    def test_memories_users(self):

        for test_user in self.all_test_users:
            with self.subTest(f'Memories {test_user.username}'):

                self.client.force_login(test_user)

                response = self.client.get(reverse("memory_list"))

                self.assertEqual(response.status_code, 200)

                response_memories_id = tuple(
                    response.context['memory_list'].values_list('pk', flat=True)
                )

                test_user_memories_id = tuple(
                    test_user.memory_list.values_list('pk', flat=True)
                )

                self.assertEqual(test_user_memories_id, response_memories_id)

    def test_create_new_memory(self):

        test_user = self.all_test_users[0]
        test_user_count_memories_before = test_user.memory_list.count()

        self.client.force_login(test_user)

        data_user_new_memory = {
            'title': 'title_new_test',
            'description': 'description_new_test',
            'review': 'review_new_test',
            'address': 'address_new_test',
            'user': 'test_user',
            'slug': 'slug_new_test',
        }

        response = self.client.post(
            path=reverse('memory_create'),
            data=data_user_new_memory,
        )

        self.assertRedirects(
            response=response,
            expected_url=reverse('memory_list'),
            status_code=302,
            target_status_code=200,
        )

        self.assertEqual(test_user.memory_list.count(), test_user_count_memories_before + 1)
