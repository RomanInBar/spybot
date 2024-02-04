from app.repository import VisitedUrlsRepo
from app.services import VisitedUrlsServices
from database.engine import session


def get_service():
    service = VisitedUrlsServices(VisitedUrlsRepo(session()))
    return service
