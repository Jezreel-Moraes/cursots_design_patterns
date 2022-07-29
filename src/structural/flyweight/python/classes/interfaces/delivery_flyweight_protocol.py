from abc import ABC, abstractmethod


class DeliveryFlyweightProtocol(ABC):
    @abstractmethod
    def deliver(self, name: str, number: str) -> None: pass
