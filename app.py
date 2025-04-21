import streamlit as st
import pandas as pd
import numpy as np
from pyresparser import ResumeParser
import spacy
import nltk
nltk.download('stopwords')


# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_details_from_resume(resume_file):
    data = ResumeParser(resume_file).get_extracted_data()
    return data

def compute_similarity(details, user_doc):
    if type(details) != str:
        return 0.0
    detail_doc = nlp(details)
    return detail_doc.similarity(user_doc)

def recommend_internships(user_details, user_skills, q_table, dataset):
    if user_details is None:
      user_details = ''
    user_doc = nlp(user_details)

    df = pd.read_csv(dataset)
    df['similarity'] = df['details'].apply(lambda x: compute_similarity(x, user_doc))

    num_jobs = len(df)
    Q = np.load(q_table)

    recommended_jobs = np.argsort(Q[0])[-3:][::-1]

    recommendations = []
    for job_idx in recommended_jobs:
        recommendations.append({
            'Job ID': df.iloc[job_idx]['id'],
            'Job Title': df.iloc[job_idx]['job_title'],
            'Similarity': df.iloc[job_idx]['similarity'],
            'Skills': df.iloc[job_idx]['skills']
        })

    return recommendations

def main():
    st.title("Internship Recommendation System")

    st.header("Upload Your Resume")

    uploaded_file = st.file_uploader("Upload your resume (PDF format only)", type="pdf")
    if uploaded_file:
        st.write("Processing your resume...")

        # Extract resume details using ResumeParser
        data = extract_details_from_resume(uploaded_file)

        # Prepare user details and skills
        user_skills = data.get('skills', [])
        user_deets = data.get('designation', [])
        user_details = ' '.join([str(elem) for elem in user_deets])
        user_details += ' for ' + str(data.get('total_experience', 0)) + ' years at ' + ' '.join([str(elem) for elem in data.get('company_names', [])])

        st.write("### Resume Details Extracted")
        # st.write(data)

        q_table = 'q_table.npy'
        dataset = '/content/recomm_df.csv'  # Adjust the path as needed
        recommendations = recommend_internships(user_details, user_skills, q_table, dataset)

        st.write("### Recommended Internships:")
        for rec in recommendations:
            st.write(f"**Job ID:** {rec['Job ID']}")
            st.write(f"**Job Title:** {rec['Job Title']}")
            st.write(f"**Similarity:** {rec['Similarity']:.2f}")
            st.write(f"**Skills:** {rec['Skills']}")
            st.write("---")

if __name__ == "__main__":
    main()
