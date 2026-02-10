from typing import Dict, Protocol


# Strategy Pattern
class PricingStrategy(Protocol):
    def calculate(self, base_price: float) -> float: ...


class RegularPrice:
    def calculate(self, base_price: float) -> float:
        return base_price


class DiscountPrice:
    def __init__(self, discount: float):
        self.discount = discount

    def calculate(self, base_price: float) -> float:
        return base_price * (1 - self.discount)


# External provide(simulated)


class ExternalPriceService:
    def get_price(self, product_name: str) -> float:
        print(f"Fetching price for {product_name} from external service...")
        prices = {
            "ligthstick": 1800.0,
            "candle lighthstick": 350.0,
        }
        return prices.get(product_name, 1000.0)


# Adapter Pattern
class PriceProvider(Protocol):
    def get_base_price(self, product_name: str) -> float: ...


class ExternalPriceAdapter:
    def __init__(self, external_service: ExternalPriceService):
        self.external_service = external_service

    def get_base_price(self, product_name: str) -> float:
        return self.external_service.get_price(product_name)


# Decorator Patterns (cache)
class CachedPriceProvider:
    def __init__(self, wrapped: PriceProvider):
        self.wrapped = wrapped
        self.cache: Dict[str, float] = {}

    def get_base_price(self, product_name: str) -> float:
        if product_name not in self.cache:
            print("Cache miss")
            self.cache[product_name] = self.wrapped.get_base_price(product_name)
        else:
            print("Cache hit")
        return self.cache[product_name]


# Service using everything
class PricingService:
    def __init__(self, provider: PriceProvider, strategy: PricingStrategy):
        self.provider = provider
        self.strategy = strategy

    def get_final_price(self, product_name: str) -> float:
        base_price = self.provider.get_base_price(product_name)
        return self.strategy.calculate(base_price)


# Demo
if __name__ == "__main__":
    external = ExternalPriceService()
    adapter = ExternalPriceAdapter(external)
    cached_provider = CachedPriceProvider(adapter)

    strategy = DiscountPrice(0.10)
    service = PricingService(cached_provider, strategy)

    print(service.get_final_price("ligthstick"))
    print(service.get_final_price("ligthstick"))
