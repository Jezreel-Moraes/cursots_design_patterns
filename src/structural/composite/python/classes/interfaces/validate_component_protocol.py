from abc import ABCMeta, abstractmethod


class ValidationComponentProtocol(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, value) -> bool: pass

    def add(self, *args) -> None: pass
