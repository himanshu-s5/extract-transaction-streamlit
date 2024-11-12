import streamlit as st
import json 

def load_file():
    
    file_data = st.file_uploader('upload JSON file', type='json')
    if file_data is not None:
        data = json.load(file_data)
        return data

def transaction_extract(data):
    
    trans_data = []
    for bank, bank_data in data.items():
    
        transactions = bank_data.get('transactions', [])
        trans_data.extend(transactions)
        st.success('Extracted successfully')
    
    return trans_data

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
            