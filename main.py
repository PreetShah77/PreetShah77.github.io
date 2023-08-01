# Import required libraries
import streamlit as st
import pandas as pd

background_color = "#f0f0f0"  # Replace with your desired background color
st.set_page_config(page_title="My Portfolio", layout="wide", initial_sidebar_state="expanded", page_icon=":rocket:")
st.markdown(f"""<style>body{{background-color: {background_color};}}</style>""", unsafe_allow_html=True)
# App Title
st.title("My Awesome Portfolio")

# Sidebar
st.sidebar.title("Navigation")
nav_selection = st.sidebar.radio("Go to:", ("About Me", "My Projects"))

# Main content
if nav_selection == "About Me":
    st.header("About Me")
    col1, col2 = st.columns([1, 2])

    # Column 1 - Profile picture
    with col1:
        st.image("profile_pic.jpg", caption="My Profile Picture", width=150)

    # Column 2 - Description
    with col2:
        st.write("Hi there! I'm Preet Shah, a passionate student at Ganpat University, India. "
                 "I am currently a core member of both the Coders Club and Robocon Club at the university, "
                 "where I indulge in my love for coding and robotics. Being part of these clubs has provided me "
                 "with practical experience, teamwork skills, and the opportunity to work on exciting projects.")

        st.write("My primary area of interest lies in Artificial Intelligence and Machine Learning. I find "
                 "great joy in exploring the potential of AI and ML to solve real-world problems and make a positive "
                 "impact on people's lives. I enjoy diving into data, analyzing patterns, and creating predictive "
                 "models that can drive data-driven decisions.")
        st.write("I'm excited to share my projects and experiences with you through this portfolio. Feel free to "
                 "explore my work, and don't hesitate to reach out to me if you have any questions or collaboration "
                 "opportunities.")

elif nav_selection == "My Projects":
    st.header("My Projects")

    st.subheader("Project 1: Elephant Robot for Robocon 2023")
    st.write("""## Robocon 2023: Intelligent Robot Control using Machine Learning and ESP Integration
        
        In this project, I developed and programmed two intelligent robots for Robocon 2023, adhering to the theme provided by the competition. The robots were designed to showcase cutting-edge technologies and innovative control mechanisms to deliver exceptional performance on the competition field.
        
        Key Features:
        - Utilized machine learning techniques, specifically PID (Proportional-Integral-Derivative) control, to achieve precise and dynamic robot movements.
        - Integrated ESP modules for seamless communication between the robots and a PS4 controller, enabling intuitive and responsive control.
        - Programmed various motors, including BLDC (Brushless DC) motors, Johnson motors, and stepper motors, to set angles dynamically and adapt to different scenarios on the field.
        - Implemented a LiDAR (Light Detection and Ranging) system for precise navigation and obstacle avoidance, enhancing the robots' autonomous capabilities.
        
        The project demonstrates my proficiency in machine learning, robotics, and hardware integration. By leveraging advanced control algorithms and real-time sensor data, the robots delivered exceptional performance and showcased their adaptability to changing conditions on the competition field.
        
        [Link to Video](https://youtu.be/waNGaybPEDs)
        """)
    st.write("[Link to Github Repo(https://github.com/PreetShah77/Robocon-2023)]")

    # Project 1
    st.subheader("Project 2: Chat with Your Data")
    st.write("""## Personalized Chatbot with Langchain's OpenAI Embeddings and Streamlit
        
        In this project, I developed a personalized chatbot using Langchain's OpenAI embeddings and Streamlit. The chatbot is trained to understand user input better and deliver contextually relevant responses. By integrating user-specific data, it can provide personalized answers tailored to individual preferences and past interactions.
        
        Key Features:
        - Utilizes Langchain's OpenAI embeddings for advanced language understanding.
        - Integrates user data to deliver personalized responses.
        - Built as a user-friendly Streamlit web application for real-time interaction.
        
        The project demonstrates my passion for AI, NLP, and solving real-world problems with innovative solutions. I'm excited about the potential of this personalized chatbot and look forward to enhancing its capabilities in the future.""")
    st.write("[Link to Github Repo(https://github.com/PreetShah77/Chatbot-using-Own-Data)]")

    # Project 2
    st.subheader("Project 3: Sql Query Generator")
    st.write("""## Natural Language SQL Query Generator with Langchain's Chains Embeddings and React UI
        
        In this project, I created a powerful SQL query generator that understands natural English language input and converts it into structured SQL queries. Leveraging the capabilities of Langchain's chains embeddings and LLm (Language Model for SQL), the generator can comprehend complex language patterns and produce accurate SQL queries.
        
        Key Features:
        - Utilizes Langchain's chains embeddings and LLm for advanced language understanding.
        - Converts natural English language into structured SQL queries.
        - Developed a user-friendly React UI for seamless interactions.
        
        The project showcases my expertise in NLP, data processing, and web development. By enabling users to generate SQL queries effortlessly, it simplifies data retrieval and analysis tasks.""")
    st.write("[Link to Github Repo(https://github.com/PreetShah77/Sqlgenerator)]")

    st.subheader("Project 4: Stock Market Prediction System")
    st.write("""## Stock Market Prediction System with Machine Learning and Streamlit
        
        In this project, I developed a robust stock market prediction system using machine learning techniques and the Stock Market India dataset sourced from Kaggle. The system is designed to forecast stock prices, enabling investors to make informed decisions and optimize their trading strategies.
        
        Key Features:
        - Utilized linear regression and random forest regression for stock price prediction.
        - Employs Jupyter Lab for data exploration and model development.
        - Incorporates scikit-learn, seaborn, and matplotlib for data analysis and visualization.
        - Developed a user-friendly Streamlit web app for real-time stock predictions.
        
        The project demonstrates my proficiency in machine learning, data analysis, and web development. By harnessing the power of machine learning algorithms, investors can gain valuable insights into stock market trends and potentially enhance their investment returns.
        """)
    st.write("[Link to Github Repo(https://project2.com)]")

    st.subheader("Project 5: Movie Prediction System")
    st.write("""## Movie Prediction System with Machine Learning and Streamlit
        
        In this project, I developed an advanced movie prediction system using machine learning techniques and the TMDb_5000 dataset. The system is designed to recommend movies based on user preferences and historical data, providing personalized movie suggestions for an enhanced entertainment experience.
        
        Key Features:
        - Performed data analysis and data cleaning on the TMDb_5000 dataset.
        - Utilized machine learning algorithms for movie recommendation.
        - Leveraged Jupyter Lab for data exploration and model development.
        - Incorporated scikit-learn, seaborn, and matplotlib for data analysis and visualization.
        - Developed a user-friendly Streamlit web app for seamless movie recommendations.
        
        The project showcases my expertise in data analysis, machine learning, and web development. By harnessing the power of machine learning algorithms and user preferences, the movie prediction system offers tailored movie recommendations to delight movie enthusiasts.
        """)
    st.write("[Link to Github Repo(https://github.com/PreetShah77/Movie-managment-system)]")

    st.subheader("Project 6: Fighting Brawler")
    st.write("""## Multiplayer Game with Pygame: Epic Shadow Fight
        
        In this project, I developed an action-packed multiplayer game using Pygame, where players can engage in thrilling combat battles with cool sprites and immersive game physics. Inspired by the popular game Shadow Fight, this project offers an exciting and competitive gaming experience for users.
        
        Key Features:
        - Implemented a real-time multiplayer game using Pygame.
        - Designed captivating and dynamic sprites for player characters and in-game elements.
        - Utilized various game physics to create realistic combat movements and interactions.
        - Incorporated interactive and user-friendly controls for seamless gameplay.
        
        The project demonstrates my creativity in game development and proficiency in Python and Pygame. With exciting combat battles and engaging multiplayer interactions, Epic Shadow Fight delivers an adrenaline-pumping gaming experience.
        """)
    st.write("[Link to Github Repo(https://github.com/PreetShah77/FightingBrawler)]")

    # Add more projects as needed


st.markdown("---")
st.write("Contact: preetshah0707@gmail.com | Follow me on [LinkedIn](https://www.linkedin.com/in/yourprofile/)")
