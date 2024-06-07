import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
from tasks.task_5.task_5 import ChromaCollectionCreator

if __name__ == "__main__":
    # Configuration for EmbeddingClient
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "my-project-425208",
        "location": "us-central1"
    }
    
    screen = st.empty() # Screen 1, ingest documents
    with screen.container():
        st.header("Quizzify")
        # Initalize DocumentProcessor and Ingest Documents
        processor = DocumentProcessor()
        processor.ingest_documents()
        # Initalize the EmbeddingClient
        embed_client = EmbeddingClient(**embed_config)
        # Initialize the ChromaCollectionCreator
        chroma_creator = ChromaCollectionCreator(processor, embed_client)

        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            # Use streamlit widgets to capture the user's input
            topic_input = st.text_input("Enter the quiz topic")
            # for the quiz topic and the desired number of questions
            num_questions = st.slider("Select the number of questions", 1, 10)
            document = None
            submitted = st.form_submit_button("Generate a Quiz!")
            if submitted:
                # Use the create_chroma_collection() method to create a Chroma collection from the processed documents
                chroma_creator.create_chroma_collection()
                # Uncomment the following lines to test the query_chroma_collection() method
                document = chroma_creator.query_chroma_collection(topic_input) 
                
    if document:
        screen.empty() # Screen 2
        with st.container():
            st.header("Query Chroma for Topic, top Document: ")
            st.write(document)