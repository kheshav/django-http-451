from django.conf import settings
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
settings.GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')
