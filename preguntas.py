"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():

    Filas = len(tbl0)
    return Filas


def pregunta_02():

    Columnas = len(list(tbl0.axes[1]))
    return Columnas


def pregunta_03():

    Recuento = tbl0.groupby('_c1').count()
    Recuento = Recuento['_c0']
    return Recuento


def pregunta_04():
    
    Promedio = tbl0.groupby('_c1').mean()
    Promedio = Promedio['_c2']
    return Promedio


def pregunta_05():

    Maximo = tbl0.groupby('_c1').max()
    Maximo = Maximo['_c2']
    return Maximo


def pregunta_06():

    Lista_Ordenada = tbl1['_c4'].tolist()
    Lista_Ordenada = sorted(list(set(Lista_Ordenada)))
    Lista_Ordenada = [z.upper() for z in Lista_Ordenada]
    return Lista_Ordenada


def pregunta_07():

    Suma = tbl0.groupby('_c1').sum()
    Suma = Suma['_c2']
    return Suma


def pregunta_08():
    
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    return tbl0


def pregunta_09():
    
    Datos = tbl0['_c3'].str.split('-', expand = True)
    Datos.columns = ['year', 'month', 'day']
    tbl0['year'] = Datos.year
    return tbl0


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    return


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    return


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    return


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    return
