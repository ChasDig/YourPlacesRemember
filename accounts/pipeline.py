from django.contrib.auth import get_user_model


# ----- User Accounts data ----- #

def get_avatar(backend, response, user=None, *args, **kwargs):
    """
    :param backend:
    :param response:
    :param user:
    :param args:
    :param kwargs:
    :return:
    """
    if not user:
        return None

    avatar_url = None

    # Get User Avatar from VK:
    if backend.name == "vk-oauth2":

        avatar_url = response.get('photo', '')

    # Get User Avatar from Google:
    if backend.name == "google-oauth2":

        avatar_url = response['picture']

    if avatar_url:

        user.avatar = avatar_url
        user.save()
        print(user.avatar)
