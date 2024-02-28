import requests
import streamlit as st

api_key = ''

def openai_request(prompt):
    headers = {'Authorization': f'Bearer {api_key}'}
    response = request.post(
        'https://api.openai.com/v1/images/generations',
        headers = headers,
        json= {
            'prompt' : prompt,
            'model' : 'dall-e-3',
            'size' : '1024x1024',
            'quality' : 'standard',
            'n' : 1
        }
    )
    if response.status_code != 200:
        raise Exception(response.json())
    else:
        image_url = response.json()['data'][0]['url']
    return image_url

def download_image(url,filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

#configure the page
st.set_page_config(page_title="AI image Generator", layout="centered")

#create a streamlit app
st.title("AI image Generator")
description = st.text_area("Prompt")

if st.button("Generate image"):
    with st.spinner("Generating your image..."):
        url= openai_request(description)
        filename = "AI_images/image_generator.png"
        download_image(url,filename)
        st.image(filename, use_column_width=True)
        with open(filename, "rb") as f:
            image_data = f.read()
        download = st.download_button(label="Download Image", data=image_data, file_name="image_generated.jpg",)
