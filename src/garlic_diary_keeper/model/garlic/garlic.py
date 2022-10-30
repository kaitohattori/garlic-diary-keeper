from datetime import date

class Garlic(object):
    def __init__(self, growth_start_date: date):
        self.growth_start_date = growth_start_date

    def elapsed_days(self) -> int:
        return (date.today() - self.growth_start_date).days
