class Loader:
    """
    Clase para cargar los datos limpios a un destino.
    """
    def __init__(self, df):
        self.df = df

    def to_csv(self, output_path="output/WorldCupPlayers_clean.csv"):
        """
        Guarda el DataFrame limpio en un archivo CSV.
        """
        try:
            self.df.to_csv(output_path, index=False, encoding="utf-8")
            print(f"✅ Datos guardados en {output_path}")
        except Exception as e:
            print(f"❌ Error al guardar datos: {e}")
