import logging
from oc_lettings_site.settings import sentry_sdk
from django.shortcuts import render, redirect

from lettings.models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum,
# consectetur quis velit. Sed non placerat massa.
# Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
# Cras eget scelerisque
def index(request: object) -> object:
    """A class represent the index view

    Arguments:
        request -- object: HttpRequest

    Returns:
        object: a Http response object
    """
    logging.info("User in lettings index page.")
    try:
        with sentry_sdk.start_transaction(name="get_all_lettings"):
            lettings_list = Letting.objects.all()
            logging.info(f"This user has {len(lettings_list)} lettings.")
    except ValueError:
        logging.warning("No lettings in database")
        return redirect("index")
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim,
# odio eu consequat pretium, purus urna vulputate arcu, vitae efficitur
# lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet. Suspendisse porta dui eget
# sem accumsan interdum. Ut quis urna pellentesque justo matti
# ullamcorper ac non tellus. In tristique mauris eu velit fermentum,
# tempus pharetra est luctus. Vivamus consequat aliquam libero,
# eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor elementum.
# Donec quis nisi ligula. Integer vehicula tincidunt enim,
# ac lacinia augue pulvinar sit amet.
def letting(request: object, letting_id: id) -> object:
    """A class to represent a letting view

    Arguments:
        request -- object: HttpRequest
        letting_id -- int: letting id

    Returns:
        _description_
    """
    logging.info("User in letting page.")
    try:
        with sentry_sdk.start_transaction(name="get_letting"):
            letting = Letting.objects.get(id=letting_id)
            context = {
                'title': letting.title,
                'address': letting.address,
                }
            logging.info(f'Letting: {letting.title}')
    except Letting.DoesNotExist:
        logging.info(f'This Letting id, not exist: "{letting_id}"')
        return redirect("lettings_index")

    return render(request, 'lettings/letting.html', context)
