from abc import ABC, abstractmethod

class DeliveryFlyweight(ABC):
    @abstractmethod
    def deliver(self, name, number) -> None: pass   