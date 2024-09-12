def hybrid_rag(query):
    # Retrieve from VectorRAG
    vector_results = qa_chain_vector.run(query)

    # Retrieve from GraphRAG (querying knowledge graph)
    graph_context = search_kg(query)

    # Combine both contexts
    combined_context = vector_results["result"] + str(graph_context)

    # Feed combined context into the LLM for answer generation
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Answer the following query using both the text and the graph: {combined_context}",
        max_tokens=150,
    )

    return response["choices"][0]["text"]
