from .cron import Cron

class EveryWeekDay(Cron):
    
    def build(self):
        self.set_week_day()
        self.set_hour()
        self.set_minute()
        return self._build_expression()