#!/usr/bin/env python
# coding: utf-8

# # Part1 : Exploration de données avec Pandas

# In[10]:


import pandas as pd
import ydata_profiling as pp

#Lire fichier covid_19
Covid_df = pd.read_csv('covid_19_data.csv')

#Avoir les informations
Covid_df.info()

#Voir l'en-tête de la dataset
Covid_df.head()

#Valeur manquant du datset
Covid_df.isnull()

#Description des information sur la data set
Covid_df.describe()


# In[2]:


#Avoir les informations
Covid_df.info()


# In[4]:


#Voir l'en-tête de la dataset
Covid_df.head()


# In[5]:


#Valeur manquant du datset
Covid_df.isnull()


# In[6]:


#Description des information sur la data set
Covid_df.describe()


# # Part2 : Exploration de données avec Pandas profiling

# In[ ]:


import pandas as pd
import ydata_profiling as pp

#Lire fichier covid_19
Covid_df = pd.read_csv('covid_19_data.csv')

#Generer un profiling report
profile = pp.ProfileReport(Covid_df, title='Pandas Profiling Report')

# Display the report
profile.to_notebook_iframe()


# In[7]:


#Lire fichier covid_19
Covid_df = pd.read_csv('covid_19_data.csv')


# In[8]:


#Generer un profiling report
profile = pp.ProfileReport(Covid_df, title='Pandas Profiling Report')


# In[12]:


# Display the report
#profile.to_notebook_iframe()
profile.to_file("MyCovid_report.html")


# # Résumé sur le rapport du pandas profiling
# 
# ### A l'issue de l'analyse des données sur le Covid_19 de plusieur pays du monde 
# 
# 1. Nous remarquons que la dataset contient 8 variables avec un total de 306429 observations et un pourcentage de 3,2% de valeur manquante dans la dataset.
# 
# 2. Au niveaux des observationn On note une evolution croissante de la covid_19 en fonction du temps et atteint un pic constant à partir de septembre 2020 jusqu'en Mai 2021 avec la RUSSIE au classement mondiale des pays les plus touché par le Covid_19. Ci-desssous les 10 premiers pays lkes plus touché par le covid_19  entre Janvier 2020 et Mai 2021:
# - Russie
# - USA
# - Japan
# - China
# - Mainland
# - India
# - Colombie
# - Mexique
# - Brasil
# - Ukraine
# 
# 3. La dataset comporte des valeurs manquante et on observe qu'il y a moins de valeur manquante au niveau de la variable Country/Region qu'au niveau des autres variables.
# 
# 4. Il y a une forte correlation entre le [nombre de cas confirmé et le nombre de cas guéris],[Nombre de deces et nombre de cas confirmé] et [Nobre de cas guéris et nombre de cas confirmé]. Mais nous ne pouvons par affirmer qu'il existe une relation cause et effet entre ces deux variable car bien n'ayant une forte correlation elle ne sont pas lier.
# 

# In[ ]:




