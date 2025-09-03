# Transform/transformer.py
import pandas as pd

class Transformer:
    """
    Clase para limpiar y transformar los datos.
    """
    def __init__(self, df):
        self.df = df

    def clean(self):
        df = self.df.copy()

        # Eliminar filas sin nombre de jugador
        df = df.dropna(subset=["Player Name"])

        # Rellenar valores nulos numéricos
        num_cols = ["RoundID", "MatchID", "Shirt Number"]
        for col in num_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        # Rellenar valores nulos de texto
        text_cols = ["Team Initials", "Coach Name", "Player Name", "Position", "Event"]
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].fillna("Unknown").astype(str).str.strip()

        # Convertir "Line-up" a booleano
        if "Line-up" in df.columns:
            df["Line-up"] = df["Line-up"].astype(str).str.lower().map(
                {"1": True, "0": False, "yes": True, "no": False, "true": True, "false": False}
            )

        print(f"🔧 Datos transformados: {df.shape[0]} filas, {df.shape[1]} columnas")
        self.df = df
        return self.df
