# main.py

# main.py
from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader
from sqlalchemy import create_engine

def main():
    print("🔹 Iniciando proceso ETL...")

    # 1️⃣ Extraer
    extractor = Extractor(Config.INPUT_PATH)
    df = extractor.extract()
    if df is None:
        print("❌ Falló la extracción. Finalizando.")
        return

    # 2️⃣ Transformar
    transformer = Transformer(df)
    df_clean = transformer.clean()

    # 3️⃣ Cargar
    loader = Loader(df_clean)

    # a) Guardar CSV
    loader.to_csv(Config.OUTPUT_PATH)

    # b) Guardar en SQL
    engine = create_engine(Config.DB_URL)
    loader.to_sql(engine, table_name="world_cup_players", if_exists='replace')

    print("✅ ETL finalizado con éxito.")

if __name__ == "__main__":
    main()
