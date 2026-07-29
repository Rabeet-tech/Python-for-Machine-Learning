#Excersice 1
job_roles = [
    {'role': 'Data Analyst', 'skills': ['Python', 'SQL', 'Excel']},
    {'role': 'Data Scientist', 'skills': ['Python', 'R', 'Machine Learning', 'Deep Learning']},
    {'role': 'Machine Learning Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn']},
    {'role': 'Data Engineer', 'skills': ['Python', 'Apache Spark', 'Hadoop', 'SQL']},
    {'role': 'Business Intelligence Analyst', 'skills': ['Python', 'SQL', 'Tableau', 'Power BI', 'Excel']},
    {'role': 'Quantitative Analyst', 'skills': ['R', 'Python', 'MATLAB', 'Statistics']},
    {'role': 'Operations Analyst', 'skills': ['Python', 'SQL', 'Data Visualization', 'Process Improvement']},
    {'role': 'Database Administrator', 'skills': ['SQL', 'Oracle', 'MySQL', 'Database Management']},
    {'role': 'AI Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Computer Vision']},
    {'role': 'Statistician', 'skills': ['R', 'SAS', 'Python', 'Statistical Modeling']}
]
# My skills
my_skills = ['Python', 'SQL', 'Excel']
can_apply=[]

for role in job_roles:
     isQual=True
     for skill in my_skills:
        if skill not in role['skills']:
            isQual=False
            break

     if isQual:
        can_apply.append(role['role'])

print(can_apply)
            

