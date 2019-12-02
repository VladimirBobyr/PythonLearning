# Date and Time
from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime("The current year is: %Y"))
    print(now.strftime("%a, %d, %B, %y"))
    print(now.strftime("Locate date and time: %c"))
    print(now.strftime("Locate date: %x"))
    print(now.strftime("Locate time: %X"))

if __name__ == "__main__":
    main()
