from abc import ABC, abstractmethod

class DAO(ABC):
    
    @abstractmethod
    def get(self, heritage_id: str) -> str:
        pass
    
    
class MockedHeritageDontDAO(DAO):
    
    def get(self, heritage_id: str) -> str:
        return '''
        You are not allowed to:
        - repaint your windows
        - change the facade
        - change the gutter
    '''