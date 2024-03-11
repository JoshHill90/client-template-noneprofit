import os
from pathlib import Path
from dotenv import load_dotenv

current_dir = Path(__file__).resolve().parent		
ven = current_dir / "./env/.env/"
load_dotenv(ven)

class EmailKeys:

	worker_host = os.getenv('WOKER_EMAIL_HOST')
	worker_send_email = os.getenv('WORKER_SEND_EMAIL')
	worker_send_passwd = os.getenv('WORKER_SEND_PASSWORD')
	worker_port = os.getenv('WORKER_PORT')
	worker_manager = os.getenv('MANAGER_EMAIL')
  
  
class SettingKeys:

	django_key = os.getenv('DJANGO_KEY')
	django_debug = os.getenv('DJANGO_DEBUG')
	django_host = os.getenv('DJANGO_HOSTS')
	django_whitlist = os.getenv('DJANGO_WHITELIST')
	db_engine = os.getenv('DB_ENGINE')
	db_name = os.getenv('DB_NAME')
	db_user = os.getenv('DB_USER')
	db_key = os.getenv('DB_PASSWORD')
	db_host = os.getenv('DB_HOST')
	db_port = os.getenv('DB_PORT')
	db_wl1 = os.getenv('DJANGO_WHITELIST_ME')
	db_wl2 = os.getenv('DJANGO_WHITELIST_Client')
	db_wl3 = os.getenv('DJANGO_WHITELIST_PLAIN')
	db_wl4 = os.getenv('DJANGO_WHITELIST_WWW')


