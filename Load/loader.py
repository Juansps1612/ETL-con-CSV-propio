# Load/loader.py
import pandas as pd

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
            print(f"❌ Error al guardar CSV: {e}")

    def to_sql(self, engine, table_name="world_cup_players", if_exists='replace'):
        try:
            self.df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
            print(f"💾 Datos cargados en la tabla '{table_name}' de la base de datos")
        except Exception as e:
            print(f"❌ Error al cargar datos a la base de datos: {e}")
