# Config/config.py
class Config:
    """
    Configuración de rutas y parámetros para ETL.
    """
    INPUT_PATH = 'Extract/Files/WorldCupPlayers.csv'
    OUTPUT_PATH = 'Extract/Files/WorldCupPlayers_clean.csv'

    # Configuración de base de datos (SQLite para pruebas)
    DB_URL = 'sqlite:///WorldCupPlayers.db'  # cambiar según tu motor: postgresql, mysql, etc.
