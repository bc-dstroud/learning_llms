# HybridRAG Implementation

This repository contains the Python implementation of **HybridRAG**, a hybrid approach combining Vector-based and Graph-based Retrieval Augmented Generation (RAG) techniques for efficient information extraction, especially in the context of financial documents.

## Overview

HybridRAG integrates both **VectorRAG** and **GraphRAG** to enhance the performance of question-answering (Q&A) systems by leveraging the power of both vector databases and knowledge graphs. This approach provides more accurate and contextually relevant answers to user queries compared to traditional methods.

### Key Features

- **VectorRAG:** Uses a vector database for document chunk retrieval based on semantic similarity.
- **GraphRAG:** Leverages a knowledge graph to retrieve structured relationships (subject, predicate, object) relevant to the query.
- **Hybrid Approach:** Combines the strengths of both methods to improve answer accuracy and relevance.

### Implementation Details

The implementation is based on the methodology described in the paper [HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction](https://arxiv.org/pdf/2408.04948).

### How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/davestroud/cloud_logs.git
