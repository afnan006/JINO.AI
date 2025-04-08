from datetime import datetime
import pytz

def get_local_time():
    tz = pytz.timezone("Asia/Kolkata")
    return datetime.now(tz).strftime("%I:%M %p %Z")
