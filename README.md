# review-summarizer

## how to start the api locally:
- pull changes
- create new conda environment and pip install requirements.txt inside summarization_service module
````bash
# note python must be at most 3.6 or some packages wont install
conda create -n nlp_summ python=3.6
conda activate nlp_summ
pip install -r summarizer_service/requirements.txt
````

- once installed start the API by running this command: python api.py
- the endpoint that you will have to use to send POST requests is : 127.0.0.1:5000/summarize

## how to run the ui locally
- pull changes
- make a ui virtual env for the ui dependencies
````bash
virtualenv appui 
source appui/bin/activate
pip install -r ui/requirements.txt
````
- run the streamlit app
````
streamlit run ui/app.py
````
- it should automatically open on port 8501 and open in your default web browser
- then enter a reivew in the text box and hit the button "add review" and the model 
  will summarize what you typed and output its abstractive summary for comparison

## Build the docker images
Ensure you have docker installed on your system and open a terminal.
Navigate into `/summarizer_service` and run:
````bash
docker build -t summary_api .
docker run -it --rm --name summary_cont -p 5000:5000 summary_api
````

Navigate into `/ui` and run
````bash
docker build -t summary_ui .
docker run -it --rm --name summary_ui -p 8501:8501 summary_ui
# if running locally, open up your browser and navigate to localhost:8501
````

In order for the sumamrization to work, you must have both containers running when interacting with the ui.

# Get the images from dockerhub
The image is avaialble in my public dockerhub repo: chrisalert/nlp-ops-workhop:summary_api
````
docker pull chrisalert/nlp-ops-workshop:summary_api
docker pull chrisalert/nlp-ops-workshop:summary_ui
````
