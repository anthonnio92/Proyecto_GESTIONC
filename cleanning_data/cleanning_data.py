import pandas as pd
import glob
import os
from pathlib import Path

current_path_dir = Path(__file__).parent.parent
files_path = current_path_dir / "entrenamiento_IA_parte_*.csv"

todos_archivos = glob.glob(str(files_path))

lista_archivos = []
for f in todos_archivos:
    data = pd.read_csv(f)
    nombre = os.path.basename(f)
    data['source_file'] = nombre
    lista_archivos.append(data)

df = pd.concat(lista_archivos)
df.replace('0000-00-00', '1900-01-01', inplace=True)
df['fecha_entrega'] = pd.to_datetime(df['fecha_entrega'], errors='coerce')
df['fecha_ultima'] = pd.to_datetime(df['fecha_ultima'], errors='coerce')
df['fecha_penultima'] = pd.to_datetime(df['fecha_penultima'], errors='coerce')
df['fecha_antepenultima'] = pd.to_datetime(df['fecha_antepenultima'], errors='coerce')
