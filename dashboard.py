import streamlit as st
from main import Coffee, Order   # main.py has your Coffee & Order classes

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="☕ Coffee Shop Dashboard",
    page_icon="☕",
    layout="wide"
)

# Optional: simple custom background + font
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;        /* Pure white background */
    }
    h1, h2, h3 {
        color: black;                   /* Dark blue text */
        font-family: "Segoe UI", sans-serif;
    }
    .coffee-card {
        padding: 0.8rem 1rem;
        border-radius: 0.8rem;
        background-color: green;        /* Light grey/blue card */
        border: 1px solid #d0d7e2;
        box-shadow: 0 2px 4px rgba(0,0,0,0.06);
        margin-bottom: 0.6rem;
    }
    .stMetric {
        background-color: orange;
        border-radius: 0.8rem;
        padding: 0.4rem 0.6rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------- SESSION STATE ----------
if "order" not in st.session_state:
    st.session_state.order = Order()
if "order_count" not in st.session_state:
    st.session_state.order_count = 0

order = st.session_state.order

# ---------- MENU DATA ----------
@st.cache_data
def get_menu():
    return [
        Coffee("Espresso", 2.50),
        Coffee("Cappuccino", 3.50),
        Coffee("Latte", 4.00),
        Coffee("Mocha", 4.50)
    ]

menu = get_menu()

# ---------- SIDEBAR ----------
st.sidebar.title("☕ Coffee Controls")
st.sidebar.markdown("Customize your order and view quick stats.")
selected_strength = st.sidebar.radio(
    "Preferred strength",
    ["Any", "Strong", "Medium", "Mild"],
    index=0
)
show_price = st.sidebar.checkbox("Show price details", value=True)
if st.sidebar.button("Clear Order 🗑️"):
    st.session_state.order = Order()
    st.sidebar.success("Order cleared!")
    st.experimental_rerun()

# ---------- HEADER / METRICS ----------
st.title("Coffee Shop Dashboard")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Items in cart", len(order.items))
with c2:
    st.metric("Current total", f"${order.total():.2f}")
with c3:
    st.metric("Orders confirmed", st.session_state.order_count)

st.markdown("---")

# ---------- TABS ----------
tab_menu, tab_order = st.tabs(["📋 Menu & Add Items", "🧾 Order & Checkout"])

# ---------- TAB 1: MENU ----------
with tab_menu:
    left, right = st.columns([2, 1])

    with left:
        st.subheader("Available Coffees")

        for i, coffee in enumerate(menu):
            # Simple rule to show "strength" info
            if coffee.name in ["Espresso", "Mocha"]:
                strength = "Strong"
            elif coffee.name == "Cappuccino":
                strength = "Medium"
            else:
                strength = "Mild"

            # Filter by strength selection
            if selected_strength != "Any" and strength != selected_strength:
                continue

            with st.container():
                st.markdown('<div class="coffee-card">', unsafe_allow_html=True)
                cc1, cc2 = st.columns([3, 1])
                with cc1:
                    st.markdown(f"**{coffee.name}**")
                    st.caption(f"Strength: {strength}")
                with cc2:
                    st.write(f"${coffee.price:.2f}")
                    if st.button("Add", key=f"add_{i}"):
                        order.add_item(coffee)
                        st.success(f"Added {coffee.name}!")
                st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.subheader("Cart Snapshot")
        if order.items:
            for i, item in enumerate(order.items, 1):
                st.write(f"{i}. {item.name}")
            st.write("---")
            st.write(f"**Total:** ${order.total():.2f}")
        else:
            st.info("No items yet. Add from the left panel.")

# ---------- TAB 2: ORDER & CHECKOUT ----------
with tab_order:
    st.subheader("Your Order")
    if order.items:
        for i, item in enumerate(order.items, 1):
            col_a, col_b, col_c = st.columns([4, 2, 1])
            with col_a:
                st.write(f"{i}. {item.name}")
            with col_b:
                if show_price:
                    st.write(f"${item.price:.2f}")
            with col_c:
                # Remove single item button
                if st.button("❌", key=f"remove_{i}"):
                    order.items.pop(i - 1)
                    st.experimental_rerun()

        st.markdown("---")
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.metric("Total to pay", f"${order.total():.2f}")
        with col_t2:
            if st.button("✅ Confirm Checkout"):
                st.success("Order confirmed! Thank you ☕")
                st.session_state.order_count += 1
                st.session_state.order = Order()
                st.experimental_rerun()
        with col_t3:
            if st.button("↩️ Reset Cart"):
                st.session_state.order = Order()
                st.info("Cart reset.")
                st.experimental_rerun()
    else:
        st.info("Your cart is empty. Go to the menu tab and add some coffee first!")

st.caption("A modern interactive dashboard for your coffee shop built with Streamlit.")
