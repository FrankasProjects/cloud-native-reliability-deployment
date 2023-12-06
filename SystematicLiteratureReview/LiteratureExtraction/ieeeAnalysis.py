import pandas as pd
from pathlib import Path

# IEEE Xplore results
df_ieee = pd.read_csv('IEEE/InitialExport/export.csv')

# ACM results
df_acm_1 = pd.read_csv('ACM/jour_1.csv')
df_acm_2 = pd.read_csv('ACM/proc_1.csv')
df_acm_3 = pd.read_csv('ACM/proc_2.csv')

df_acm_all = pd.concat([df_acm_1, df_acm_2, df_acm_3])

#SpringerLink
# 1 (cost analysis, cloud computing)
df_springer_1_1 = pd.read_csv('SpringerLink/springer_1_1.csv')
df_springer_1_2 = pd.read_csv('SpringerLink/springer_1_2.csv')
df_springer_1_3 = pd.read_csv('SpringerLink/springer_1_3.csv')


df_springer_1= pd.concat([df_springer_1_1,df_springer_1_2,df_springer_1_3])


# 2 (cost analysis, cloud-native)
df_springer_2_1 = pd.read_csv('SpringerLink/springer_2_1.csv')
df_springer_2_2 = pd.read_csv('SpringerLink/springer_2_2.csv')

df_springer_2 = pd.concat([df_springer_2_1,df_springer_2_2])


# 3 (pricing model, cloud computing)
df_springer_3_1 = pd.read_csv('SpringerLink/springer_3_1.csv')
df_springer_3_2 = pd.read_csv('SpringerLink/springer_3_2.csv')
df_springer_3_3 = pd.read_csv('SpringerLink/springer_3_3.csv')

df_springer_3 = pd.concat([df_springer_3_1,df_springer_3_2, df_springer_3_3])

# 4 (pricing scheme, cloud computing)
df_springer_4_1 = pd.read_csv('SpringerLink/springer_4_1.csv')
df_springer_4_2 = pd.read_csv('SpringerLink/springer_4_2.csv')
df_springer_4_3 = pd.read_csv('SpringerLink/springer_4_3.csv')

df_springer_4 = pd.concat([df_springer_4_1,df_springer_4_2, df_springer_4_3])

df_springer_all = pd.concat([df_springer_1,df_springer_2,df_springer_3,df_springer_4])

#combine all data sets

df_literature = pd.concat([df_ieee,df_acm_all, df_springer_all])

#generate DOI column

df_literature['DOI'].fillna(df_literature['Item DOI'], inplace=True)

#export csv
filepath = Path('LiteratureExtraction/literature_unfiltered.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df_literature.to_csv(filepath)

#remove duplicates (based on DOI)

df_cleaned = df_literature[(~df_literature.duplicated(['DOI'])) | (df_literature['DOI'].isnull())]
df_duplicates = df_literature[(df_literature.duplicated(['DOI'])) & (~df_literature['DOI'].isnull())]


#export csv
filepath = Path('LiteratureExtraction/literature_removed_dupes.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df_cleaned.to_csv(filepath)

#build a clean dataset for further scanning

df_scan = df_cleaned[['Document Title', 'Title', 'Item Title', 'Authors', 'Publication Title', 'Publication Year', 'DOI', 'PDF Link', 'URLs', 'URL']]

#merge duplicate columns
df_scan['Document Title'].fillna(df_scan['Title'], inplace=True)
df_scan['Document Title'].fillna(df_scan['Item Title'], inplace=True)

df_scan['PDF Link'].fillna(df_scan['URLs'], inplace=True)
df_scan['PDF Link'].fillna(df_scan['URL'], inplace=True)

df_prepared = df_scan[['Document Title', 'Authors', 'Publication Title', 'Publication Year', 'DOI', 'PDF Link']]

#export prepared dataset
filepath = Path('LiteratureExtraction/Title Scan/prepared_literature.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df_prepared.to_csv(filepath)

#filter for same title: to detect fraction of conference to journal extension

df_title_scan = pd.read_excel('LiteratureExtraction/Title Scan/result.xlsx')
# manually removed duplicates based on titles: looked for possible journal extensions / missing DOIs
df_dup_scan = df_title_scan[(df_title_scan.duplicated(['Document Title'])) & (~df_title_scan['Document Title'].isnull())]


