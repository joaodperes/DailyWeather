import yagmail

city = "your_city_here"
lang = "your_lang_here"
API_KEY = "your_api_key_here"
send_to = ["email_1", "email_2"]
google_client_id = "your_client_id"
yag = yagmail.SMTP('sending_account_address', oauth2_file='credentials.json', google_client_id=google_client_id)
# Don't forget to rename file to "config.py"