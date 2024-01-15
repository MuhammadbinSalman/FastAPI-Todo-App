# streamlit_client.py

import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App")

def create_todo():
    title = st.text_input("Enter Todo Title")
    # description = st.text_area("Enter Todo Description")
    if st.button("Add Todo"):
        response = requests.post(f"{BASE_URL}/todos/", json={"db": title})
        if response.status_code == 200:
            st.success("Todo added successfully")
            st.success(f"{response.json()}")
def delete_todo():
    todo_id = st.number_input("Enter Todo ID to delete")
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            st.success("Todo deleted successfully")

if __name__ == "__main__":
    create_todo()
    delete_todo()



    
# import streamlit as st

# page_title= "Todo-App"
# page_icon= ":clipboard:"
# layout= "centered"
# st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

# if "user_tasks" not in st.session_state:
#     st.session_state["user_tasks"] = []
# st.title(f'Todo app assignment {page_icon}')
# task = st.text_input('Enter your todo task')

# if st.button('Add Todo'):   #make a button in streamlit
#     if task:
#         st.success('Task added successfully')
#         st.session_state['user_tasks'].append(task) 
#     else:
#         st.warning('Please enter a task')
# for i, t in enumerate(st.session_state['user_tasks']):
#     st.text(f"{i+1}. {t}")
#     if st.button(f"Delete {t}", key=(i+2)):
#         st.session_state['user_tasks'].remove(t)

