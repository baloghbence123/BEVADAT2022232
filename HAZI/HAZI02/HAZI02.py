# %%
import numpy as np

# %%
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# %%
# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

# %%
def column_swap(input_arr):
    return np.flip(input_arr, axis=1)

# %%
# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

# %%
def compare_two_array(input_array1, input_array2):
    if (len(input_array1) == len(input_array2)):
        return np.where(input_array1 == input_array2)[0].astype(int)
    else:
        return np.array([])


# %%
# Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!, 

# %%
def get_array_shape(input_array):
    if input_array.ndim == 1:
        outstring = f"sor: 1, oszlop: {input_array.shape[0]}, melyseg: 1"
        return outstring
    elif input_array.ndim == 2:
        outstring = f"sor: {input_array.shape[0]}, oszlop: {input_array.shape[1]}, melyseg: 1"
        return outstring
    elif input_array.ndim == 3:
        outstring = f"sor: {input_array.shape[1]}, oszlop: {input_array.shape[2]}, melyseg: {input_array.shape[0]}"
        return outstring


# %%
# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

# %%
def encode_Y(input_array, classNumber):
    return np.squeeze(np.eye(classNumber,dtype=int)[input_array.reshape(-1)])



# %%
# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

# %%
def decode_Y(input_matrix):
    return np.argmax(input_matrix,axis=1)


# %%
# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy
# listát és egy array-t és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()

# %%
def eval_classification(input_list,input_array):
    return input_list[np.argmax(input_array)]

# %%
# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()

# %%
def replace_odd_numbers(input_array):
    input_array = np.where(input_array%2 == 1,-1, input_array)
    return input_array


# %%
# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja,
# attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()

# %%
def replace_by_value(input_array,input_value):
    input_array[input_array < input_value]=-1
    input_array[input_array >= input_value]=1
    return input_array

# %%
# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza

# %%
def array_multi(input_array):
    return np.prod(input_array)

# %%
# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza 
# és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()

# %%
def array_multi_2d(input_array):
    return np.prod(input_array,axis=1)

# %%
# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal.
# Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()


# %%
def add_border(input_array):
    return np.pad(input_array, pad_width=1, mode='constant', constant_values=0)

# %%
# A KÖTVETKEZŐ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!

# %%
# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot
# és ezt adja vissza egy numpy array-ben. A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()

# %%
def list_days(fromdate,todate):
    return np.arange(fromdate, todate, dtype='datetime64[D]')

# %%
# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD.
# Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24


# %%
def get_act_date():
    return np.datetime64('now','D')

# %%
# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta.
# Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()

# %%
def sec_from_1970():
    startTime = np.datetime64('1970-01-01T00:02:00')
    now = np.datetime64('now')
    return (now - startTime).astype(int)


