from intermediate_level.laboratory12 import DiscountPrice, PricingService, RegularPrice


class FakeProvider:
    def get_base_price(self, product_name: str) -> float:
        return 100.0


def test_regular_price():
    service = PricingService(FakeProvider(), RegularPrice())
    assert service.get_final_price("any") == 100.0


def test_discount_price():
    service = PricingService(FakeProvider(), DiscountPrice(0.2))
    assert service.get_final_price("any") == 80.0
