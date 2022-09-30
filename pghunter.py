#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

import warnings
warnings.filterwarnings("ignore")

# In[10]:


csv_file="pghunter_data_full.csv"


# In[11]:


def read_data(csv_file):
    df=pd.read_csv(csv_file)
    df.columns=[x.lower() for x in df.columns]
    df.columns=df.columns.str.replace(' ','_')
    return df


# In[34]:


def data_cleaning(df):
    df=df.dropna()
    df=df.drop_duplicates()
    title_df=df.title
    df=df.drop(['unnamed:_0','title','date_of_extraction'],axis='columns')
    
    df['rent']=df.rent.str.replace('₹','')
    df['rent']=df.rent.str.replace('Onwards','')
    df['rent']=df.rent.str.replace(',','')
    df['rent']=df.rent.str.replace('Sharing','')
    df['rent']=df.rent.str.replace('Twin','')
    df['rent']=df.rent.str.replace('Triple','')
    df['rent']=df.rent.str.replace('Single ','')
    df['rent']=df.rent.str.replace('Others ','')
    df['rent']=df['rent'].str.strip()
    
    dict1={"Food Included":2,"Food not Included":0,"Food Charge extra":1}
    df.food=df.food.replace(dict1)

    df.locality=df.locality.str.replace('in ','')
    df.locality=df.locality.str.strip()
    
    preferred=[]
    for i in range(df.shape[0]):
        if df.iloc[i,2]=="Professionals Preferred":
            preferred.append("Professionals")
        elif df.iloc[i,2]=="Student Preferred":
            preferred.append("Students")
        elif df.iloc[i,2]=="Competition Aspirants Preferred":
            preferred.append("Competitive Aspirants")
        else:
            preferred.append("Anyone")
    
    df['preferred']=preferred
    
    dict2={"Professionals Preferred":0,"Student Preferred":0,"Competition Aspirants Preferred":0}
    df.food=df.food.replace(dict2)
    
    # df=df.dropna()
    
    l1=lambda x:x[0:3]
    df['educational_instituiton']=df['educational_instituiton'].apply(l1)

    df['educational_instituiton']=df['educational_instituiton'].astype(float)

    df['office']=df['office'].apply(l1)
    df['office']=df['office'].astype(float)

    df['metro']=df['metro'].apply(l1)
    df['metro']=df['metro'].astype(float)
    
    return df,title_df


# In[35]:


def categorical(df):
    df=pd.get_dummies(df,columns=['preferred','occupancy_for'],drop_first=True)
    return df


# In[36]:


def splitting_and_modelling(df):
    Y=df['rent']
    X=df.drop(['rent'],axis='columns')

    from sklearn.model_selection import train_test_split
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.8,random_state=99)

    cat_columns=['city','locality']
    from catboost import CatBoostRegressor
    cbr=CatBoostRegressor()

    cbr.fit(X_train,Y_train,cat_features=cat_columns,silent=False,eval_set=(X_test,Y_test))
    return cbr


# In[37]:


def pickle_dump(cbr):
    pickle.dump(cbr, open('pghunter.pkl', 'wb'))


# In[38]:


def pg_predictor():
    df=read_data(csv_file)
    df=data_cleaning(df)
    df=categorical(df)
    cbr=splitting_and_modelling(df)
    pickle_dump(cbr)


# In[39]:

def get_full_data():
    df=read_data(csv_file)
    df,title_df=data_cleaning(df)
    return df,title_df


# pg_predictor()



# In[40]:


pickled_model=pickle.load(open('pghunter.pkl', 'rb'))


# In[ ]:




