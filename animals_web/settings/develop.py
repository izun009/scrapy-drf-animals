
try:
    from .base import *
    DEBUG=True
    SECRET_KEY = os.environ.get('SECRET_KEY')

    DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'animals_db',
        'CLIENT': {
            'host': '0.0.0.0',
            'port': 27017,
            'username': 'izzun',
            'password': '1234',
            #'authSource': 'admin',  # Specify the authentication database here
        }
    }
}

    # DATABASES = {
    #     "default": {
    #         "ENGINE": os.environ.get('DB_ENGINE'),
    #         "NAME": os.environ.get('DB_NAME'),
    #         'CLIENT': {
    #             'host': os.environ.get('DB_HOST'),
    #             'port': os.environ.get('DB_PORT'),
    #             'username': os.environ.get('DB_USER'),
    #             'password': os.environ.get('DB_PASS'),
    #             #'authSource': 'admin',  # Specify the authentication database here
    #         }
    #     }
    # }

except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


