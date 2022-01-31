from signal import signal, SIGTERM, SIGNUP, pause
from  rpi_lcd import LCD
lcd=LCD()
def safe_exit(signum,frame):
    exit(1)
signal(SIGTERM, safe_exit)
signal(SIGNUP,safe_exit)

try:
    lcd.text("No wasting time")
    lcd.text("Raspberry pin")

    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()