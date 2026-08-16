import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Recommendation System", page_icon="🤖", layout="wide"
)

# Initialize Session States
if "favorites" not in st.session_state:
    st.session_state["favorites"] = []


# --- DATASET ---
@st.cache_data
def load_data():
    data = [
        {
            "Product": "Python Basics",
            "Category": "Programming",
            "Price": 20,
            "Rating": 4.8,
        },
        {
            "Product": "Machine Learning Book",
            "Category": "Programming",
            "Price": 35,
            "Rating": 4.9,
        },
        {
            "Product": "AI Fundamentals",
            "Category": "Programming",
            "Price": 30,
            "Rating": 4.7,
        },
        {
            "Product": "Gaming Mouse",
            "Category": "Gaming",
            "Price": 25,
            "Rating": 4.6,
        },
        {
            "Product": "Mechanical Keyboard",
            "Category": "Gaming",
            "Price": 50,
            "Rating": 4.8,
        },
        {
            "Product": "Gaming Headset",
            "Category": "Gaming",
            "Price": 40,
            "Rating": 4.7,
        },
        {"Product": "Football", "Category": "Sports", "Price": 15, "Rating": 4.5},
        {
            "Product": "Cricket Bat",
            "Category": "Sports",
            "Price": 45,
            "Rating": 4.8,
        },
        {
            "Product": "Tennis Racket",
            "Category": "Sports",
            "Price": 60,
            "Rating": 4.7,
        },
        {
            "Product": "Smart Watch",
            "Category": "Electronics",
            "Price": 120,
            "Rating": 4.9,
        },
        {
            "Product": "Wireless Earbuds",
            "Category": "Electronics",
            "Price": 80,
            "Rating": 4.8,
        },
        {
            "Product": "Bluetooth Speaker",
            "Category": "Electronics",
            "Price": 70,
            "Rating": 4.6,
        },
    ]
    return pd.DataFrame(data)


df = load_data()

# --- SIDEBAR SELECTION ---
st.sidebar.markdown("### 🤖 AI Recommendation System")

st.sidebar.markdown("🎨 **Appearance**")
mode = st.sidebar.radio("Select Mode", ["Dark", "Light"], index=1)

st.sidebar.markdown("---")
st.sidebar.markdown("📌 **Navigation**")
page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📊 Dataset",
        "📈 Statistics",
        "🤖 Recommendation",
        "❤️ Favorites",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div class="project-box">
        <h4 style="margin:0;">Project 3</h4>
        <p style="margin: 4px 0;">AI Recommendation Logic</p>
        <small>DecodeLabs AI Internship</small>
    </div>
""",
    unsafe_allow_html=True,
)

# --- DYNAMIC LIGHT / DARK THEMING (CSS) ---
if mode == "Dark":
    # Dark Mode Colors
    bg_main = "#1A1D24"
    bg_sidebar = "#252B37"
    text_color = "#E2E8F0"
    box_bg = "rgba(255, 255, 255, 0.05)"
    box_border = "#3B4252"
else:
    # Light Mode Colors (Matching your Screenshot)
    bg_main = "#EFE3EC"
    bg_sidebar = "#FADCE9"
    text_color = "#5B1A3A"
    box_bg = "rgba(255, 255, 255, 0.4)"
    box_border = "#D8B4C8"

st.markdown(
    f"""
    <style>
        /* Main background */
        .stApp {{
            background-color: {bg_main} !important;
            color: {text_color} !important;
        }}
        
        /* Sidebar background */
        [data-testid="stSidebar"] {{
            background-color: {bg_sidebar} !important;
        }}
        
        /* Text styling */
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp span, .stApp label {{
            color: {text_color} !important;
        }}
        
        /* Sidebar Project Box */
        .project-box {{
            background-color: {box_bg};
            border: 1px solid {box_border};
            padding: 12px;
            border-radius: 8px;
        }}
    </style>
""",
    unsafe_allow_html=True,
)


# --- PAGE 1: HOME ---
if page == "🏠 Home":
    st.title("🤖 AI Recommendation System")
    st.write("Welcome to the **AI Recommendation System**.")
    st.write(
        "This application recommends products based on your preferences using simple AI recommendation logic."
    )

    st.markdown("## Welcome!")
    st.write(
        "This AI Recommendation System recommends products according to the user's interests."
    )

    st.markdown("### Features")
    features = [
        "✓ Product Recommendation",
        "✓ Pattern Matching",
        "✓ User Preferences",
        "✓ Search & Price Filtering",
        "✓ Sort by Price / Rating / Score",
        "✓ Save Favorites ❤️",
        "✓ Dark / Light Mode 🌓",
        "✓ Interactive Dashboard",
        "✓ Download Results",
        "✓ Professional UI",
    ]
    for feat in features:
        st.write(feat)

    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <h4>🤖 AI Recommendation System</h4>
            <p>Developed by Zikra</p>
            <p>BS Computer Science | Women University Mardan</p>
            <p>DecodeLabs Artificial Intelligence Internship</p>
            <p>2026 All Rights Reserved</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

# --- PAGE 2: DATASET ---
elif page == "📊 Dataset":
    st.title("📊 Product Dataset")

    search_query = st.text_input(
        "🔍 Filter dataset by product name", placeholder="Type product name..."
    )

    filtered_df = df.copy()
    if search_query:
        filtered_df = filtered_df[
            filtered_df["Product"]
            .str.lower()
            .str.contains(search_query.lower())
        ]

    st.dataframe(filtered_df, use_container_width=True)
    st.caption(
        f"Showing {len(filtered_df)} of {len(df)} products"
    )

# --- PAGE 3: STATISTICS ---
elif page == "📈 Statistics":
    st.title("📈 Dataset Statistics")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Products", len(df))
    col2.metric("Categories", df["Category"].nunique())
    col3.metric("Highest Rating", f"⭐ {df['Rating'].max()}")
    col4.metric("Average Price", f"${df['Price'].mean():.2f}")

    st.markdown("---")
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("📁 Product By Category")
        cat_counts = (
            df["Category"]
            .value_counts()
            .reset_index()
            .rename(columns={"index": "Category", "count": "Total Products"})
        )
        st.dataframe(cat_counts, use_container_width=True)

    with c2:
        st.subheader("🎨 Category Share")
        cat_share = (
            (df["Category"].value_counts(normalize=True) * 100)
            .reset_index()
            .rename(columns={"index": "Category", "proportion": "Percentage Share"})
        )
        cat_share["Percentage Share"] = cat_share["Percentage Share"].apply(
            lambda x: f"{x:.1f}%"
        )
        st.dataframe(cat_share, use_container_width=True)

    st.markdown("---")
    st.subheader("💰 Price Distribution")
    sorted_df = df.sort_values(by="Price", ascending=False)
    st.dataframe(sorted_df, use_container_width=True)

# --- PAGE 4: RECOMMENDATION ---
elif page == "🤖 Recommendation":
    st.title("🤖 AI Recommendation Engine")
    st.write(
        "Set your preferences below and click the button to get personalized recommendations."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        selected_category = st.selectbox(
            "Category", ["All"] + list(df["Category"].unique())
        )
    with col2:
        min_rating = st.slider("Minimum Rating", 4.0, 5.0, 4.5, step=0.1)
    with col3:
        price_range = st.slider(
            "Price Range ($)",
            int(df["Price"].min()),
            int(df["Price"].max()),
            (15, 120),
        )

    r_col1, r_col2 = st.columns(2)
    with r_col1:
        search_term = st.text_input("🔍 Search by product name (optional)")
    with r_col2:
        sort_by = st.selectbox(
            "⚡ Sort results by",
            ["Recommendation Score", "Price: Low to High", "Rating: High to Low"],
        )

    # Filtering Logic
    results = df.copy()
    if selected_category != "All":
        results = results[results["Category"] == selected_category]

    results = results[
        (results["Rating"] >= min_rating)
        & (results["Price"] >= price_range[0])
        & (results["Price"] <= price_range[1])
    ]

    if search_term:
        results = results[
            results["Product"].str.lower().str.contains(search_term.lower())
        ]

    # Calculate Score Algorithm
    results["Recommendation Score"] = (
        (results["Rating"] / 5.0) * 60 + (1 - (results["Price"] / 120)) * 40
    ).astype(int)

    # Sorting Logic
    if sort_by == "Recommendation Score":
        results = results.sort_values(
            by="Recommendation Score", ascending=False
        )
    elif sort_by == "Price: Low to High":
        results = results.sort_values(by="Price", ascending=True)
    elif sort_by == "Rating: High to Low":
        results = results.sort_values(by="Rating", ascending=False)

    st.success(f"✅ {len(results)} products matched your preferences!")

    if not results.empty:
        top_item = results.iloc[0]
        st.markdown(
            f"""
            <div style="background-color: #FEF3C7; padding: 20px; border-radius: 10px; border: 2px solid #F59E0B; color: #78350F;">
                <h3>🏆 Top Recommendation</h3>
                <h2>{top_item['Product']}</h2>
                <p><strong>Recommendation Score:</strong> {top_item['Recommendation Score']}% Match</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button(f"❤️ Add '{top_item['Product']}' to Favorites"):
            if top_item["Product"] not in st.session_state["favorites"]:
                st.session_state["favorites"].append(top_item["Product"])
                st.toast(
                    f"Added {top_item['Product']} to favorites!", icon="❤️"
                )

        st.markdown("### 📋 All Recommended Products")
        st.dataframe(results, use_container_width=True)

        csv_data = results.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Download Recommendation Data",
            data=csv_data,
            file_name="recommendations.csv",
            mime="text/csv",
        )

# --- PAGE 5: FAVORITES ---
elif page == "❤️ Favorites":
    st.title("❤️ Your Favorite Products")
    st.write(
        "Welcome to your personalized wishlist! Here you can keep track of products you like the most."
    )
    st.write(
        "Easily organize your saved items, review their pricing and ratings, and compare them anytime."
    )

    if not st.session_state["favorites"]:
        st.info(
            "Your favorites list is currently empty. Navigate to the **Recommendation Engine** page, adjust your filters, and click **Add to Favorites** to save your top choices here!"
        )
    else:
        fav_df = df[df["Product"].isin(st.session_state["favorites"])]
        st.dataframe(fav_df, use_container_width=True)

        if st.button("🗑️ Clear Favorites"):
            st.session_state["favorites"] = []
            st.rerun()