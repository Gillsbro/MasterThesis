# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:56:02 2017

@author: Mattias
"""
import pandas as pd
import csv
import numpy as np

#Loading data
data = pd.read_csv('thesis_dataset_incomplete.csv')
sorted_by_id = data.sort_values(by='PatientIDNumber')

#Sorting patients 
patient383 = sorted_by_id.loc[sorted_by_id['PatientIDNumber']== 383]
sorted_patient383 = patient383.sort_values(by='TreatmentStart')
sorted_patient383.index = range(len(sorted_patient383))

#Plotting LitersProcessed for one patient
sorted_patient383['LitersProcessed'].plot()

# Sorting patients using groupby
sorted_by_group = data.groupby([data['PatientIDNumber'],data['TreatmentStart']])