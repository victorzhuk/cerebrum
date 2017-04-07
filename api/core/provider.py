from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """Abstract devices provider."""

    @abstractmethod
    def send_request(self, address, action, payload):
        pass
