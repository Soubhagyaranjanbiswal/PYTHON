#!/usr/bin/env python
# coding: utf-8

# # BODY MASS INDEX CALCULATOR

# In[5]:


name=str(input("enter your name"))
body_weight_in_kg=int(input("enter a body weight"))
height=int(input("enter in inches"))
body_weight_in_pounds=body_weight_in_kg*2.02
BMI=(body_weight_in_pounds*703)/(height**2)
print("Your BMI is",BMI)
if( BMI<=18.5):
    print(name,"you are underweight.")
elif(BMI<=24.9):
    print(name,"you are normalweight.you dont have to worry about")
elif( BMI<=29.9):
    print(name,"you are overweight.stop eating junks and start working out")
else:
    print(name,"you are overwight, workout regularly, dont sit much.follow a clean diet")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




