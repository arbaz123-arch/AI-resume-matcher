# job_dataset_loader.py
import csv
def load_jobs(file_path="jobs.csv"):
    jobs = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                job = {
                    "job_id": int(row["job_id"]),
                    "title": row["title"].strip(),
                    "description": row["description"].lower().strip()
                }
                jobs.append(job)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return jobs

# Sample test
if __name__ == "__main__":
    job_list = load_jobs()
    for job in job_list:
        print(f"Job ID: {job['job_id']}, Title: {job['title']}")
        print(f"Description: {job['description']}\n")
