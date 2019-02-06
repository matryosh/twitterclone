import os
from uuid import uuid4


def path_and_rename(instance, filename):
    upload_to = 'media/images'
    ext = filename.split('.')[-1]

    filename = '{}{}'.format(uuid4().hex, ext)

    return os.path.join(upload_to, filename)
