from sqlalchemy import and_, insert, select
from sqlalchemy.orm import Session

from app.models import VisitedUrls


class VisitedUrlsRepo:
    """Класс для работы с запросами к модели VisitedUrls."""

    def __init__(self, session: Session):
        self.session = session
        self.model = VisitedUrls

    def add(self, data: list[dict]) -> None:
        """
        Запрос на добавление новых записей в базу данных.
        data - список словарей с данными о новых объектах.
        """
        self.session.execute(insert(self.model), data)

    def get(self, interval: dict = False) -> list:
        """
        Запрос на получение данных.
        interval - словарь с ключами 'from' и 'to', значения времнеи в
        секундах от начала эпохи. Фильтрует записи по этому промежутку.
        Возвращает список уникальных данных.
        """
        if interval:
            query = (
                select(self.model.url)
                .filter(
                    and_(
                        self.model.visited_at <= int(interval['to']),
                        self.model.visited_at >= int(interval['from']),
                    )
                )
                .distinct()
            )
        else:
            query = select(self.model.url).distinct()
        result = self.session.execute(query)
        return result.scalars().all()
