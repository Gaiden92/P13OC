import logging
from django.shortcuts import render, redirect

from .models import Profile
from oc_lettings_site.settings import sentry_sdk


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque,
# quis dictum lacus d
def index(request: object) -> object:
    """A method to display the index template

    Arguments:
        request -- object: HttpRequest

    Returns:
        object: HttpResponse
    """
    logging.info("User in profiles index page.")
    try:
        with sentry_sdk.start_transaction(name="get_all_profiles"):
            profiles_list = Profile.objects.all()
            logging.info(f"{len(profiles_list)} total profiles get.")
    except ValueError:
        logging.warning("None profiles in database.")
        return redirect('index')
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi
# tristique senectus et netus et males
def profile(request: object, username: str) -> object:
    """A method to display the profile template

    Arguments:
        request -- object: HttpRequest
        username -- str: username

    Returns:
        object: HttpResponse
    """
    logging.info("User in profile page.")
    try:
        with sentry_sdk.start_transaction(name="get_profile"):
            profile = Profile.objects.get(user__username=username)
            logging.info(f'Profile: {profile.user.username}')
    except Profile.DoesNotExist:
        logging.info(f'This Profile, not exist: "{username}"')
        return redirect('profiles_index')
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
