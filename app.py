import streamlit as st

# Initialize data in session state
if "data" not in st.session_state:
    st.session_state.data = [
        {"id": 1, "name": "Item 1", "description": "This is item 1"},
        {"id": 2, "name": "Item 2", "description": "This is item 2"}
    ]

# Streamlit App
st.title("Simple REST API with Streamlit")

# Display all items
st.header("All Items")
if st.button("Show All Items"):
    st.json(st.session_state.data)

# Add a new item
st.header("Add a New Item")
with st.form("Add Item"):
    new_name = st.text_input("Name")
    new_description = st.text_input("Description")
    submitted = st.form_submit_button("Add Item")
    if submitted:
        new_item = {
            "id": len(st.session_state.data) + 1,
            "name": new_name,
            "description": new_description
        }
        st.session_state.data.append(new_item)
        st.success(f"Added: {new_item}")

# Get an item by ID
st.header("Get Item by ID")
item_id = st.number_input("Enter Item ID", min_value=1, step=1)
if st.button("Get Item"):
    item = next((item for item in st.session_state.data if item['id'] == item_id), None)
    if item:
        st.json(item)
    else:
        st.error("Item not found!")

# Update an item
st.header("Update an Item")
with st.form("Update Item"):
    update_id = st.number_input("ID to Update", min_value=1, step=1, key="update_id")
    update_name = st.text_input("New Name", key="update_name")
    update_description = st.text_input("New Description", key="update_description")
    update_submitted = st.form_submit_button("Update Item")
    if update_submitted:
        item = next((item for item in st.session_state.data if item['id'] == update_id), None)
        if item:
            item['name'] = update_name
            item['description'] = update_description
            st.success(f"Updated: {item}")
        else:
            st.error("Item not found!")

# Delete an item
st.header("Delete an Item")
delete_id = st.number_input("ID to Delete", min_value=1, step=1, key="delete_id")
if st.button("Delete Item"):
    st.session_state.data = [item for item in st.session_state.data if item['id'] != delete_id]
    st.success(f"Deleted item with ID: {delete_id}")
