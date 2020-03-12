from dependency_injector import providers, containers
from Vin import vin  
from vehicle import Vehicle

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')
    # other configs
    
class Clients(containers.DeclarativeContainer):
    Vin = providers.Singleton(vin, Configs.config)
    # other clients
    
class Readers(containers.DeclarativeContainer):
    vehicle = providers.Factory(Vehicle)
    # other readers




