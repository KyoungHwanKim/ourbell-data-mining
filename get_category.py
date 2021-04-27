# -*- conding: utf-8 -*-
import time
import pandas as pd

pd.set_option('display.max_columns', None)

# CSV -> pandas Dataframe
csv = pd.read_csv('./소상공인시장진흥공단_상가(상권)정보_서울_202012.csv', sep='|')
#print(csv.head())
print(csv.head())
print(csv.isnull().sum(axis = 0))
'''
l_category, m_category, s_category = set(), set(), set()

for idx, rows in csv.iterrows():
    #print(rows['상권업종대분류명'])
    l_category.add(rows['상권업종대분류명'])
    m_category.add(rows['상권업종중분류명'])
    s_category.add(rows['상권업종소분류명'])

print(l_category)
print(m_category)
print(s_category)
'''