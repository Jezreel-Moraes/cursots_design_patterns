from abc import ABCMeta, abstractmethod


class ValidationsProtocol(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def is_email(self, email: str) -> bool: pass
