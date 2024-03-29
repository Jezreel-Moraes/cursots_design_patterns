from abc import ABC, abstractmethod


class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str: pass

    @abstractmethod
    def get_date(self) -> str: pass
