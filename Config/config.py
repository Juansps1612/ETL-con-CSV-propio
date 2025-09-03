# Config/config.py
class Config:
    """
    Configuración de rutas y parámetros para ETL.
    """
<<<<<<< HEAD
    INPUT_PATH = 'Extract/Files/WorldCupPlayers.csv'
    OUTPUT_PATH = 'Extract/Files/WorldCupPlayers_clean.csv'

    # Configuración de base de datos (SQLite para pruebas)
    DB_URL = 'sqlite:///WorldCupPlayers.db'  # cambiar según tu motor: postgresql, mysql, etc.
=======
    INPUT_PATH = '/workspaces/ETLProject/Extract/Files/ncr_ride_bookings.csv'
    SQLITE_DB_PATH = '/workspaces/ETLProject/Extract/Files/etl_data.db'
    SQLITE_TABLE = 'ride_bookings_clean'
>>>>>>> 3f74f7204df74673c86322cce9b9f48f0702a2d4
