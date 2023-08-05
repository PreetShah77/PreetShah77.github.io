
import streamlit as st



background_color = "#f0f0f0"  # Replace with your desired background color
st.set_page_config(page_title="My Portfolio", layout="wide", initial_sidebar_state="expanded", page_icon=":rocket:")
st.markdown(f"""<style>body{{background-color: {background_color};}}</style>""", unsafe_allow_html=True)
# App Title
st.title("My Awesome Portfolio")
lottie1 = "971.png"

# Sidebar
st.sidebar.title("My Portfolio")
st.sidebar.markdown("---")
st.sidebar.image(lottie1, width=300)
st.sidebar.markdown("---")
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
        st.write("""
        
        
        
        
        
        """)

elif nav_selection == "My Projects":
    st.header("My Projects")
    st.subheader("Project 1: Space Science Using Python")
    st.write("""## Planetary Data Analysis with SpicePy and Spiceypy Framework
        
        In this ambitious project, I delved into the fascinating realm of planetary data analysis using Python's SpicePy and Spiceypy framework, which were meticulously developed by NASA JPL (Jet Propulsion Laboratory) and ESA (European Space Agency). Armed with these powerful libraries, I embarked on an exploration of real-time information about various planetary bodies, seeking to uncover a wealth of critical parameters such as distance, speed, positioning, and velocity.
        
        **Key Analyses and Discoveries:**
        
        1. Real-Time Distance Calculation:
           Leveraging the capabilities of SpicePy and Spiceypy, I devised intricate algorithms to accurately calculate the real-time distance between diverse planets within our awe-inspiring solar system. This led to groundbreaking insights into their complex orbital dynamics, paving the way for deeper understanding and celestial observations.
        
        2. Planetary Speed and Velocity:
           Through comprehensive data analysis and simulations, I probed the mysteries of planetary motion, uncovering the secrets behind their varying speeds and velocities. This revelation provided essential knowledge about gravitational interactions and planetary behavior across space and time.
        
        3. Planetary Positioning:
           Armed with the powerful SpicePy and Spiceypy framework, I undertook an intensive investigation into the precise positioning of planets relative to each other and the radiant Sun. This meticulous analysis enabled me to create mesmerizing visualizations, presenting celestial bodies in their correct spatial orientations.
        
        4. Orbital Trajectories:
           Fascinated by the graceful dance of planets, I embarked on a captivating journey to visualize their orbital trajectories. With the help of SpicePy and Spiceypy, I skillfully crafted dynamic visual representations of planetary journeys, offering a stunning and interactive experience for all stargazing enthusiasts.
        
        5. Customized Environment with Docker:
           To enhance development efficiency and ensure a seamless workflow, I employed Docker containers to create a customized environment. This approach enabled me to maintain a consistent and isolated environment, optimizing productivity during data exploration and code development.
        
        6. Jupyter Notebook Development:
           Enabling an interactive and immersive data analysis experience, I wholeheartedly embraced Jupyter Notebook as my coding companion. Through Jupyter's versatility, I immersed myself in a realm of exploration, empowering me to share my groundbreaking findings and valuable insights with the world.
        
        **Significance and Future Endeavors:**
        
        This exemplary project showcases my prowess in planetary data analysis, scientific computing, and Docker containerization. By harnessing the unparalleled capabilities of SpicePy and Spiceypy, I have deepened our collective understanding of planetary dynamics, contributing valuable data for astronomical research and education. My passion for space exploration and scientific advancement compels me to continuously explore new frontiers in the realm of astrophysics and planetary sciences.
        
        This project description provides a comprehensive overview of your planetary data analysis project. It emphasizes the key analyses and discoveries made, as well as the significance of your work for scientific research and exploration. Customize the description further to highlight any other significant contributions, challenges faced, or future endeavors related to your project.
        """)
    st.write("[Link to Github Repo(https://github.com/PreetShah77/Space-Science-With-Python)]")

    st.subheader("Project 2: Object Detection using TensorFlow")
    st.write("""## Object Detection using Teachable Machine and TensorFlow.js
        
        In this ambitious project, I developed a powerful object detection system using Google Teachable Machine and a comprehensive dataset sourced from Kaggle. The primary objective was to create a highly accurate and versatile model capable of detecting a wide range of objects, including cars, bikes, people, dogs, cats, horses, flowers, and more.
        
        **Key Features:**
        
        1. Google Teachable Machine:
           Leveraging the user-friendly Google Teachable Machine platform, I meticulously trained a custom machine learning model exclusively for object detection. The intuitive interface enabled me to efficiently train the model using the diverse Kaggle dataset.
        
        2. Extensive Kaggle Dataset:
           For comprehensive object detection, I carefully curated an extensive dataset sourced from Kaggle. The dataset comprised a diverse array of images, encompassing various object classes and scenarios, thereby enhancing the model's accuracy and adaptability.
        
        3. TensorFlow.js Export:
           Following successful model training, I harnessed the capabilities of TensorFlow.js, a powerful JavaScript library, to export the machine learning model. This crucial step enabled seamless integration of the model into web applications, facilitating real-time object detection directly within the user's browser.
        
        **Object Detection in the Browser:**
        
        The culmination of this project was the creation of a dynamic web application featuring real-time object detection capabilities. Users had the convenience of uploading images or using their webcams to experience immediate and accurate object detection within their browsers. This interactive and immersive experience was made possible through the integration of the TensorFlow.js-exported model.
        
        **Applications and Future Enhancements:**
        
        The potential applications of this object detection system are vast, encompassing automated image tagging, surveillance, and augmented reality interactions. Looking ahead, I envision enhancing the model's accuracy through fine-tuning and incorporating additional object classes to expand its already impressive capabilities.
        
        **Try the Demo:**
        
        Embark on a journey of real-time object detection with my captivating interactive demo:
        
        
        """)
    st.write("[Link to Object Detection Demo](https://teachablemachine.withgoogle.com/models/GjYNX-oT4/)")

    st.subheader("Project 3: Elephant Robot for Robocon 2023")
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
    st.subheader("Project 4: Chat with Your Data")
    st.write("""## Personalized Chatbot with Langchain's OpenAI Embeddings and Streamlit
        
        In this project, I developed a personalized chatbot using Langchain's OpenAI embeddings and Streamlit. The chatbot is trained to understand user input better and deliver contextually relevant responses. By integrating user-specific data, it can provide personalized answers tailored to individual preferences and past interactions.
        
        Key Features:
        - Utilizes Langchain's OpenAI embeddings for advanced language understanding.
        - Integrates user data to deliver personalized responses.
        - Built as a user-friendly Streamlit web application for real-time interaction.
        
        The project demonstrates my passion for AI, NLP, and solving real-world problems with innovative solutions. I'm excited about the potential of this personalized chatbot and look forward to enhancing its capabilities in the future.""")
    st.write("[Link to Github Repo(https://github.com/PreetShah77/Chatbot-using-Own-Data)]")

    # Project 2
    st.subheader("Project 5: Sql Query Generator")
    st.write("""## Natural Language SQL Query Generator with Langchain's Chains Embeddings and React UI
        
        In this project, I created a powerful SQL query generator that understands natural English language input and converts it into structured SQL queries. Leveraging the capabilities of Langchain's chains embeddings and LLm (Language Model for SQL), the generator can comprehend complex language patterns and produce accurate SQL queries.
        
        Key Features:
        - Utilizes Langchain's chains embeddings and LLm for advanced language understanding.
        - Converts natural English language into structured SQL queries.
        - Developed a user-friendly React UI for seamless interactions.
        
        The project showcases my expertise in NLP, data processing, and web development. By enabling users to generate SQL queries effortlessly, it simplifies data retrieval and analysis tasks.""")
    st.write("[Link to Github Repo(https://github.com/PreetShah77/Sqlgenerator)]")

    st.subheader("Project 5: Cancer Prediction Using MachineLearning")
    st.write("""' Breast Cancer Prediction Application using Numpy, Scikit-learn, and Streamlit
        
        ' In this ambitious project, I developed a powerful breast cancer prediction application that aids medical professionals in diagnosing breast cancer at an early stage. The application leverages the combined strength of Numpy and Scikit-learn for robust model development and employs Streamlit for creating an intuitive and user-friendly front-end.
        
        ' Key Features:
        
        ' 1. Dataset and Parameter Selection:
        '    To build a reliable breast cancer prediction model, I curated a comprehensive dataset containing a wide array of parameters related to breast cancer cases. These essential features encompassed tumor size, cell shape, cell size, and other critical factors known to influence cancer diagnosis.
        
        ' 2. Model Development with Scikit-learn:
        '    Harnessing the versatility of Scikit-learn, I explored various machine learning algorithms, including logistic regression, decision trees, and random forests. Rigorous model evaluation and hyperparameter tuning ensured optimal performance and reduced the risk of misdiagnosis.
        
        ' 3. Streamlit Front-end:
        '    The application's front-end was crafted using Streamlit, a user-friendly framework that facilitated the seamless integration of the breast cancer prediction model. The Streamlit interface provided an intuitive experience for medical professionals and researchers, enabling them to easily access and utilize the app's predictive capabilities.
        
        ' Empowering Medical Diagnosis:
        
        ' The breast cancer prediction application serves as an indispensable tool in the hands of medical practitioners. By providing quick and accurate predictions based on patient parameters
        """)
    st.write("[Link to Github Repo(https://github.com/PreetShah77/CancerPrediction)]")
    
    st.subheader("Project 6: Stock Market Prediction System")
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

    st.subheader("Project 7: Movie Prediction System")
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

    st.subheader("Project 8: Fighting Brawler")
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
