import random, sys, json
sys.path.insert(0, '..')
from pyfb.pyfb import PyFb
import model
from angusphotos import random_angus_photo_file_path

fb_client = PyFb(json.load(open('../tokens.json', 'r'))['pcbuilder'])

fb_client.create_post(message=model.pstr_pc(mode.random_pc()), image_path=random_angus_photo_file_path())