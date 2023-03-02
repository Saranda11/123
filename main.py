import sqlite3

conn = sqlite3.connect('bookstore.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              author TEXT,
              genre TEXT,
              price REAL,
              quantity INTEGER)''')

conn.commit()

import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('bookstore.db')

st.title('Sarandas bookshop')

menu = ['View Inventory', 'Add Book', 'Update Book', 'Delete Book', 'Filter Inventory', 'Calculate Total Value']
choice = st.sidebar.selectbox('Select an action', menu)

if choice == 'View Inventory':
    st.subheader('View Inventory')
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['ID', 'Title', 'Author', 'Genre', 'Price', 'Quantity'])
    st.dataframe(df)

elif choice == 'Add Book':
    st.subheader('Add Book')
    title = st.text_input('Title')
    author = st.text_input('Author')
    genre = st.text_input('Genre')
    price = st.number_input('Price')
    quantity = st.number_input('Quantity', min_value=1)
    if st.button('Add'):
        c = conn.cursor()
        c.execute('INSERT INTO books (title, author, genre, price, quantity) VALUES (?, ?, ?, ?, ?)', (title, author, genre, price, quantity))
        conn.commit()
        st.success('Book has been added to the inventory')

elif choice == 'Update Book':
    st.subheader('Update Book')
    id = st.number_input('Enter the ID of the book you want to update', min_value=1)
    c = conn.cursor()
    c.execute('SELECT * FROM books WHERE id=?', (id,))
    data = c.fetchall()
    if not data:
        st.warning('Book not found')
    else:
        book = data[0]
        title = st.text_input('Title', book[1])
        author = st.text_input('Author', book[2])
        genre = st.text_input('Genre', book[3])
        price = st.number_input('Price', book[4])
        quantity = st.number_input('Quantity', book[5])
        if st.button('Update'):
            c.execute('UPDATE books SET title=?, author=?, genre=?, price=?, quantity=? WHERE id=?', (title, author, genre, price, quantity, id))
            conn.commit()
            st.success('Book has been updated')

elif choice == 'Delete Book':
    st.subheader('Delete Book')
    id = st.number_input('Enter the ID of the book you want to delete', min_value=1)
    if st.button('Delete'):
        c = conn.cursor()
        c
