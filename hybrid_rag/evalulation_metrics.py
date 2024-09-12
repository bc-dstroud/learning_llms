from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Answer Relevance (AR) Metric
def answer_relevance(generated_answer, original_question):
    # Generate question embeddings
    question_embedding = embeddings.embed_query(original_question)
    generated_question_embedding = embeddings.embed_query(generated_answer)

    # Cosine similarity between original question and generated answer
    similarity = cosine_similarity([question_embedding], [generated_question_embedding])

    return similarity[0][0]
