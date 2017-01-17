# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:47:00 2017

@author: Erik
"""

import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv('thesis_dataset_incomplete.csv')

data.TreatmentStart=pd.to_datetime(data.TreatmentStart)

# sort data according to PatientIDNumber 
sorted_data = data.sort_values(by=['PatientIDNumber', 'TreatmentStart'])

plt.plot(pd.to_datetime(sorted_patient1.TreatmentStart),sorted_patient1['LitersProcessed'],'*-')

# Use group-by to sort by patient and date
from itertools import groupby
result = data.groupby('PatientIDNumber').groups
#%%
grouped = data.groupby(['PatientIDNumber'])
for patientID, sub in grouped:
    print(patientID, max(sub['TreatmentStart']))
    
    if patientID > 400:
        break
    