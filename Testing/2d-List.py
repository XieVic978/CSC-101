from datetime import datetime
import time

current_time = datetime.now().strftime("%I:%M %p")
idx = 0
while True:
    print(current_time)
    time.sleep(10)