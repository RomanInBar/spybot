from sqlalchemy.orm import Mapped, mapped_column

from database.engine import Base


class VisitedUrls(Base):
    __tablename__ = 'visited_urls'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(nullable=False)
    visited_at: Mapped[int] = mapped_column(nullable=False)
