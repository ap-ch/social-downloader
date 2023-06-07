import yaml
from fastapi import APIRouter, Security
from fastapi.exceptions import HTTPException
from security import manager


router = APIRouter(prefix="/services")


@router.get("/", status_code=200)
def info(user=Security(manager, scopes=["auth"])):
    services = {}
    with open('services.yml', 'r') as services_file:
        services = yaml.safe_load(services_file)
    return services
