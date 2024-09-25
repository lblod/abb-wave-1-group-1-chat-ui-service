import logging
import os
from abc import ABC, abstractmethod

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



class DAO(ABC):

    def __init__(self):
        self.db_host = os.environ.get("DB_HOST", 'http://localhost:90')

    @abstractmethod
    def get(self, designation_id: str) -> str:
        pass


class MockedHeritageDontDAO(DAO):

    def get(self, designation_id: str) -> str:
        return '''
        You are not allowed to:
        - repaint your windows
        - change the facade
        - change the gutter
    '''


class LODDAO(DAO):

    def get(self, designation_id='14969'):
        annotations = requests.get(
            f'{self.db_host}/annotations?filter[:exact:resource]=https://id.erfgoed.net/aanduidingsobjecten/{designation_id}').json()
                
        logger.info(annotations)

        annotations = annotations.get('data', [])

        return [{'rule': annotation['attributes']['body'], 'resource': annotation['attributes']['resource']} for
                annotation in annotations]


'''
PREFIX oa: <http://www.w3.org/ns/oa#>

SELECT ?content
WHERE {
    ?node oa:hasBody ?content .
    ?node oa:hasTarget <https://id.erfgoed.net/aanduidingsobjecten/14969> .
}

'''

'''
PREFIX oa: <http://www.w3.org/ns/oa#>

SELECT ?content
WHERE {
    ?node oa:hasBody ?content .
    ?node oa:hasTarget ?BESLUIT .
    
    FILTER(?BESLUIT == <https://id.erfgoed.net/aanduidingsobjecten/14969>)
}

'''
