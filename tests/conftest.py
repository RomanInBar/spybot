import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).parents[1]))

from app.models import Base
from database.config import DBSettings
from database.engine import engine

settings = DBSettings()


@pytest.fixture(scope='session', autouse=True)
def setup_db():
    assert settings.MODE == 'TEST'
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
