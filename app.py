import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

# ==========================================
# 1. Page Configuration
# ==========================================
st.set_page_config(
    page_title="Kyle Ed C. Maningo · Portfolio",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. Winter Blue Theme
# ==========================================
st.markdown("""
<style>
    :root {
        --winter-blue: #2E4057;
        --snow-cream:  #F4F1EA;
        --icy-blue:    #A9C6D9;
        --deep-accent: #1B2A3D;
        --soft-text:   #4A5A6A;
        --border:      #D9D3C4;
    }

    html, body, [class*="css"] {
        font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
        color: var(--winter-blue);
    }

    .stApp { background-color: var(--snow-cream); }

    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 3px solid var(--icy-blue);
    }

    h1, h2, h3 {
        font-family: Georgia, "Times New Roman", serif;
        color: var(--winter-blue);
        letter-spacing: 0.2px;
    }

    .hero {
        background: linear-gradient(135deg, var(--winter-blue) 0%, var(--deep-accent) 100%);
        color: var(--snow-cream);
        padding: 42px 46px;
        border-radius: 18px;
        margin-bottom: 26px;
        box-shadow: 0 10px 26px rgba(46, 64, 87, 0.25);
        border: 4px solid var(--icy-blue);
    }
    .hero h1 { color: var(--snow-cream); font-size: 3rem; margin: 0 0 8px 0; }
    .hero p  { font-size: 1.15rem; margin: 0; color: var(--icy-blue); }

    .card {
        background: #FFFFFF;
        border: 2px solid var(--border);
        border-radius: 14px;
        padding: 22px 26px;
        margin-bottom: 18px;
        box-shadow: 0 3px 10px rgba(46, 64, 87, 0.06);
    }
    .card h3 { margin-top: 0; color: var(--winter-blue); font-family: Georgia, serif; }

    .chip {
        display: inline-block;
        padding: 6px 14px;
        margin: 4px 6px 4px 0;
        border-radius: 999px;
        background-color: var(--icy-blue);
        color: var(--winter-blue);
        font-weight: 600;
        font-size: 0.85rem;
        letter-spacing: 0.3px;
    }
    .chip.dark { background-color: var(--winter-blue); color: var(--snow-cream); }
    .chip.soft { background-color: var(--snow-cream); color: var(--winter-blue); border: 2px solid var(--icy-blue); }

    .metric-tile {
        background: #FFFFFF;
        border-left: 6px solid var(--icy-blue);
        border-radius: 10px;
        padding: 16px 18px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(46, 64, 87, 0.06);
    }
    .metric-tile .label {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: var(--soft-text);
    }
    .metric-tile .value {
        font-size: 1.45rem;
        font-weight: 700;
        color: var(--winter-blue);
        font-family: Georgia, serif;
    }

    .project {
        background: #FFFFFF;
        border: 2px solid var(--border);
        border-top: 6px solid var(--winter-blue);
        border-radius: 14px;
        padding: 22px;
        height: 100%;
        box-shadow: 0 4px 12px rgba(46, 64, 87, 0.06);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .project:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 22px rgba(46, 64, 87, 0.14);
    }
    .project h3 { margin-top: 0; color: var(--winter-blue); font-size: 1.15rem; }
    .project p  { color: var(--soft-text); font-size: 0.92rem; line-height: 1.5; }

    .divider {
        height: 3px;
        background: repeating-linear-gradient(
            to right,
            var(--icy-blue) 0,
            var(--icy-blue) 24px,
            transparent 24px,
            transparent 48px
        );
        border: none;
        margin: 28px 0;
    }

    .footer {
        text-align: center;
        color: var(--soft-text);
        font-size: 0.85rem;
        padding: 24px 0 8px 0;
        border-top: 2px dashed var(--border);
        margin-top: 40px;
    }

    .stButton > button, .stLinkButton > a {
        background-color: var(--winter-blue) !important;
        color: var(--snow-cream) !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
    }
    .stButton > button:hover, .stLinkButton > a:hover {
        background-color: var(--deep-accent) !important;
    }

    .stTabs [data-baseweb="tab-list"] { gap: 8px; border-bottom: 2px solid var(--border); }
    .stTabs [data-baseweb="tab"] {
        background-color: #FFFFFF;
        border-radius: 8px 8px 0 0;
        padding: 10px 18px;
        font-weight: 600;
        color: var(--winter-blue);
    }
    .stTabs [aria-selected="true"] {
        background-color: var(--icy-blue) !important;
        color: var(--winter-blue) !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. Sidebar — Profile Card
# ==========================================
with st.sidebar:
    st.markdown("### ❄️ Kyle's Space")
    st.image("assets/profpfp.jpg", width=160)
    st.markdown("**Kyle Ed C. Maningo**")
    st.caption("BSIT 4 · UI/UX Designer · Cat lover")
    st.markdown("---")

    page = st.radio(
        "Navigate",
        ["🏠 About Me", "📂 Portfolio", "🎓 Education", "📬 Contact"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("**Quick Links**")
    st.markdown(
        "[🐙 GitHub](https://github.com/Kaled244) · "
        "[📧 Email](mailto:kikikyleed@gmail.com)"
    )
    st.caption("Built with ❄️ and a little 🐶 inspiration")

# ==========================================
# 4. Pages
# ==========================================

# ---------------- ABOUT ----------------
if page == "🏠 About Me":
    st.markdown("""
    <div class="hero">
        <h1>Hello, I'm Kyle 👋</h1>
        <p>BSIT Student · UI/UX Designer · Web Builder · Cat lover</p>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("""
        <div class="card">
            <h3>About Me</h3>
            <p>
            I'm <b>Kyle Ed C. Maningo</b>, a <b>BS Information Technology</b> student
            based in <b>Cebu Institute of Technology – University</b>, with a
            specialization in <b>UI/UX design for websites</b>. I care about how
            interfaces look, how they feel, and how fast users can do what they came to do.
            </p>
            <p>
            My work blends design thinking with real code — I prototype in Figma, then
            bring it to life with <b>React</b>, <b>Tailwind CSS</b>, and <b>Spring Boot</b>
            on the back end. When I'm not designing, I'm playing <b>CODM</b>, <b>MLBB</b>,
            <b>COC</b>, or <b>Apex Legends</b>, or binge-watching K-dramas with my cats
            curled up nearby. 🐱
            </p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("🎲 Fun Facts About Me"):
            st.write("🐱 I absolutely love cats — the fluffier, the better.")
            st.write("🐶 I'm a huge Snoopy fan — the Peanuts aesthetic always cheers me up.")
            st.write("🎮 I rotate between four games depending on my mood: CODM, MLBB, COC, and Apex Legends.")
            st.write("📺 K-dramas and movies are my go-to for winding down after coding.")
            st.write("🎨 I'm the person who redesigns every app I use in my head — it's a blessing and a curse.")

    with col_right:
        st.markdown("""
        <div class="metric-tile">
            <div class="label">Degree</div>
            <div class="value" style="font-size:1.1rem;">BS Information Technology</div>
        </div>
        <div class="metric-tile">
            <div class="label">Major</div>
            <div class="value" style="font-size:1.1rem;">UI/UX Design</div>
        </div>
        <div class="metric-tile">
            <div class="label">Focus</div>
            <div class="value" style="font-size:1.1rem;">Web Interfaces</div>
        </div>
        <div class="metric-tile">
            <div class="label">Location</div>
            <div class="value" style="font-size:1.1rem;">Basak, Cebu City</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ✅ Real st.metric components
    m1, m2, m3 = st.columns(3)
    m1.metric("Year Level", "4th Year", "BSIT 4")
    m2.metric("Projects Completed", "3", "+1 this year")
    m3.metric("UI/UX Focus", "Web", "Figma · React")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.subheader("🛠️ Languages & Frameworks")
    st.markdown("""
        <span class="chip dark">Python</span>
        <span class="chip">Java</span>
        <span class="chip soft">C</span>
        <span class="chip dark">React</span>
        <span class="chip">Spring Boot</span>
        <span class="chip soft">HTML</span>
        <span class="chip">CSS</span>
        <span class="chip dark">Tailwind</span>
        <span class="chip">Supabase</span>
        <span class="chip soft">Kotlin</span>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("🎨 UI/UX Focus")
    st.markdown("""
        <span class="chip">Wireframing</span>
        <span class="chip dark">Prototyping</span>
        <span class="chip soft">Figma</span>
        <span class="chip">Design Systems</span>
        <span class="chip dark">User Research</span>
        <span class="chip soft">Accessibility</span>
        <span class="chip">Responsive Design</span>
    """, unsafe_allow_html=True)

    st.write("")
    st.caption("Proficiency overview")
    c1, c2, c3 = st.columns(3)
    c1.progress(85, text="UI/UX Design")
    c2.progress(80, text="React + Tailwind")
    c3.progress(75, text="Python / Java")

# ---------------- PORTFOLIO ----------------
elif page == "📂 Portfolio":
    st.markdown("""
    <div class="hero" style="background: linear-gradient(135deg, #A9C6D9 0%, #2E4057 100%); border-color:#F4F1EA;">
        <h1 style="color:#F4F1EA;">📂 Selected Work</h1>
        <p style="color:#F4F1EA;">React projects, full-stack builds, and a few experiments in between.</p>
    </div>
    """, unsafe_allow_html=True)

    projects = [
        {
            "icon": "🐾",
            "title": "Lost & Found – Wildcats Finder",
            "role": "Frontend Developer & UI Designer",
            "desc": "A comprehensive web application for CIT-University students to report, find, and claim lost and found items on campus.",
            "outcome": "Deployed for CIT-U students; reduced item-reporting friction with a 3-step form.",
            "tags": ["React", "Spring Boot", "Java"],
            "link": "https://github.com/Kaled244/Lost-Found-WildcatsFinder",
        },
        {
            "icon": "🐱",
            "title": "Furever",
            "role": "Full-Stack Developer (Web + Mobile)",
            "desc": "A streamlined pet adoption and shop application for web and mobile — browse pets, view details, purchase, and adopt.",
            "outcome": "Full-stack demo with Spring Boot API, React web frontend, and Kotlin mobile client.",
            "tags": ["React", "Spring Boot", "Kotlin"],
            "link": "https://github.com/Kaled244/FurEver",
        },
        {
            "icon": "🏛️",
            "title": "PAMANA",
            "role": "UI/UX Designer & Frontend Developer (Capstone)",
            "desc": "A full-stack, three-tier capstone addressing a gap in the MATATAG Grade 2 Filipino curriculum through gamification and storytelling.",
            "outcome": "Capstone prototype covering 4 interactive language-learning modules.",
            "tags": ["Full-Stack", "Gamification", "Capstone"],
            "link": "https://github.com/KobeVLM/PAMANA",
        },
    ]

    cols = st.columns(3, gap="large")
    for i, proj in enumerate(projects):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="project">
                    <h3>{proj['icon']} {proj['title']}</h3>
                    <p style="font-size:0.82rem;color:#2E4057;"><b>Role:</b> {proj['role']}</p>
                    <p>{proj['desc']}</p>
                    <p style="font-size:0.85rem;color:#2E4057;"><b>Outcome:</b> {proj['outcome']}</p>
                    <p style="font-size:0.8rem;color:#777;">
                        <b>Tools:</b> {', '.join(proj['tags'])}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("View Code →", proj["link"], use_container_width=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.subheader("📈 Design & Dev Activity")
    tab1, tab2, tab3 = st.tabs(["Figma Hours", "Languages", "Milestones"])

    with tab1:
        chart_data = pd.DataFrame(
            np.random.randint(2, 12, size=(12, 2)),
            columns=["Figma", "Code"],
            index=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        )
        st.line_chart(chart_data, color=["#2E4057", "#A9C6D9"])

    with tab2:
        # ✅ Self-rated skills (your own numbers)
        skill_df = pd.DataFrame({
            "Skill": ["UI/UX Design", "React", "Tailwind", "Java", "Spring Boot", "Python", "Kotlin", "C"],
            "Self-rated (1-10)": [9, 8, 8, 7, 7, 7, 6, 6],
        })
        st.caption("Self-rated proficiency on a 1–10 scale, based on coursework and projects.")
        st.bar_chart(skill_df, x="Skill", y="Self-rated (1-10)", color="#2E4057")

    with tab3:
        st.write("✅ **2024** — Started focusing on UI/UX design")
        st.write("✅ **2025** — Built **Lost & Found – Wildcats Finder** (React + Spring Boot)")
        st.write("✅ **2025** — Built **Furever** (React + Spring Boot + Kotlin)")
        st.write("✅ **2025** — Built **PAMANA** prototype for capstone (full-stack, gamified learning)")
        st.write("⏳ **2026** — Continuing UI/UX for **PAMANA**")
        st.write("")
        if st.button("🎉 Celebrate Progress"):
            st.balloons()
            st.success("You're doing great, Kyle!")

# ---------------- EDUCATION ----------------
elif page == "🎓 Education":
    st.markdown("""
    <div class="hero" style="background: linear-gradient(135deg, #A9C6D9 0%, #2E4057 100%);">
        <h1 style="color:#F4F1EA;">🎓 Education</h1>
        <p style="color:#F4F1EA;">BS Information Technology · UI/UX Design focus</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>BS Information Technology</h3>
        <p><b>Cebu Institute of Technology – University</b></p>
        <p><b>Major focus:</b> UI/UX Design for Web</p>
        <p style="color:#666;font-size:0.9rem;">
            Coursework spanning web development, human-computer interaction,
            database systems, and software engineering — with a personal focus
            on interface design and usability.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Relevant Coursework")
    courses_df = pd.DataFrame({
        "Course": ["Human-Computer Interaction", "Web Systems & Technologies",
                   "Database Management", "Software Engineering"],
        "Focus": ["UX principles, usability testing",
                  "HTML/CSS/JS, responsive design",
                  "SQL, data modeling",
                  "SDLC, project work"],
        "Status": ["Completed", "Completed", "Completed", "In Progress"],
    })
    st.dataframe(courses_df, use_container_width=True, hide_index=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.subheader("📌 Current Status")
    with st.status("Loading academic records...", expanded=True) as status:
        st.write("Fetching grades...")
        st.write("Calculating GPA...")
        status.update(
            label="Records loaded successfully!",
            state="complete",
            expanded=False,
        )

# ---------------- CONTACT ----------------
elif page == "📬 Contact":
    st.markdown("""
    <div class="hero">
        <h1>📬 Get in Touch</h1>
        <p>Always happy to connect — drop a message below.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>Contact Details</h3>
        <p>📞 <b>09694388745</b></p>
        <p>📧 <b>kikikyleed@gmail.com</b> <span style="color:#888;">(personal)</span></p>
        <p>🎓 <b>kyleed.maningo@cit.edu</b> <span style="color:#888;">(school)</span></p>
        <p>🐙 <b><a href="https://github.com/Kaled244" target="_blank">github.com/Kaled244</a></b></p>
        <p>📍 <b>Basak, Cebu City</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Your Name", placeholder="Juan Dela Cruz")
        with c2:
            email = st.text_input("Your Email", placeholder="juan@example.com")

        topic = st.selectbox(
            "Topic",
            ["General Inquiry", "UI/UX Collaboration",
             "Web Design Project", "Job Opportunity", "Just saying hi"],
        )
        message = st.text_area("Message", placeholder="Write your message here...", height=150)
        urgency = st.slider("Urgency Level", 1, 5, 3, help="1 = Low, 5 = Urgent")

        # ✅ st.checkbox (lecture component)
        consent = st.checkbox("I agree to be contacted about my message.")

        submitted = st.form_submit_button(
            "Send Message", type="primary", use_container_width=True
        )

        if submitted:
            if not consent:
                st.error("Please check the consent box before sending.")
            elif name and email and message:
                st.success(f"Thanks {name}! I'll get back to you within 24 hours.")
                st.balloons()
            else:
                st.error("Please fill in all required fields (Name, Email, Message).")

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    st.subheader("Find me online")
    c1, c2, c3 = st.columns(3)
    c1.info("📧 kikikyleed@gmail.com")
    c2.info("🐙 github.com/Kaled244")
    c3.info("🎓 kyleed.maningo@cit.edu")

# ==========================================
# 5. Footer
# ==========================================
st.markdown(f"""
<div class="footer">
    © {date.today().year} Kyle Ed C. Maningo · BSIT 4 · UI/UX Design · ❄️ Winter Blue theme
</div>
""", unsafe_allow_html=True)