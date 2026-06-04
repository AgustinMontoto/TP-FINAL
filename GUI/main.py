from pathlib import Path
from GUI.func.manejo_datos import leer_datos

def main():
    #input
    archivo=Path("data/medicion.csv")   #mejorar input
    carpeta_salida = Path("output/graficos")

    #proceso de datos
    df = leer_datos(archivo)



if __name__ == "__main__":
    main()
