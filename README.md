# Coffee Shop Dashboard App

A modern interactive coffee shop dashboard built with Python and Streamlit. This app allows users to browse coffee menu options, add items to the cart, and check out. It features a user-friendly interface with session management and a simple cart system.

---

## Features
- **Browse Coffee Menu**: Select from various coffee types with detailed information.
- **Order Management**: Add, view, and remove items from your order.
- **Real-Time Dashboard**: View metrics like the number of items in the cart, total cost, and orders confirmed.
- **Customizable Preferences**: Select coffee strength preferences from the sidebar.
- **Clear/Reset Cart**: Option to clear or reset the cart.

---

## Technologies Used
- **Backend**: Python (OOP concepts for Coffee & Order management)
- **Frontend**: Streamlit (for creating the interactive dashboard)
- **Session State**: Used to manage order state between user interactions.

---

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/coffee-shop-dashboard.git

   Navigate to the project directory:

2. cd coffee-shop-dashboard


3. Install required packages:

4. pip install -r requirements.txt


5. Run the app:

6. streamlit run app.py


Your app should now be live at https://coffeeapp-saikoushik.streamlit.app/.

File Structure
coffee-shop-dashboard/
├── app.py                # Main Streamlit application file
├── main.py               # Contains Coffee and Order classes
├── requirements.txt      # Dependencies file
└── README.md             # This file

Code Explanation

main.py: Contains two main classes:

Coffee: Represents each coffee item with a name and price.

Order: Handles the order, allowing items to be added, removed, and the total price to be calculated.

app.py: The Streamlit frontend, where users can interact with the coffee menu, select items, view their cart, and check out.

Session State: The order is stored in the Streamlit session state, allowing it to persist throughout interactions.

Contributing

Feel free to fork the repository and submit pull requests if you have any improvements or new features in mind!
