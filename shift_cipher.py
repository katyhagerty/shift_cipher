#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:46:35 2022

@author: katyhagerty

TO DO:
    [] Error message if phrase contains numbers or spaces
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.title('Shift Cipher')
st.write("""
Use the option below to set your parameters for:
- Phrase to decode
- Number of letters to shift phrase by
""")
st.write('---')

# st.image('data/doge.jpg', use_column_width=True)
# st.write("[Photo by Minh Pham](https://unsplash.com/@minhphamdesign?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)")
# #Photo by <a href="https://unsplash.com/@minhphamdesign?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Minh Pham</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
 
# Inputs
st.header('Inputs')
phrase = st.text_input("Phrase: ")
shift_dir = st.selectbox("Shift direction: ", ('Forward', 'Backward'))
shift_no = st.number_input("Shift Amount: ", min_value=1, max_value=999999999)

import string

def shift(phrase, shift_dir, shift_no):
    phrase = phrase.lower()
    # if shift_no >= 26:
    #     shift_no = shift_no % 26
    
    answer = ''
    letter_to_no = {}
    no_to_letter = {}
    
    for no, letter in enumerate(string.ascii_lowercase):
        letter_to_no[letter] = no
        no_to_letter[no] = letter
    
    for i in phrase:
        if i == ' ': 
            sub = i
            
        else:
            ind = letter_to_no[i]
            if shift_dir == 'Forward':
                shift_ind = ind + shift_no
                sub = no_to_letter[shift_ind % 26]
                
            elif shift_dir == 'Backward':
                shift_ind = ind - shift_no
                sub = no_to_letter[shift_ind % 26]
            
        answer = answer + sub
    
    return answer
        
# doge_historic = round(doge_historic, 5)
answer = shift(phrase, shift_dir, shift_no)

st.write('''# Results''')
# st.write('''## Historic Analysis''')
# st.write("You would have originally bought: ***{:,.2f}*** $DOGE".format(round((ORG_USD/doge_historic),5)))
# st.write("At a price of ***{:,.9f}*** per $DOGE".format(doge_historic))
st.write(f'Decoded Phrase: {answer}')

# st.write('''## Present Effects''')
# total_doge = ORG_USD/doge_historic
# current_USD = total_doge * doge_current
# perc_change = (current_USD - ORG_USD)/(ORG_USD)*100
# usd_diff = current_USD - ORG_USD

# st.write("That is currently worth: ***${:,.2f}***".format(round(current_USD,2)))
# st.write("Which is a percentage change of ***{:,.2f}%***".format(round(perc_change, 2),))

# if usd_diff == 0:
#    st.write('''# You Broke Even''')
# elif usd_diff <= 0:
#    st.write('''# You Would Have Lost''')
# else:
#    st.write('''# You Missed Out On''') 
# st.write('***${:,.2f}!!!***'.format(abs(round(usd_diff,2)),))

# now = datetime.now()
# historical_prices = cg.get_coin_market_chart_range_by_id(id='dogecoin', vs_currency="usd", from_timestamp=HIST_DATE_datetime.timestamp(), to_timestamp=now.timestamp())['prices']

# dates = []
# prices = []

# for x,y in historical_prices:
#   dates.append(x)
#   prices.append(y)

# dictionary = {"Prices":prices, "Dates":dates}
# df = pd.DataFrame(dictionary)
# df['Dates'] = pd.to_datetime(df['Dates'],unit='ms',origin='unix')

# st.line_chart(df.rename(columns={"Dates":"index"}).set_index("index"))
# st.write("Please consider donating some of that sweet $DOGE to the wallet address below:")
# st.write("DGVqvZW43P5yLkdZfddaPfibZcBtSxa52A")