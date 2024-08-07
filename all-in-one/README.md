# LangChain All-In-One Demo
A multi-page Streamlit app showcasing generative AI uses cases with LangChain, OpenAI, and others.

[LangChain](https://langchain.readthedocs.io/en/latest) is an open-source framework created to aid the development of applications leveraging the power of large language models (LLMs). It can be used for chatbots, text summarisation, data generation, code understanding, question answering, evaluation, and more 🔥

*Provide the API keys in Settings, and select a use case from the sidebar to get started.*

#### Web Search
* A sample app for web search queries using LangChain and Serper API.
* References: Blog | [Source Code](https://github.com/alphasecio/langchain-examples/blob/main/search) | [Python Notebook](https://github.com/alphasecio/langchain-examples/blob/main/search/langchain_search.ipynb)
* *Note: The all-in-one search app has been modified to use Serper API instead of SerpApi.*

#### URL Summary
* A sample app for summarizing URL content using LangChain and OpenAI.
* References: [Blog](https://alphasec.io/blinkist-for-urls-with-langchain-and-openai) | [Source Code](https://github.com/alphasecio/langchain-examples/blob/main/url-summary)

#### Text Summary
* A sample app for summarizing text using LangChain and OpenAI.
* References: [Blog](https://alphasec.io/summarize-text-with-langchain-and-openai) | [Source Code](https://github.com/alphasecio/langchain-examples/blob/main/text-summary) | [Python Notebook](https://github.com/alphasecio/langchain-examples/blob/main/text-summary/langchain_text_summarizer.ipynb)

#### Document Summary
* A sample app for summarizing documents using LangChain and Chroma.
* References: [Blog](https://alphasec.io/summarize-documents-with-langchain-and-chroma) | [Source Code](https://github.com/alphasecio/langchain-examples/blob/main/chroma-summary) | [Python Notebook](https://github.com/alphasecio/langchain-examples/blob/main/chroma-summary/langchain_doc_summarizer.ipynb)

#### News Summary
* A sample app for Google news search and summaries using LangChain and Serper API.
* References: [Blog](https://alphasec.io/summarize-google-news-results-with-langchain-and-serper-api) | [Source Code](https://github.com/alphasecio/langchain-examples/blob/main/news-summary)

#### Settings
* [OpenAI API Key](https://platform.openai.com/account/api-keys) | [Serper API Key](https://serper.dev/api-key)


# Setup
cd to this folder  
run `python -m venv venv` 
run `source venv/bin/activate`  
run `python -m pip install --upgrade pip`  
run `pip install -r requirements.txt`  
run `rm .env`   
run `echo "OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>" >> .env`  
run `echo "SERPER_API_KEY=<YOUR_SERPER_API_KEY>" >> .env`  
run `streamlit run Home.py`  
enter `ctrl-c` to quit  


