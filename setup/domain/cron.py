class Cron:

    def __init__(self):
        self.minute = '*'
        self.hour = '*'
        self.day = '*'
        self.month = '*'
        self.weekday = '*'

    def set_int_value(self, message: str, min_value: int, max_value: int):
        try:
            while True:
                value = int(input(message))
                if min_value <= value <= max_value:
                    return value
                print(f"Out of the {min_value}-{max_value} range")
        except Exception as e:
            print("Invalid value")

    def set_minute(self):
        self.minute = self.set_int_value("At minute (0-59): ", 0, 59)
    
    def set_hour(self):
        self.hour = self.set_int_value("At hour (0-24): ", 0, 24)

    def set_day_of_month(self):
        self.day = self.set_int_value("Day of month: ", 1, 28)

    def set_month(self):
        self.month = self.set_int_value("Month (1-12): ", 1, 12)

    def set_week_day(self):
        self.weekday = self.set_int_value("Weekday (0-6). 0 being Sunday: ", 0, 6)

    def _build_expression(self):
        return f'{self.minute} {self.hour} {self.day} {self.month} {self.weekday}'
        
            