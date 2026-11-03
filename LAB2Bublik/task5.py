from abc import ABC, abstractmethod


class TicketPricingStrategy(ABC):
    @abstractmethod
    def calculate(self, price, quantity):
        pass


class StandardPricing(TicketPricingStrategy):
    def calculate(self, price, quantity):
        return price * quantity


class StudentPricing(TicketPricingStrategy):
    def calculate(self, price, quantity):
        return price * quantity * 0.8


class WeekendPricing(TicketPricingStrategy):
    def calculate(self, price, quantity):
        return price * quantity * 1.1


class TicketOffice:
    def __init__(self, pricing_strategy):
        self.strategy = pricing_strategy

    def set_strategy(self, pricing_strategy):
        self.strategy = pricing_strategy

    def total(self, ticket_price, quantity):
        if isinstance(ticket_price, bool) or not isinstance(ticket_price, (int, float)):
            raise TypeError("Ціна має бути числом")
        if ticket_price <= 0 or type(quantity) is not int or quantity < 1:
            raise ValueError("Ціна має бути додатною, кількість — цілим числом від 1")
        return round(self.strategy.calculate(ticket_price, quantity), 2)


class GroupPricing(TicketPricingStrategy):
    def calculate(self, price, quantity):
        discount = 0.85 if quantity >= 5 else 1.0
        return price * quantity * discount


def demo_task5():
    office = TicketOffice(StandardPricing())
    for strategy in (StandardPricing(), StudentPricing(), WeekendPricing()):
        office.set_strategy(strategy)
        print(f"{type(strategy).__name__}: {office.total(200, 2):.2f} грн за 2 квитки")
    office.set_strategy(GroupPricing())
    print(f"GroupPricing: {office.total(200, 5):.2f} грн за 5 квитків")
    assert office.total(200, 5) == 850.0

if __name__ == "__main__":
    demo_task5()