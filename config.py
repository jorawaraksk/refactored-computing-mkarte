import os

# Renamed to prevent clashing with the Compressor bot token
RESTRICTED_BOT_TOKEN = os.environ.get("RESTRICTED_BOT_TOKEN", "7078710813:AAEewmdbVbBK9F67F1h2IwOl0IVAI8YXYlo")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "16732227"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8b5594ad7ad37f3a0a7ddbfb3963bb51")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5868426717"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://zuzoo:Movie12345@cluster0.y7xfsuh.mongodb.net") 
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
