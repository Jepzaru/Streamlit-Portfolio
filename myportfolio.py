import streamlit as st
import time

st.set_page_config(
    page_title="Jepzfolio",  
    page_icon="images/ulogo.png", 
    layout="wide", 
    initial_sidebar_state="expanded"  
)


with st.spinner('Huwat lang hehe...'):
    time.sleep(5)
st.success("Yey Mana!")

st.balloons()

st.logo("images/ulogo.png")

with open("portfolio.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.markdown("""
    <div style="padding: 20px;">
        <a href="#home" class="sidebar-link">
           🏠 Home
        </a>
        <a href="#favorites" class="sidebar-link">
           ⭐ My Favorites
        </a>
        <a href="#projects" class="sidebar-link">
           📖 Projects
        </a>
        <a href="#programming-languages" class="sidebar-link">
           ✒️ P-Languages
        </a>
        <a href="#skills" class="sidebar-link">
           💪 Skills
        </a>
         <a href="#framework" class="sidebar-link">
          📰 Frameworks learned
        </a>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<div id='home'></div>", unsafe_allow_html=True)

col1, col2 = st.columns([6, 8])

with col1:
    st.image("images/jepz.png", width=550)

with col2:
    st.markdown(
    "<h1>Hello! I'm <span style='color: #ffba09;'>Jeff Francis Conson</span></h1>",
    unsafe_allow_html=True
)
    st.markdown(
    "<p><span style='color: #ffba09;'>Front-End Developer</span></p>",
    unsafe_allow_html=True
)
    st.write("📞 09085916093")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.write("🎓 Bachelor of Science in Information Technology")
    st.write("🏠 6th Street Buenahills Guadalupe Cebu city")
    st.write("🍼 21 years old - December 14, 2002")
    st.write("🏫 Cebu Institute of Technology - University")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Social Links")
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1, 4, 1, 4, 1, 4, 1, 4])
    
    with col1:
        st.image("images/fb.png", width=30)

    with col2:
        st.markdown("""
        <a href="https://www.facebook.com/jaxon.conson" target="_blank" style="text-decoration: none; color: inherit;">
            jaxon.conson
        </a>
        """, unsafe_allow_html=True)
        
    with col3:
        st.image("images/insta.png", width=30)

    with col4:
        st.markdown("""
        <a href="https://www.instagram.com/jfconson/" target="_blank" style="text-decoration: none; color: inherit;">
            jfconson
        </a>
        """, unsafe_allow_html=True)
        
    with col5:
        st.image("images/yt.png", width=30)

    with col6:
        st.markdown("""
        <a href="https://www.youtube.com/@consonjefffrancisd.9432" target="_blank" style="text-decoration: none; color: inherit;">
            Youtube
        </a>
        """, unsafe_allow_html=True)
    
    with col7:
        st.image("images/ghub.png", width=30)

    with col8:
        st.markdown("""
        <a href="https://github.com/Jepzaru" target="_blank" style="text-decoration: none; color: inherit;">
            Jepzaru
        </a>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<div id='favorites'></div>", unsafe_allow_html=True)

st.subheader("My Favorites")

st.markdown("<div style='display: flex; justify-content: space-around; '></div>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.image("images/tufo.png", caption="🐶 Pet", use_column_width=True)
    
    with col2:
        st.image("images/coffee.png", caption="☕ Coffee", use_column_width=True)
    
    with col3:
        st.image("images/basket.png", caption="🏀 Basketball", use_column_width=True)
        
    with col4:
        st.image("images/food.png", caption="🍕 Food", use_column_width=True)
        
    with col5:
        st.image("images/vacation.png", caption="🌊 Vacation", use_column_width=True)
        
    with col6:
        st.image("images/code.png", caption="💻 Programming", use_column_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<div id='projetcs'></div>", unsafe_allow_html=True)
st.subheader("Projects")

project_images = [
    "images/Reserve.png", "images/boird.png", "images/Sakay.png", "images/flightway.png", 
]

for i in range(0, len(project_images), 2):
    cols = st.columns(2)
    for j, col in enumerate(cols):
        if i + j < len(project_images):
            col.image(project_images[i + j], use_column_width=True, caption=f"Project {i + j + 1}")
            
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<div id='programming-languages'></div>", unsafe_allow_html=True)
st.subheader("Programming Languages Learned")

languages = {
    'HTML': 90,
    'CSS': 90,
    'JavaScript': 60,
    'Python': 80,
    'Java': 60
}

for lang, perc in languages.items():
    color_class = {
        'HTML': 'html-bar',
        'CSS': 'css-bar',
        'JavaScript': 'javascript-bar',
        'Python': 'python-bar',
        'Java': 'java-bar'
    }[lang]
    
    st.write(f"{lang} ({perc}%)")
    st.markdown(
        f"""
        <div class="progress-bar {color_class}">
            <div class="progress-bar-filled" style="width: {perc}%;"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)


st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
st.subheader("Skills")

skills = [
    "Problem-solving", 
    "Teamwork", 
    "Time Management", 
    "Leadership", 
    "UI/UX Design",
    "Data Analysis",
]


st.markdown(
    "<ul style='list-style-type:none; padding-left: 0;'>"
    + "".join([f"<li>✅ {skill}</li>" for skill in skills])  
    + "</ul>",
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<div id='framework'></div>", unsafe_allow_html=True)

st.subheader("Frameworks learned")

st.markdown("<div style='display: flex; justify-content: space-around; '></div>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("images/frame.png", use_column_width=True)
    
    with col2:
        st.image("images/mysql.png", use_column_width=True)
    
    with col3:
        st.image("images/apache.png", use_column_width=True)
        
    with col4:
        st.image("images/figma.png", use_column_width=True)
        

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center;'>Assignment: Basic Streamlit App</h4>", unsafe_allow_html=True)