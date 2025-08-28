import pandas as pd

class Transformer:
    """
    Clase para transformar y limpiar los datos de WorldCupPlayers.csv
    """
    def __init__(self, df):
        self.df = df

    def clean(self):
        """
        Realiza limpieza y transformación de los datos.
        Adaptado a columnas del dataset WorldCupPlayers.csv
        """
        df = self.df.copy()

        # --- 1. Eliminar filas sin nombre de jugador ---
        df = df.dropna(subset=["Player Name"])

        # --- 2. Rellenar valores nulos ---
        num_cols = ["RoundID", "MatchID", "Shirt Number"]
        for col in num_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        text_cols = ["Team Initials", "Coach Name", "Player Name", "Position", "Event"]
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].fillna("Unknown").astype(str).str.strip()

        # --- 3. Convertir "Line-up" a booleano (titular/suplente) ---
        if "Line-up" in df.columns:
            df["Line-up"] = df["Line-up"].astype(str).str.lower().map(
                {"1": True, "0": False, "yes": True, "no": False,
                 "true": True, "false": False}
            )

        print(f"✅ Datos transformados (WorldCupPlayers): {df.shape[0]} filas, {df.shape[1]} columnas")
        self.df = df
        return self.df
