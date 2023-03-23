# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%


def csv_to_df(path):
    df_data = pd.read_csv(path)
    return df_data

df = pd.read_csv("StudentsPerformance.csv")


# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
def capitalize_columns(df_data):
    newDf = df_data.copy()
    for col in newDf:
        if col.find("e") == -1:
            tmp = col.upper()
            newDf.rename(columns={col:tmp},inplace=True)
    return newDf


# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''


# %%
def math_passed_count(df_data):
    newDf = df_data.copy()
    ctr = len(newDf[newDf['math score'] >= 50])
    return ctr

math_passed_count(df)

# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat),
akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
def did_pre_course(df_data):
    newDf=df_data.copy()
    ret = newDf[newDf['test preparation course']!='none']
    return ret

did_pre_course(df)

# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
def average_scores(df_data):
    newDf = df_data.copy()
    return newDf.groupby('parental level of education').aggregate({'math score':'mean','reading score':'mean',
                                                                   'writing score':'mean'})
average_scores(df)

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal,
töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
def add_age(df_data):
    newDf=df_data.copy()
    np.random.seed(42)
    age = np.random.randint(18, 66, size=len(newDf))    
    newDf['age']=age
    return newDf

add_age(df)

# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
def female_top_score(df_data):
    newDf = df_data.copy()
    column_names = ['math score', 'reading score', 'writing score']
    retval = newDf[newDf[column_names].sum(axis=1) == newDf[column_names].sum(axis=1).max()]
    tmp = retval[retval['gender']=='female'].iloc[0]
    ki = (tmp['math score'],tmp['reading score'],tmp['writing score'])
    return ki

female_top_score(df)

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%


def add_grade(df_data):
    newDf = df_data.copy()
    grade = (newDf['math score']+newDf['reading score']+newDf['writing score'])/300    
    newDf['grade'] = pd.cut(grade,
                     bins = [0, 0.61,0.71,0.81,0.91,1.],
                     right=False,
                     labels=['F','D','C','B','A'])
    
    return newDf
add_grade(df)

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%


def math_bar_plot(df_data):
    newDf = df_data.copy()
    arr = newDf.groupby("gender", group_keys=False)['math score'].mean()
    fig = arr.plot(kind='bar', title='Average Math Score by Gender',ylabel='Math Score', xlabel='Gender', figsize=(5, 5))

    return fig

print(math_bar_plot(df))

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
def writing_hist(df_data):
    newDf = df_data.copy()
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=False)

    newDf.hist(column='writing score',ax=axes)
    plt.suptitle('Distribution of Writing Scores', x=0.5, y=1.05, ha='center', fontsize='xx-large')
    fig.text(0.5, 0.04, 'Writing Score', ha='center')
    fig.text(0.04, 0.5, 'Number of Students', va='center', rotation='vertical')
    
    

    return fig
    
writing_hist(df)

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''


# %%
def ethnicity_pie_chart(df_data):
    newDf = df_data.copy()
    groupped = newDf.groupby('race/ethnicity')['race/ethnicity'].count()
    plot = groupped.plot.pie(y='race/ethnicity',title='Proportion of Students by Race/Ethnicity',autopct='%1.1f%%', figsize=(5, 5))
    return plot
    
ethnicity_pie_chart(df)



