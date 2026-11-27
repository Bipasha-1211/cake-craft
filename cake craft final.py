
import streamlit as st
import sqlite3
from datetime import date, timedelta

st.set_page_config(
    page_title="Cake Craft | Sweet Moments",
    page_icon="🎂",
    layout="wide"
)

# ---------- BEAUTIFUL BAKERY THEME ----------
st.markdown("""
<style>
.stApp {
    background-color: #fff8f5;
}
h1, h2, h3 {
    color: #8b3a50;
}
p, label {
    color: #59434a;
}
div.stButton > button,
div.stFormSubmitButton > button {
    background-color: #b94f70;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1.2rem;
}
div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    background-color: #8b3a50;
    color: white;
}
[data-testid="stSidebar"] {
    background-color: #fde8ed;
}
.cake-banner {
    background: linear-gradient(120deg, #f8dce4, #fff0dc);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 25px;
}
.cake-banner h1 {
    font-size: 42px;
    margin-bottom: 8px;
}
.cake-banner p {
    font-size: 18px;
}
.cake-name {
    color: #8b3a50;
    font-weight: bold;
    font-size: 19px;
}
.cake-price {
    color: #b94f70;
    font-weight: bold;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------- CAKE MENU ----------
cakes = {
    "Chocolate Fudge Cake": {
        "price": 25, "category": "Classic Cakes",
        "description": "Rich chocolate sponge with creamy chocolate frosting.",
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80"
    },
    "Vanilla Dream Cake": {
        "price": 20, "category": "Classic Cakes",
        "description": "Soft vanilla sponge with silky vanilla cream with berry.",
        "image": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?auto=format&fit=crop&w=800&q=80"
    },
    " Cream Cake": {
        "price": 28, "category": "Fruit Cakes",
        "description": "Fresh creamy flavours with delicate mixed cream.",
        "image": "https://images.unsplash.com/photo-1586985289688-ca3cf47d3e6e?auto=format&fit=crop&w=800&q=80"
    },
    "Red Velvet Cake": {
        "price": 30, "category": "Classic Cakes",
        "description": "Velvety red sponge with cream cheese-style frosting.",
        "image": "https://images.unsplash.com/photo-1586788680434-30d324b2d46f?auto=format&fit=crop&w=800&q=80"
    },
    "Chocolate Brownie": {
        "price": 29, "category": "Classic Cakes",
        "description": "Rich chocolate chip and walnut.",
        "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=800&q=80"
    },
    "Lemon Cake": {
        "price": 24, "category": "Fruit Cakes",
        "description": "Light sponge with a refreshing lemon flavour.",
        "image": "https://images.unsplash.com/photo-1519915028121-7d3463d20b13?auto=format&fit=crop&w=800&q=80"
    },
    "Birthday Cake": {
        "price": 22, "category": "Special Cakes",
        "description": "Birthday Celebration cake for special days.",
        "image": "https://images.unsplash.com/photo-1621303837174-89787a7d4729?auto=format&fit=crop&w=800&q=80"
    },
    "Cheesecake": {
        "price": 27, "category": "Special Cakes",
        "description": "Creamy cheesecake with a buttery biscuit base.",
        "image": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=800&q=80"
    },
    "Cupcakes": {
        "price": 15, "category": "Cupcakes",
        "description": "A box of six cupcakes with frosting.",
        "image": "https://images.unsplash.com/photo-1486427944299-d1955d23e34d?auto=format&fit=crop&w=800&q=80"
    },
    "Rainbow Cake": {
        "price": 35, "category": "Celebration Cakes",
        "description": "A colourful Rainbow Cake.",
        "image": "https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?auto=format&fit=crop&w=800&q=80"
    },
    "Wedding Cake": {
        "price": 80, "category": "Celebration Cakes",
        "description": "An elegant cake for weddings and memorable occasions.",
        "image": "https://images.unsplash.com/photo-1535254973040-607b474cb50d?auto=format&fit=crop&w=800&q=80"
    },
    "Blueberry Cake": {
        "price": 28, "category": "Fruit Cakes",
        "description": "A soft cake with sweet blueberry flavours.",
        "image": "https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?auto=format&fit=crop&w=800&q=80"
    },
}

# ---------- DATABASE ----------
def setup_database():
    with sqlite3.connect("cake_craft.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                phone TEXT NOT NULL,
                cake TEXT NOT NULL,
                size TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                pickup_date TEXT NOT NULL,
                message TEXT,
                total REAL NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending'
            )
        """)

setup_database()

# ---------- HEADER ----------
st.markdown("""
<div class="cake-banner">
    <h1>🎂 Cake Craft</h1>
    <p>Handmade sweetness for your most special moments</p>
    <p>♡ Freshly baked • Beautifully made • Made with love ♡</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "🍰 Explore Cake Craft",
    ["Home", "Cake Menu", "Cake Ordering", "Order Management"]
)

st.sidebar.markdown("---")
st.sidebar.write("💗 Made with love, one cake at a time!")

# ---------- HOME ----------
if page == "Home":
    left, right = st.columns([1.2, 1])

    with left:
        st.title("Every celebration deserves cake!")
        st.write(
            "Discover delicious flavours, beautiful celebration cakes, "
            "and sweet treats made for your happiest moments."
        )
        st.write("🍓 Fresh flavours  ·  🎉 Special occasions  ·  💕 Sweet memories")

        if st.button("Explore Our Cakes"):
            st.session_state["page"] = "Cake Menu"
            st.rerun()

    with right:
        st.image(
            "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True
        )

    st.divider()
    st.header("✨ Our Customer Favourites")

    favourites = [
    "Chocolate Fudge Cake",
    "Vanilla Dream Cake",
    "Red Velvet Cake"
]

    cols = st.columns(3)
    for col, name in zip(cols, favourites):
        item = cakes[name]
        with col:
            st.image(item["image"], use_container_width=True)
            st.markdown(f'<p class="cake-name">{name}</p>', unsafe_allow_html=True)
            st.write(item["description"])
            st.markdown(
                f'<p class="cake-price">${item["price"]:.2f} onwards</p>',
                unsafe_allow_html=True
            )

    st.divider()
    st.subheader("💝 Why choose Cake Craft?")
    a, b, c = st.columns(3)
    a.markdown("### 🍰")
    a.write("A variety of delicious flavours")
    b.markdown("### 🎂")
    b.write("Cakes for birthdays and celebrations")
    c.markdown("### 💗")
    c.write("Easy online order management")

# ---------- CAKE MENU ----------
elif page == "Cake Menu":
    st.header("🍰 Our Cake Collection")
    st.write("Find the perfect treat for your next special moment.")

    categories = ["All Cakes"] + sorted(set(
        item["category"] for item in cakes.values()
    ))
    chosen_category = st.selectbox("Filter by category", categories)

    for category in categories[1:]:
        if chosen_category != "All Cakes" and chosen_category != category:
            continue

        matching = [
            (name, item) for name, item in cakes.items()
            if chosen_category == "All Cakes" or item["category"] == chosen_category
        ]

        if chosen_category == "All Cakes":
            st.subheader(category)
            matching = [
                (name, item) for name, item in cakes.items()
                if item["category"] == category
            ]

        for start in range(0, len(matching), 3):
            cols = st.columns(3)
            for col, (name, item) in zip(cols, matching[start:start + 3]):
                with col:
                    with st.container(border=True):
                        st.image(item["image"], use_container_width=True)
                        st.markdown(
                            f'<p class="cake-name">{name}</p>',
                            unsafe_allow_html=True
                        )
                        st.write(item["description"])
                        st.markdown(
                            f'<p class="cake-price">${item["price"]:.2f}</p>',
                            unsafe_allow_html=True
                        )

# ---------- CAKE ORDERING ----------
elif page == "Cake Ordering":
    st.header("🛒 Place Your Cake Order")
    st.write("Choose your favourite cake and tell us how you'd like it.")

    with st.form("order_form"):
        customer_name = st.text_input("Your full name")
        phone = st.text_input("Your phone number")

        cake = st.selectbox("Choose a cake", list(cakes.keys()))
        item = cakes[cake]

        st.image(item["image"], width=320)
        st.write(item["description"])
        st.write(f"Base price: **${item['price']:.2f}**")

        size = st.selectbox("Choose cake size", ["Small", "Medium", "Large"])
        quantity = st.number_input(
            "Quantity", min_value=1, max_value=20, value=1, step=1
        )

        pickup_date = st.date_input(
            "Pickup date",
            value=date.today() + timedelta(days=1),
            min_value=date.today() + timedelta(days=1)
        )

        message = st.text_area("Special requests (optional)")

        multipliers = {"Small": 1.0, "Medium": 1.5, "Large": 2.0}
        total = item["price"] * multipliers[size] * quantity

        st.markdown(f"## Estimated total: ${total:.2f}")
        submitted = st.form_submit_button("💗 Place My Order")

    if submitted:
        if not customer_name.strip() or not phone.strip():
            st.error("Please enter your name and phone number.")
        else:
            with sqlite3.connect("cake_craft.db") as conn:
                cursor = conn.execute("""
                    INSERT INTO orders (
                        customer_name, phone, cake, size, quantity,
                        pickup_date, message, total, status
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    customer_name.strip(), phone.strip(), cake, size,
                    int(quantity), pickup_date.isoformat(),
                    message.strip(), total, "Pending"
                ))
                order_id = cursor.lastrowid

            st.success(f"Your order has been placed! Order number: #{order_id}")
            st.write(f"Your estimated total is **${total:.2f}**.")

# ---------- ORDER MANAGEMENT ----------
elif page == "Order Management":
    st.header("📋 Order Management")

    with sqlite3.connect("cake_craft.db") as conn:
        orders = conn.execute("""
            SELECT id, customer_name, phone, cake, size,
                   quantity, pickup_date, message, total, status
            FROM orders ORDER BY id DESC
        """).fetchall()

    if not orders:
        st.info("No orders yet. Place a test order to see it here.")
    else:
        st.write(f"**Total orders:** {len(orders)}")

        for order in orders:
            (
                order_id, name, phone, cake, size, quantity,
                pickup_date, message, total, status
            ) = order

            with st.expander(f"Order #{order_id} · {name} · {status}"):
                st.write(f"**Customer:** {name}")
                st.write(f"**Phone:** {phone}")
                st.write(f"**Cake:** {cake}")
                st.write(f"**Size:** {size}")
                st.write(f"**Quantity:** {quantity}")
                st.write(f"**Pickup date:** {pickup_date}")
                st.write(f"**Special requests:** {message or 'None'}")
                st.write(f"**Total:** ${total:.2f}")

                statuses = [
                    "Pending", "Preparing", "Ready",
                    "Completed", "Cancelled"
                ]

                new_status = st.selectbox(
                    "Order status",
                    statuses,
                    index=statuses.index(status)
                    if status in statuses else 0,
                    key=f"status_{order_id}"
                )

                if st.button("Save Status", key=f"save_{order_id}"):
                    with sqlite3.connect("cake_craft.db") as conn:
                        conn.execute(
                            "UPDATE orders SET status = ? WHERE id = ?",
                            (new_status, order_id)
                        )
                    st.success("Order status updated!")
                    st.rerun()

# Contact Information
st.markdown("---")
st.subheader("📍 Contact Us")

st.write("**Cake Craft**")
st.write("📍 Location: Norreport, Copenhagen")
st.write("📞 Phone: 71686555")

