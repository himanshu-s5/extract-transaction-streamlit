import streamlit as st
import json 

st.title("Extract Transaction from json file")
def load_file():
    
    file_data = st.file_uploader('upload JSON file', type='json')
    if file_data:
        data = json.load(file_data)
        return data

def transaction_extract(data):
    
    bank = list(data.keys())[0]
    extracted_data = {
        bank:{
            "account":data[bank]['account'],
            "transactions":data[bank]['transactions']
        }
            }
    st.success('Extracted successfully')
    json_text = json.dumps(extracted_data, indent=4)
    st.text_area('Extracted json data', json_text, height=500)
    return extracted_data

file_data = load_file()

if file_data:
    
    if st.button('get transaction only'):
        trans_data = transaction_extract(file_data)
        
        
        if trans_data:
            json_data = json.dumps(trans_data)
            st.download_button(
                label="Download Transactions",
                data=json_data,
                file_name="transaction_file.json",
                mime="application/json"
            )

