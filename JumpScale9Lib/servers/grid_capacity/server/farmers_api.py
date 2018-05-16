# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

from flask import Blueprint
from . import handlers


farmers_api = Blueprint('farmers_api', __name__)


@farmers_api.route('/api/farmers', methods=['GET'])
def ListFarmers():
    """
    List Farmers
    It is handler for GET /api/farmers
    """
    return handlers.ListFarmersHandler()


@farmers_api.route('/api/farmer_create', methods=['GET'])
def RegisterFarmer():
    """
    Register a farmer
    It is handler for GET /api/farmer_create
    """
    return handlers.RegisterFarmerHandler()
