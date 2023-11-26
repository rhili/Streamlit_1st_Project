# importing libraries
import pickle
import streamlit as st

# Loading the models
with open('./Financial_Inclusion_Model.pkl', 'rb') as f:
    inclusion_model = pickle.load(f)

with open('./FI_country_Encoder.pkl', 'rb') as ce:
    country_Encoder = pickle.load(ce)

with open('./FI_education_Encoder.pkl', 'rb') as ee:
    education_level_Encoder = pickle.load(ee)

with open('./FI_job_type_Encoder.pkl', 'rb') as jte:
    job_type_Encoder = pickle.load(jte)

with open('./FI_marital_status_Encoder.pkl', 'rb') as mse:
    marital_status_Encoder = pickle.load(mse)

with open('./FI_relationship_with_head_Encoder.pkl', 'rb') as rwhe:
    relationship_with_head_Encoder = pickle.load(rwhe)

# Setting a title to our app
st.title('Financial Inclusion Prediction Model')

# Getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    country = st.selectbox("Country :", ['Kenya', 'Rwanda', 'Tanzania', 'Uganda'])

with col2:
    year = st.number_input("Year :", min_value=2000, max_value=2023, step=1)

with col3:
    location_type = st.selectbox("Location Type :", ['Rural', 'Urban'])

with col1:
    cellphone_access = st.selectbox("Has Cellphone Access :", ['Yes', 'No'])

with col2:
    household_size = st.number_input("Household Size :", min_value=0, max_value=9, step=1)

with col3:
    age_of_respondent = st.number_input("Age :", min_value=20, max_value=85, step=1)

with col1:
    gender_of_respondent = st.selectbox("Gender :", ['Female', 'Male'])

with col2:
    relationship_with_head = st.selectbox("Relationship with Head :", ['Spouse', 'Head of Household', 'Other relative',
        'Child', 'Parent', 'Other non-relatives'])

with col3:
    marital_status = st.selectbox("Marital Status :", ['Married/Living together', 'Widowed', 'Single/Never Married',
        'Divorced/Seperated', 'Dont know'])

with col1:
    education_level = st.selectbox("Education Level :", ['Secondary education', 'No formal education',
        'Vocational/Specialised training', 'Primary education', 'Tertiary education', 'Other/Dont know/RTA'])

with col2:
    job_type = st.selectbox("Job Type :", ['Self employed', 'Government Dependent', 'Formally employed Private',
        'Informally employed', 'Formally employed Government', 'Farming and Fishing', 'Remittance Dependent',
        'Other Income', 'Dont Know/Refuse to answer', 'No Income'])

# Button to execute prediction code
if st.button('Submit'):

    country = country_Encoder.transform([[country]])[0]
    relationship_with_head = relationship_with_head_Encoder.transform([[relationship_with_head]])[0]
    marital_status = marital_status_Encoder.transform([[marital_status]])[0]
    education_level = education_level_Encoder.transform([[education_level]])[0]
    job_type = job_type_Encoder.transform([[job_type]])[0]

    if location_type == 'Urban':
        location_type = 0
    else:
        location_type = 1

    if cellphone_access == 'Yes':
        cellphone_access = 1
    else:
        cellphone_access = 0

    if gender_of_respondent == 'Male':
        gender_of_respondent = 0
    else:
        gender_of_respondent = 1

    inclusion_prediction = inclusion_model.predict([[country, year, location_type, cellphone_access,
        household_size, age_of_respondent, gender_of_respondent, relationship_with_head,
        marital_status, education_level, job_type]])

    if inclusion_prediction[0] == 1:
        st.success('This individual is most likely to have or use a bank account')
    else:
        st.error('This individual may not have nor use a bank account')