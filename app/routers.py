from typing import Union

from fastapi import APIRouter, Depends, Request

from app.depends import VisitedUrlsServices, get_service
from app.descriptions import AIPDescriptions
from app.schemas import AddUrls, GetUrls

router = APIRouter(
    prefix='/urls',
    tags=['Urls'],
)
description = AIPDescriptions()


@router.get(
    '/visited_domains',
    response_model=Union[GetUrls, dict[str, str]],
    summary='Получить данные о посещенных сайтах',
    description=description.visited_domains,
)
def get(request: Request, service: VisitedUrlsServices = Depends(get_service)):
    params = request.query_params
    try:
        interval = {'from': params['from'], 'to': params['to']}
    except KeyError:
        interval = None
    finally:
        response = service.get(interval)
    return response


@router.post(
    '/visited_links',
    response_model=dict[str, str],
    summary='Запись новых объектов.',
    description=description.visited_links,
)
def create(data: AddUrls, service: VisitedUrlsServices = Depends(get_service)):
    response = service.add(data)
    return response
