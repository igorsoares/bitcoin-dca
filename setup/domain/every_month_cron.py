from .cron import Cron

class EveryMonth(Cron):

    def build(self):
        self.set_day_of_month()
        self.set_hour()
        self.set_minute()
        return self.build_expression()