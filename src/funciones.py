import re

def title(x):
    x=x.lower()
    if 'analyst' in x or 'analytics' in x:
        return 'Data Analyst'
    elif 'engineer' in x or 'architect' in x or 'etl' in x:
        return 'Data Engineer'
    elif 'machine' in x or '3d' in x or 'ai' in x:
        return 'Machine Learning Engineer'
    elif 'science' in x or 'scientist' in x or 'head of data' in x or 'data specialist' in x:
        return 'Data Scientist'
    else:
        return x

   