import statsapi
import tkinter as tk
from tkinter import *

def build_transactions_frame(team_id, main_window, start_date, end_date):
    
    frame = tk.Frame(main_window, bg='#ffffff', bd=5, relief=SOLID, width=100, height=600)

    # Display transactions title
    title_label = tk.Label(frame, text='Transactions', font=('Calibri', 16), bg='white')
    title_label.pack(pady=5)

    transactions = statsapi.get('transactions', {'teamId': team_id, 'startDate': start_date, 'endDate': end_date})
    transactions_list = transactions['transactions']

    for transaction in transactions_list:
        date = transaction.get('date', '')
        description = transaction.get('description', '')
        transaction_info = f'{date} - {description}'
        transaction_label = tk.Label(frame, text=transaction_info, font=('Calibri', 10), bg='white', justify='left', width=50)
        transaction_label.pack(anchor='e', pady=2)

    return frame