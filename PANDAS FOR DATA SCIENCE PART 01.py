#!/usr/bin/env python
# coding: utf-8

# ### M.FAHAD FAROOQ

# # PANDAS FOR DATA SCIENCE 

# ## HOW TO INSTALL

# In[1]:


pip install pandas


# ## SERIES

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


labels=['a','b','c','d','e']
data=[1,2,3,4,5]
arr=np.array(data)
dic={'a':10,'b':20,'c':30,'d':40,'e':50}


# In[5]:


pd.Series(data)


# In[6]:


pd.Series(data=data,index=labels)


# ### OR

# In[7]:


pd.Series(data,labels)


# In[8]:


pd.Series(arr,labels)


# In[9]:


pd.Series(dic)


# In[10]:


pd.Series(labels,data)


# ### ser1=pd.Series(data,index)

# In[11]:


ser1=pd.Series([1,2,3,4,5],['USA','PAKISTAN','GERMANY','CHINA','USSR'])


# In[12]:


ser2=pd.Series([1,3,4,5,6],['USA','INDIA','PAKISTAN','GERMANY','CHINA'])


# In[13]:


ser2['PAKISTAN']


# In[14]:


ser1['PAKISTAN']


# In[15]:


ser3=pd.Series(['USA','INDIA','PAKISTAN','GERMANY','CHINA'],[1,2,3,4,5])


# In[16]:


ser3[3]


# In[17]:


ser1+ser2


# In[18]:


ser1*ser2


# ## DATA FRAMES 

# In[19]:


import numpy as  np
import pandas as pd


# In[20]:


from numpy.random import randn


# In[21]:


df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['U','V','W','X'])


# In[22]:


df


# In[23]:


df[['U','X']]                               # TO GRAB ANY COLOUMN 


# #### TO ADD NEW COLOUMN  

# In[24]:


df['Y']=df['U']+df['X']


# In[25]:


df


# #### TO REMOVE ANY COLOUMN 

# #### drop('Coloumn Name ',axis=1)  OR  drop('Row Name',axis=0)

# In[26]:


df.drop('Y',axis=1)


# In[27]:


df


# #### If you want to permanantly delete it so df.drop('coloumn name',axis=1,inplace=True) OR df.drop('row name',axis=0,inplace=True)

# In[28]:


df.drop('Y',axis=1,inplace=True)


# In[29]:


df


# In[30]:


df.loc['A']                   # TO GRAB ANY ROW 


# In[31]:


df.loc[['A','E']]


# In[32]:


df.loc['A','X']                      # TO GRAB ANY SPECIFIC VALUE df.loc('Row','Coloumn ')


# In[33]:


# WE CAN ALSO DO THIS THING AS WELL

df.loc[['A','E'],['W','X']]            # df.loc[['row','row'],['coloumn','coloumn']]


# In[34]:


df


# In[35]:


df>0                #IT WILL GIVE BOOLEAN DATA 


# In[36]:


booldf=df>0


# In[37]:


df[booldf]        #NOW IT WILL GIVE HE VALUE WHCIH ARE TRUE


# In[38]:


df


# In[39]:


df['W']>0                              # TO CHECK ANY COLOUMN 


# In[40]:


df[df['W']>0]


# In[41]:


df.loc['E']>0                       #TO CHECK ANY ROW 


# In[42]:


df.loc['E']>0


# In[43]:


# FOR MULTIPLE CONDITIONS  AND

df[(df['W']<0) & (df['X']<1)]


# In[44]:


# FOR MULTIPLE CONDITIONS  OR

df[(df['W']<0) | (df['X']<1)]


# In[45]:


df


# ### TO SET & RESET INDEX 

# In[46]:


df.reset_index()


# In[47]:


df.set_index('X')


# In[48]:


df


# # Multi-Index and Index Hierarchy
# 
# Let us go over how to work with Multi-Index, first we'll create a quick example of what a Multi-Indexed DataFrame would look like:

# In[49]:


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[50]:


hier_index


# In[51]:


df=pd.DataFrame(np.random.rand(6,2),hier_index,['A','B'])


# In[52]:


df


# In[53]:


df.index.names


# In[54]:


df.index.names=['GROUPS','NUMBERS']


# In[57]:


df


# In[55]:


df.loc['G1'].loc[3].loc['B']


# In[56]:


df.loc['G2'].loc[3].loc["A"]


# ## CROSS-SECTION FUNC 

# In[58]:


df.xs(1,level='NUMBERS')


# In[ ]:




