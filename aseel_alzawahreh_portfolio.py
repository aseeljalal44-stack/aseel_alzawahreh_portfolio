# portfolio.py
import streamlit as st
from pathlib import Path
import base64
import datetime

# ============ إعدادات الصفحة ============
st.set_page_config(
    page_title="Aseel Alzawahreh | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============ الحالة الافتراضية ============
if 'language' not in st.session_state:
    st.session_state.language = 'ar'
if 'theme' not in st.session_state:
    st.session_state.theme = 'auto'  # auto, light, dark

# ============ المحتوى ثنائي اللغة ============
CONTENT = {
    "ar": {
        "title": "أسيل الزواهرة",
        "role": "مطور لوحات تحكّم تفاعلية",
        "tagline": "تحويل البيانات إلى تطبيقات ذكية وسهلة الاستخدام",
        "about": "عنّي",
        "skills": "المهارات",
        "projects": "المشاريع",
        "contact": "تواصل",
        "services": "الخدمات",
        "view_live": "عرض التطبيق",
        "view_code": "عرض الكود",
        "download_cv": "تحميل السيرة الذاتية",
        "send_message": "إرسال رسالة",
        "name": "الاسم",
        "email": "البريد الإلكتروني",
        "message": "الرسالة",
        "get_in_touch": "تواصل معي",
    },
    "en": {
        "title": "Aseel Alzawahreh",
        "role": "Interactive Dashboard Developer",
        "tagline": "Transforming data into smart, usable web apps",
        "about": "About",
        "skills": "Skills",
        "projects": "Projects",
        "contact": "Contact",
        "services": "Services",
        "view_live": "View App",
        "view_code": "View Code",
        "download_cv": "Download CV",
        "send_message": "Send Message",
        "name": "Name",
        "email": "Email",
        "message": "Message",
        "get_in_touch": "Get in Touch",
    }
}

# ============ ثيم Gradient Modern (CSS) ============
def apply_theme():
    # pick palette
    if st.session_state.theme == 'auto':
        # try to use prefers-color-scheme (browser) — fallback to light
        base_primary = "#6366F1"
        base_secondary = "#8B5CF6"
        bg_light = "#F8FAFC"
        bg_card = "#FFFFFF"
        text_dark = "#0f172a"
        text_muted = "#475569"
        border = "#E6EEF8"
    elif st.session_state.theme == 'dark':
        base_primary = "#8B5CF6"
        base_secondary = "#5B21B6"
        bg_light = "#0b1220"
        bg_card = "#0f172a"
        text_dark = "#E6EEF8"
        text_muted = "#94a3b8"
        border = "#1f2937"
    else:  # light
        base_primary = "#6366F1"
        base_secondary = "#8B5CF6"
        bg_light = "#F8FAFC"
        bg_card = "#FFFFFF"
        text_dark = "#0f172a"
        text_muted = "#475569"
        border = "#E6EEF8"

    css = f"""
    <style>
    :root {{
        --primary: {base_primary};
        --secondary: {base_secondary};
        --bg: {bg_light};
        --card: {bg_card};
        --text: {text_dark};
        --muted: {text_muted};
        --border: {border};
    }}

    html, body, .stApp {{
        background: linear-gradient(180deg, rgba(255,255,255,0.0), rgba(245,247,255,0.5)), var(--bg);
        color: var(--text);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }}

    /* Header hero */
    .hero {{
        border-radius: 14px;
        padding: 28px;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        box-shadow: 0 10px 30px rgba(99,102,241,0.15);
        margin-bottom: 18px;
    }}

    .hero h1 {{ margin: 0; font-size: 32px; }}
    .hero h3 {{ margin: 6px 0 0 0; font-weight: 400; opacity: 0.95; }}

    /* Card */
    .card {{
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 6px 18px rgba(15,23,42,0.04);
        transition: transform .18s ease, box-shadow .18s ease;
    }}
    .card:hover {{
        transform: translateY(-6px);
        box-shadow: 0 16px 40px rgba(15,23,42,0.08);
    }}

    .project-icon {{
        width: 64px;
        height: 64px;
        border-radius: 12px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        color: white;
        margin-bottom: 8px;
        background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
        box-shadow: 0 6px 18px rgba(99,102,241,0.12);
    }}

    .tag {{
        display:inline-block;
        margin:4px 6px 4px 0;
        padding:6px 10px;
        border-radius:999px;
        font-size:12px;
        color:var(--muted);
        background: rgba(15,23,42,0.03);
        border: 1px solid var(--border);
    }}

    .primary-btn {{
        background: var(--primary);
        color: white !important;
        padding: 8px 12px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
    }}
    .ghost-btn {{
        background: transparent;
        color: var(--text);
        padding: 8px 12px;
        border-radius: 8px;
        text-decoration: none;
        border: 1px solid var(--border);
        font-weight: 600;
        margin-left:8px;
    }}

    /* responsive */
    @media (max-width: 900px) {{
        .hero h1 {{ font-size: 24px; }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ============ بيانات المستخدم الأساسية ============
USER = {
    "name_ar": "أسيل الزواهرة",
    "name_en": "Aseel Alzawahreh",
    "role_ar": "مطور لوحات تحكّم تفاعلية",
    "role_en": "Interactive Dashboard Developer",
    "tagline_ar": "تحويل البيانات إلى تطبيقات ذكية وسهلة الاستخدام",
    "tagline_en": "Transforming data into smart, usable web apps",
    "email": "aseeljalal45@gmail.com",
    "github": "https://github.com/aseeljalal44-stack",
    "whatsapp": "+962785094075",
    # LinkedIn intentionally left empty for now
    "linkedin": ""
}

# ============ Projects (Grid) ============
PROJECTS = [
    {
        "icon": "👔",
        "title_ar": "لوحة تحكم الموارد البشرية الذكية",
        "title_en": "Smart HR Analytics Dashboard",
        "desc_ar": "نظام تفاعلي لمعالجة أي ملف Excel وتحويله إلى لوحة قيادة ذكية للموارد البشرية.",
        "desc_en": "An intelligent HR system that transforms any Excel file into a smart HR analytics dashboard.",
        "tags": ["HR", "Excel Automation", "KPI", "Field Detection"],
        "url": "https://hrdashbord-28auw66gfafgeiav5vdnks.streamlit.app/"
    },
    {
        "icon": "📈",
        "title_ar": "لوحة تحليل المبيعات المتقدمة – نسخة المؤسسات",
        "title_en": "Advanced Sales Analytics – Enterprise",
        "desc_ar": "تحليل متقدم للبيانات المعقّدة مع اكتشاف تلقائي للحقول وتحليلات متمكّنة.",
        "desc_en": "Advanced analytics for complex datasets with automatic field detection and deep KPI insights.",
        "tags": ["Sales", "Enterprise", "Automation", "Excel"],
        "url": "https://salesdashboards-bvbbbq6v7m9p7h7yrcwww2.streamlit.app/"
    },
    {
        "icon": "🛍️",
        "title_ar": "لوحة تحكم المبيعات الذكية – الإصدار السريع",
        "title_en": "Smart Sales Dashboard – Lite",
        "desc_ar": "نسخة خفيفة وسريعة لعرض المؤشرات الأساسية من ملفات Excel/CSV.",
        "desc_en": "A lightweight, fast dashboard for essential KPIs using Excel/CSV uploads.",
        "tags": ["Sales", "Lite", "Excel", "KPIs"],
        "url": "https://salesdashboards.streamlit.app/"
    }
]

# ============ Skills & Services ============
SKILLS = {
    "data": [
        ("Pandas", "تحليل ومعالجة البيانات / Data manipulation"),
        ("NumPy", "حسابات علمية / Numerical computing"),
        ("SQL", "استعلامات قواعد البيانات / DB queries")
    ],
    "streamlit": [
        ("Streamlit", "تطبيقات ويب تفاعلية / Interactive apps"),
        ("Plotly", "تصورات تفاعلية / Interactive visualizations"),
        ("Altair", "تصورات إحصائية / Statistical viz")
    ],
    "automation": [
        ("Python", "برمجة وأتمتة / Programming & automation"),
        ("OpenPyXL", "أتمتة Excel / Excel automation"),
        ("APScheduler", "جدولة المهام / Job scheduling")
    ]
}

SERVICES = [
    ("تطوير لوحات تحكم", "بناء لوحات تحكم تفاعلية مخصصة / Custom interactive dashboards"),
    ("تحويل Excel إلى WebApp", "تحويل الملفات التقليدية إلى تطبيقات ويب / Excel → WebApp"),
    ("أتمتة العمليات", "أتمتة المهام الروتينية لتحسين الكفاءة / Process automation"),
    ("تحليل البيانات", "استخراج تقارير وInsight قابلة للتنفيذ / Data analysis & reporting")
]

# ============ مساعدة لتحميل/عرض ملف CV ============
def get_file_download_link(file_path: Path, label: str):
    if not file_path.exists():
        return None
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f"data:application/octet-stream;base64,{b64}"
    return href

# ============ Render Functions ============
def top_control_bar():
    cols = st.columns([6, 1, 1])
    with cols[1]:
        if st.button("EN" if st.session_state.language == "ar" else "عربي"):
            st.session_state.language = "en" if st.session_state.language == "ar" else "ar"
            st.experimental_rerun()
    with cols[2]:
        # cycle theme
        if st.button("🌓"):
            # cycle auto -> dark -> light -> auto
            order = ["auto", "dark", "light"]
            idx = order.index(st.session_state.theme)
            st.session_state.theme = order[(idx + 1) % len(order)]
            st.experimental_rerun()

def render_hero():
    c = CONTENT[st.session_state.language]
    u = USER
    name = u["name_ar"] if st.session_state.language == "ar" else u["name_en"]
    role = u["role_ar"] if st.session_state.language == "ar" else u["role_en"]
    tagline = u["tagline_ar"] if st.session_state.language == "ar" else u["tagline_en"]

    st.markdown(f"""
    <div class="hero">
        <h1>{name} — {role}</h1>
        <h3>{tagline}</h3>
    </div>
    """, unsafe_allow_html=True)

    # brief metrics (example)
    cols = st.columns(4)
    metrics = [
        ("🚀", "Projects", "3+"),
        ("👥", "Clients", "10+"),
        ("⭐", "Satisfaction", "100%"),
        ("📅", "Experience", "2+ Years"),
    ]
    for i, (icon, label, value) in enumerate(metrics):
        with cols[i]:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
                <div style="font-size:20px">{icon}</div>
                <div style="font-weight:700; font-size:18px; margin-top:6px;">{value}</div>
                <div style="color:var(--muted); margin-top:4px;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

def render_about():
    c = CONTENT[st.session_state.language]
    st.markdown(f"## {c['about']}")
    about_text_ar = """
    مطور متخصص في بناء حلول تحليل البيانات التفاعلية باستخدام Streamlit.
    أركز على تحويل العمليات اليدوية إلى أنظمة أوتوماتيكية، وتحويل ملفات Excel
    إلى تطبيقات ويب تفاعلية تسهل اتخاذ القرار.
    """
    about_text_en = """
    Developer specializing in interactive data solutions using Streamlit.
    I focus on turning manual processes into automated systems and converting Excel
    into interactive web apps that streamline decision making.
    """
    st.markdown(about_text_ar if st.session_state.language == "ar" else about_text_en)

def render_skills():
    c = CONTENT[st.session_state.language]
    st.markdown(f"## {c['skills']}")
    cols = st.columns(3)
    keys = list(SKILLS.keys())
    for i, k in enumerate(keys):
        with cols[i]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            title = "تحليل البيانات" if k == "data" and st.session_state.language == "ar" else \
                    ("Data Analysis" if k == "data" else k.title())
            st.markdown(f"### {title}")
            for name, desc in SKILLS[k]:
                st.markdown(f"**{name}** — <span style='color:var(--muted); font-size:13px'>{desc}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

def render_services():
    c = CONTENT[st.session_state.language]
    st.markdown(f"## {c['services']}")
    cols = st.columns(2)
    for i, (title, desc) in enumerate(SERVICES):
        with cols[i % 2]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"### {title}")
            st.markdown(f"<span style='color:var(--muted); font-size:13px'>{desc}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

def render_projects():
    c = CONTENT[st.session_state.language]
    st.markdown(f"## 🚀 {c['projects']}")
    # grid of 3 columns
    cols = st.columns(3)
    for i, proj in enumerate(PROJECTS):
        with cols[i % 3]:
            tags_html = "".join([f"<span class='tag'>#{t}</span>" for t in proj["tags"]])
            title = proj["title_ar"] if st.session_state.language == "ar" else proj["title_en"]
            desc = proj["desc_ar"] if st.session_state.language == "ar" else proj["desc_en"]
            st.markdown(f"""
            <div class="card">
                <div class="project-icon" style="background: linear-gradient(135deg, var(--primary), var(--secondary));">
                    {proj['icon']}
                </div>
                <h4 style="color:var(--primary); margin-top:8px;">{title}</h4>
                <div style="color:var(--muted); font-size:13px; margin-top:6px;">{desc}</div>
                <div style="margin-top:10px;">{tags_html}</div>
                <div style="margin-top:12px;">
                    <a class="primary-btn" href="{proj['url']}" target="_blank">{c['view_live']}</a>
                    <a class="ghost-btn" href="{USER['github']}" target="_blank">{c['view_code']}</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_contact():
    c = CONTENT[st.session_state.language]
    st.markdown(f"## {c['contact']}")
    col1, col2 = st.columns([2, 3])
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {c['get_in_touch']}")
        st.markdown(f"**📧 {USER['email']}**  ")
        st.markdown(f"**📱 WhatsApp:** {USER['whatsapp']}  ")
        if USER['linkedin']:
            st.markdown(f"**💼 LinkedIn:** {USER['linkedin']}  ")
        st.markdown(f"**💻 GitHub:** <a href='{USER['github']}' target='_blank'>{USER['github']}</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # CV upload / download
        st.markdown("<div class='card' style='margin-top:12px;'>", unsafe_allow_html=True)
        st.markdown("### 📄 CV")
        uploaded = st.file_uploader("رفع ملف السيرة الذاتية (PDF) — Upload CV (optional)", type=['pdf'])
        cv_path = Path("uploaded_cv.pdf")
        if uploaded:
            with open(cv_path, "wb") as f:
                f.write(uploaded.getbuffer())
            st.success("تم رفع السيرة الذاتية ✅")
        # show download button if exists
        download_link = get_file_download_link(cv_path, "CV")
        if download_link:
            st.markdown(f"<a href='{download_link}' download='CV_Aseel_Alzawahreh.pdf' class='primary-btn'>{c['download_cv']}</a>", unsafe_allow_html=True)
        else:
            st.info("يمكنك رفع ملف PDF للسيرة الذاتية ليظهر زر التحميل.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### ✉️ " + (c['send_message']))
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input(c['name'])
            email = st.text_input(c['email'])
            message = st.text_area(c['message'], height=160)
            submitted = st.form_submit_button(c['send_message'])
            if submitted:
                if name.strip() and email.strip() and message.strip():
                    st.success("✅ تم إرسال الرسالة. سأعاود التواصل معك قريبًا." if st.session_state.language == "ar" else "✅ Message sent. I'll get back to you soon.")
                else:
                    st.warning("⚠️ يرجى ملء جميع الحقول." if st.session_state.language == "ar" else "⚠️ Please fill all fields.")
        st.markdown("</div>", unsafe_allow_html=True)

# ============ Main ============
def main():
    apply_theme()
    top_control_bar()
    render_hero()

    tabs = st.tabs([
        CONTENT[st.session_state.language]['about'],
        CONTENT[st.session_state.language]['skills'],
        CONTENT[st.session_state.language]['projects'],
        CONTENT[st.session_state.language]['contact']
    ])

    with tabs[0]:
        render_about()
        render_services()

    with tabs[1]:
        render_skills()

    with tabs[2]:
        render_projects()

    with tabs[3]:
        render_contact()

    # Footer
    st.markdown("---")
    st.markdown(f"<div style='text-align:center; color:var(--muted); padding: 16px;'>© {datetime.datetime.now().year} {USER['name_en']} • Built with ❤️ using Streamlit</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()