import streamlit as st
from function_wa import save_to_do, read_todo_from_file


def add_todo():
    new_to_do = st.session_state["todo_input"]
    print(new_to_do)
    to_do_list.append(new_to_do)
    save_to_do(FILEPATH2, to_do_list=to_do_list)


FILEPATH2 = "todo_wa.txt"

to_do_list = []

to_do_list = read_todo_from_file(filepath=FILEPATH2)

st.title("My To Do App")
st.subheader("This is my todo app")
st.text("Increase yor productivity")

for index, todo in enumerate(to_do_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        to_do_list.pop(index)
        save_to_do(FILEPATH2, to_do_list=to_do_list)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(
    label="input todo",
    placeholder="Enter a todo...",
    on_change=add_todo,
    key="todo_input",
    label_visibility="hidden",
)
