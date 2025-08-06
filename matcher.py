from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_jobs(resume_text, job_list):
    documents = [job['description'] for job in job_list] + [resume_text]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    resume_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(resume_vector, job_vectors)[0]

    for i, score in enumerate(similarities):
        job_list[i]['score'] = round(score * 100, 2)

    top_matches = sorted(job_list, key=lambda x: x['score'], reverse=True)[:3]

    return top_matches
