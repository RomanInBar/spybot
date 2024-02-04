from time import time
from typing import Union

from app.schemas import AddUrls, GetUrls


class VisitedUrlsServices:
    def __init__(self, repository):
        self.repo = repository

    def add(self, data: AddUrls) -> str:
        """Добавляет новые данные в модель."""
        links = data.model_dump().get('links')
        data_for_model = [
            {'url': link, 'visited_at': int(time())} for link in links
        ]
        try:
            self.repo.add(data_for_model)
            self.repo.session.commit()
            return {'status': 'ok'}
        except Exception as error:
            return {'status': str(error)}
        finally:
            self.repo.session.close()

    def get(self, interval: dict = False) -> Union[list, str]:
        """Возвращает уникальные данные модели."""
        try:
            objects = self.repo.get(interval)
            response = {'domains': objects, 'status': 'ok'}
            return GetUrls.model_validate(response, from_attributes=True)
        except Exception as error:
            return {'status': str(error)}
        finally:
            self.repo.session.close()
