import pandas as pd
import matplotlib.pyplot as plt

# TODO : 1. Initial Data Inspection
file = pd.read_csv('ai_job_market_insights.csv', sep = "\t")
print(file.info())
print(file.head(10))








#TODO : 2. Data Cleaning Tasks
clean_data = file.copy()
categorical_colms = [
    'Job_Title', 'Industry', 'Company_Size', 'Location','AI_Adoption_Level','Automation_Risk','Remote_Friendly'
]

for col in categorical_colms:
    clean_data[col] = clean_data[col].astype('category')

clean_data.columns = clean_data.columns.str.lower().str.replace('_', ' ')
clean_data.info()
print(clean_data.head(10))








# Cleaning data: step one - Using isnull() method
null_mask = file.isnull()
null_count = null_mask.sum()
#print("Number of Nulls: ",null_count)

total_isnull_count = null_mask.sum().sum()
#print("Total Nulls:",total_isnull_count)











#  Step Three : Double-Checking data if there is no missing value
empyt_count = (clean_data == '').sum()
na_counts = (clean_data == 'N/A').sum()
unknown_counts = (clean_data == 'Unknown').sum()
summary = pd.DataFrame({
    'empty_count': empyt_count,
    'N/A': na_counts,
    'Unknown': unknown_counts
})
#print(summary)








# TODO: 3. Find Job Title & Location & Salary USD
job_salary = clean_data[['job title','location','salary usd',]]
round_salary = job_salary['salary usd'].round(0)
data = pd.DataFrame({
    'Job Title' : job_salary['job title'],
    'Location' : job_salary['location'],
    'Salary USD' : round_salary
})

print(data)

data_sct_job = data[data['Job Title'] == 'Data Scientist']
data_sct_job = data_sct_job.sort_values(by='Salary USD',ascending=False)
print(data_sct_job.head(5))









#TODO: 4. Create Visaul Graph For Data Scientiest

top_job_for_data_sct = data_sct_job.loc[
    data_sct_job.groupby('Location', observed=True)['Salary USD'].idxmax()
    ]
top_job_for_data_sct = top_job_for_data_sct[['Job Title','Location','Salary USD']]
top_job_for_data_sct = top_job_for_data_sct.sort_values(by='Salary USD',ascending=True)
#print(top_job_for_data_sct)

colors = ['#87CEFA', '#00BFFF', '#1E90FF', '#4169E1', '#0000FF', '#0000CD', '#00008B', '#000080', '#191970', '#000066']

plt.figure(figsize=(8, 6))
bars = plt.bar(top_job_for_data_sct['Location'], top_job_for_data_sct['Salary USD'], color=colors)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1500, f"${int(height):,}",ha='center',va='bottom',  fontsize=9)

plt.xlabel('City', fontsize=12)
plt.ylabel('Salary ($)', fontsize=12)
plt.title('Data Scientist Salaries by Country', fontsize=14, fontweight='bold')

plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.savefig("data_scientist_salaries.png")




