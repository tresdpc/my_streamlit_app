import streamlit as st
import requests

st.title("Crypto Price Notifier")

crypto_symbol = st.text_input("Enter cryptocurrency symbol (e.g., BTC):").upper()
fiat_currency = st.text_input("Enter fiat currency (e.g., EUR):").upper()
threshold = st.number_input("Enter price threshold:", min_value=0.0, format="%.2f")

if st.button("Notify me"):

    if not crypto_symbol or not fiat_currency:
        st.warning("Please enter both cryptocurrency and fiat currency.")
    else:
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": "YOUR_API_KEY_HERE"
        }
        params = {
            "symbol": crypto_symbol,
            "convert": fiat_currency
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        try:
            price = data["data"][crypto_symbol]["quote"][fiat_currency]["price"]
            price_formatted = f"{price:,.2f}"
            threshold_formatted = f"{threshold:,.2f}"
            st.success(f"The current price of {crypto_symbol} is {price_formatted} {fiat_currency}.")
            st.info(f"We will notify you when the price reaches {threshold_formatted} {fiat_currency}.")
        except KeyError:
            st.error("Invalid symbol or fiat currency. Please check your input.")
