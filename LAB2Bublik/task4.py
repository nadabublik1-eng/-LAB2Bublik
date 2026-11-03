class PostalDelivery(DeliveryMethod):
    @property
    def method_name(self):
        return "Поштова служба"

    def calculate_cost(self, weight_kg):
        return 40 + 10 * weight_kg

    def estimate_days(self, distance_km):
        return 2 if distance_km <= 100 else 5


class DeliveryJournal:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)


class DeliveryService:
    def __init__(self, delivery_method, journal):
        self.delivery_method = delivery_method
        self.journal = journal

    def create_order(self, weight_kg, distance_km):
        if weight_kg <= 0 or distance_km < 0:
            raise ValueError("Маса має бути > 0, відстань — >= 0")
        cost = self.delivery_method.calculate_cost(weight_kg)
        days = self.delivery_method.estimate_days(distance_km)
        result = f"{self.delivery_method.method_name}: {cost:.2f} грн, {days} дн."
        self.journal.add_record(result)
        return result


def demo_task4():
    try:
        DeliveryMethod()
    except TypeError as exc:
        print("Абстрактний клас не можна створити:", type(exc).__name__)
    journal = DeliveryJournal()
    for method in (CourierDelivery(), PostalDelivery()):
        print(method.description())
        service = DeliveryService(method, journal)
        print("Замовлення:", service.create_order(2, 120))
    print("Журнал доставок:", journal.records)
    assert len(journal.records) == 2

if __name__ == "__main__":
    demo_task4()