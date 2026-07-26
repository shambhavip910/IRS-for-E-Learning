import streamlit as st
import pandas as pd
from content_based import recommend_courses



# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="E-Learning Recommendation System",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
courses = pd.read_csv(r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\clean_courses.csv")
users = pd.read_csv(r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\research_users.csv")
interactions = pd.read_csv(r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\research_interactions.csv")


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎓 E-Learning Platform")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📚 Recommend Courses",
        # "🔍 Search Courses",
        # "📊 Analytics",
        "ℹ About"
    ]
)


# -----------------------------
# Home Page
# -----------------------------
if page == "🏠 Home":

    st.title("🎓 Intelligent E-Learning Recommendation System")

    st.markdown("""
    Welcome to the **AI-powered E-Learning Recommendation System**.
""")


    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📚 Courses",
        len(courses)
    )

    col2.metric(
        "👤 Users",
        len(users)
    )

    col3.metric(
        "⭐ Interactions",
        len(interactions)
    )

    col4.metric(
        "🏆 Categories",
        courses["category"].nunique()
    )

    st.divider()

    st.subheader("🔥 Top Rated Courses")

    top_courses = courses.sort_values(
        "rating",
        ascending=False
    ).head(5)

    st.dataframe(
        top_courses[
            [
                "course_name",
                "platform",
                "category",
                "rating"
            ]
        ],
        use_container_width=True
    )

    st.divider()

 

# -----------------------------
# Recommendation Page
# -----------------------------
elif page == "📚 Recommend Courses":

    st.title("🎓 Course Recommendation")
   

    recommendation_type = st.radio(
        "Choose Recommendation Type",
        ["Content-Based"],
        horizontal=True
    )


    # -------------------------------
    # Content-Based Recommendation
    # -------------------------------
    if recommendation_type == "Content-Based":

        st.subheader("📖 Content-Based Recommendation")
        platform = st.selectbox(
           "Platform",
           ["All"] + sorted(courses["platform"].unique().tolist())
)

        level = st.selectbox(
           "Level",
           ["All"] + sorted(courses["level"].unique().tolist())
)

        category = st.selectbox(
           "Category",
           ["All"] + sorted(courses["category"].unique().tolist())
) 
        

        course_name = st.selectbox(
            "Select a Course",
            sorted(courses["course_name"].unique())
        )

        top_n = st.slider(
            "Number of Recommendations",
            1,
            5,
            3,
            key="content_slider"
        )

        


        if st.button("Recommend Courses"):

            recommendations = recommend_courses(course_name, top_n)

            if recommendations.empty:
                st.warning("No recommendations found.")
            else:
                st.success(f"Top {top_n} recommendations for '{course_name}'")

                for _, row in recommendations.iterrows():

                    with st.container():

                        st.markdown("---")

                        col1, col2 = st.columns([5, 1])

                        with col1:

                            st.subheader(f"📚 {row['course_name']}")
                            st.write(f"🏢 Platform: {row['platform']}")
                            st.write(f"📂 Category: {row['category']}")
                            st.write(f"🎯 Level: {row['level']}")

                        with col2:

                            st.metric("⭐ Rating", row["rating"])


# -----------------------------
# About
# -----------------------------
elif page == "ℹ About":

    st.title("ℹ About")

    st.write("""
Project Name:
Intelligent Recommendation System for E-Learning Platforms

Developed using:

• Python

• Scikit-learn

• Streamlit

• Pandas
""")
     #py -m streamlit run app.py