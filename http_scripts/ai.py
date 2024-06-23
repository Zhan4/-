from openai import OpenAI
import time

# Replace with your OpenAI API key
api_key = 'nuh uh'
client = OpenAI(api_key=api_key)

# Replace with your fine-tuning job ID
fine_tune_id = 'ftjob-lskYn0u6emVErhz3Mx5S94qd'

# Function to retrieve the fine-tuning job status
def retrieve_fine_tune_status(client, fine_tune_id):
    response = client._request("GET", f"/v1/fine-tunes/{fine_tune_id}")
    return response

# Monitor the fine-tuning job
while True:
    response = retrieve_fine_tune_status(client, fine_tune_id)
    status = response['status']
    if status == 'succeeded':
        model_id = response['fine_tuned_model']
        print(f'Fine-tuning succeeded. Model ID: {model_id}')
        break
    elif status == 'failed':
        print('Fine-tuning failed.')
        break
    else:
        print(f'Status: {status}. Waiting for completion...')
        time.sleep(60)  # Wait for a minute before checking again