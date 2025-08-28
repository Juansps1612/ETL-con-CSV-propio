# main.py

from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader



def main():
    print("🔹 Iniciando proceso ETL...")

    # 1. Extraer datos
    print("📥 Extrayendo datos...")
    extractor = Extractor(Config.INPUT_PATH)
    df = extractor.extract()

    if df is None:
        print("❌ No se pudieron extraer los datos. Finalizando proceso.")
        return

    # 2. Transformar datos
    print("🔧 Transformando datos...")
    transformer = Transformer(df)
    df_clean = transformer.clean()

    # 3. Cargar datos limpios
    print("💾 Guardando datos limpios...")
    # Genera el nuevo nombre del archivo con sufijo "_clean"
    output_file = Config.OUTPUT_PATH.replace(".csv", "_clean.csv")
    loader = Loader(df_clean)
    loader.to_csv(output_file)

    print("✅ Proceso ETL finalizado con éxito.")
    print(f"📂 Archivo limpio disponible en: {output_file}")


if __name__ == "__main__":
    main()