# Extract/extractor.py
import pandas as pd

class Extractor:
    """
    Clase para extraer datos de archivos CSV.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        try:
            df = pd.read_csv(self.file_path)
            print(f"📥 Datos extraídos: {df.shape[0]} filas, {df.shape[1]} columnas")
            return df
        except Exception as e:
            print(f"❌ Error al extraer datos: {e}")
            return None

