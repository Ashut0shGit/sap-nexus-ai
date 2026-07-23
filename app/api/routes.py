from app.models.sap_object import SAPObject
from app.models.transport import Transport
from app.services import transport_service
from app.services import object_service
from fastapi import APIRouter

from app.core.config import settings

from app.services.transport_service import TransportService

from app.services.object_service import ObjectService

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": settings.environment,
    }


@router.get("/version")
def version():
    return {
        "app": settings.app_name,
        "version": settings.app_version,
    }

transport_service = TransportService()

@router.get("/change-request/{cr_number}",
response_model = list[Transport],
)
def get_transport(cr_number: str):
    return transport_service.get_transports(cr_number)  

object_service = ObjectService()

@router.get(
    "/transport/{transport_number}/objects",
    response_model= list[SAPObject]
)
def get_objects(transport_number: str):
    return object_service.get_objects(transport_number)