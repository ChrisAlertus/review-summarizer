# review-summarizer

how to start the api locally:
- pull changes
- create new conda environment and pip install requirements.txt inside summarization_service module
````bash
# note python must be at most 3.6 or some packages wont install
conda create -n nlp_summ python=3.6
````

- once installed start the API by running this command: python api.py
- the endpoint that you will have to use to send POST requests is : 127.0.0.1:5000/summarize

# How to run the ui locally
- pull changes
- make a ui virtual env for the ui dependencies
````bash
virtual env appui 
pip install -r ui/requirements.txt
````
- run the streamlit app
````
streamlit run ui/app.py
````
- it should automatically open on port 8501 and open in your default web browser
- then enter a reivew in the text box and hit the button "add review" and the model 
  will summarize what you typed and output its abstractive summary for comparison
