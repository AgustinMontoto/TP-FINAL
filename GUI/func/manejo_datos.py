import panda as pd

def leer_datos(archivo, skiprows=2, header=None, sep=","):    #formato(columnas): tiempo(0), CH1(1), CH2(2), ..., CHn(n) ; Por defecto lee arch csv del TP final
    try:
        df = pd.read_csv(archivo, skiprows=skiprows, header=header, sep=sep)
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
    return df

    
    