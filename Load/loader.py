<<<<<<< HEAD
# Load/loader.py
import pandas as pd
=======

from Config.config import Config
import sqlite3
>>>>>>> 3f74f7204df74673c86322cce9b9f48f0702a2d4

class Loader:
    """
    Clase para cargar datos a CSV o SQL.
    """
    def __init__(self, df):
        self.df = df

    def to_csv(self, output_path="output/WorldCupPlayers_clean.csv"):
        try:
            self.df.to_csv(output_path, index=False, encoding="utf-8")
            print(f"💾 Datos guardados en CSV: {output_path}")
        except Exception as e:
<<<<<<< HEAD
            print(f"❌ Error al guardar CSV: {e}")

    def to_sql(self, engine, table_name="world_cup_players", if_exists='replace'):
        try:
            self.df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
            print(f"💾 Datos cargados en la tabla '{table_name}' de la base de datos")
        except Exception as e:
            print(f"❌ Error al cargar datos a la base de datos: {e}")
=======
            print(f"Error al guardar datos: {e}")

    def to_sqlite(self, db_path=None, table_name=None):
        """
        Guarda el DataFrame limpio en una base de datos SQLite.
        """
        db_path = db_path or Config.SQLITE_DB_PATH
        table_name = table_name or Config.SQLITE_TABLE
        try:
            conn = sqlite3.connect(db_path)
            self.df.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.close()
            print(f"Datos guardados en la base de datos SQLite: {db_path}, tabla: {table_name}")
        except Exception as e:
            print(f"Error al guardar en SQLite: {e}")
>>>>>>> 3f74f7204df74673c86322cce9b9f48f0702a2d4
