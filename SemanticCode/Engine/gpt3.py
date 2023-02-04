import requests
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

# Define the API endpoint and your OpenAI API key
api_endpoint = "https://api.openai.com/v1/engines/gpt-3/jobs"
file = args.file

# Define the model and text input
model = "code-davinci-002"
with open(file) as f:
    data = f.read()
code = precompile(data)
# Define the headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

# Define the request body
data = {
    "model": model,
    "prompt": prompt,
    "temperature": 0.1,
    "max_tokens": 200,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": ["\n"],
}

# Make the API request
response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    # Extract the generated text from the response
    generated_text = response.json()["choices"][0]["text"]
    print(generated_text)
else:
    # Handle the error
    print("Error: " + response.text)
