from decouple import config
import logging

# Ensure LOGS is defined so the except block works
logging.basicConfig(level=logging.INFO)
LOGS = logging.getLogger(__name__)

try:
    # Uses .env value if present, otherwise defaults to '16732227'
    APP_ID = config("APP_ID", default=16732227, cast=int)
    
    # Uses .env value if present, otherwise defaults to your hash string
    API_HASH = config("API_HASH", default="8b5594ad7ad37f3a0a7ddbfb3963bb51")
    
    # Hardcoded Bot Token (Not reading from decouple/env)
    BOT_TOKEN = "7142361995:AAHHDmYyE4plBuzBTO4Q0fArJ3P4kzzETzE"
    
    # Other configurations
    # DEV stays as an integer because the code checks 'e.sender_id != DEV'
    DEV = config("DEV", default=5868426717, cast=int)
    
    # OWNER changed to a string. This prevents the 'int is not iterable' error!
    OWNER = config("OWNER", default="5868426717")
    
    ffmpegcode = ["-preset veryfast -c:v libx264 -b:a 64k -crf 38 -map 0 -c:s copy"]
    THUMB = config("THUMBNAIL", default="https://injured-tan-vshddubr0a.edgeone.app/IMG_20260326_132346_678.jpg")

except Exception as e:
    LOGS.info("Configuration Error occurred")
    LOGS.info(str(e))
    exit(1)
