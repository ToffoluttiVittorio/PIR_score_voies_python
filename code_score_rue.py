import pandas as pd
import numpy as np
# from collections import Counter


# Attribution des poids au rues 
def poids(df):
    """
    Attribut des poids par rapport aux commerces, et ensuite attribut des scores aux voies 
    Parameters
    ----------
    df : TYPE : dataframe
        DESCRIPTION : open in the main, contains all the shops of Paris

    Returns
    -------
    dico_rue : TYPE : dictionnary 
        DESCRIPTION : contain all the names of the streets as the key and their score as the values 

    """
    poids_enseignes_sport = 4
    poids_boulevard = 1.2
    poids_place = 1.3
    rues = np.unique(df["VOIES"])
    dico_rue = {}
    for rue in rues:
        liste_rue = df["VOIES"].tolist()
        poids = liste_rue.count(rue)
        arr_indexes = np.where(np.asarray(liste_rue) == rue)
        for i in range(np.shape(arr_indexes)[1]):
            if "sport" in df["C20_LIBACT"][arr_indexes[0][i]]:
                poids += poids_enseignes_sport
        poids = poids/5
        if df["TYP_VOIE"][arr_indexes[0][i]] == "BD":
                poids = (poids*poids_boulevard)
        if df["TYP_VOIE"][arr_indexes[0][i]] == "PL":
                poids = (poids*poids_place)
        
        dico_rue.update({rue : poids})
                    

    return dico_rue

def assigner(df):
    """
    

    Parameters
    ----------
    df : TYPE dataframe 
        

    Returns
    -------
    df1 : TYPE dataframe 
        DESCRIPTION dataframe avec ajout d'une ligne qui prend le nom complet des voies '

    """
    df1 = df.assign(VOIES = df["TYP_VOIE"] + " " + df["LIB_VOIE"])
    
    return df1

if __name__ == "__main__":
    
    file_commerce = (r"commerce_paris.csv")
    df = pd.read_csv(file_commerce, sep = ';',encoding = "ISO-8859-1") 
    dfbis = assigner(df)
    
    
    dico = poids(dfbis)
    print("-----------------------------------------------\n                    FIN")

