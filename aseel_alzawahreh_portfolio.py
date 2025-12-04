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
    st.session_state.language = 'en'   # default language = English (per request)
# force dark theme only
st.session_state.theme = 'dark'

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
        "send_message": "إرسال رسالة",
        "name": "الاسم",
        "email": "البريد الإلكتروني",
        "message": "الرسالة",
        "get_in_touch": "تواصل معي",
        "message_sent": "✅ تم إرسال الرسالة. سأعاود التواصل معك قريبًا.",
        "fill_fields": "⚠️ يرجى ملء جميع الحقول."
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
        "send_message": "Send Message",
        "name": "Name",
        "email": "Email",
        "message": "Message",
        "get_in_touch": "Get in Touch",
        "message_sent": "✅ Message sent. I'll get back to you soon.",
        "fill_fields": "⚠️ Please fill all fields."
    }
}

# ============ DATA: USER / PROJECTS / SKILLS / SERVICES ============
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
    "linkedin": ""
}

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

# SKILLS: lists with bilingual descriptions where needed
SKILLS = {
    "data": [
        ("Pandas", {"ar": "تحليل ومعالجة البيانات", "en": "Data manipulation"}),
        ("NumPy", {"ar": "حسابات علمية", "en": "Numerical computing"}),
        ("SQL", {"ar": "استعلامات قواعد البيانات", "en": "DB queries"})
    ],
    "streamlit": [
        ("Streamlit", {"ar": "تطبيقات ويب تفاعلية", "en": "Interactive apps"}),
        ("Plotly", {"ar": "تصورات تفاعلية", "en": "Interactive visualizations"}),
        ("Altair", {"ar": "تصورات إحصائية", "en": "Statistical viz"})
    ],
    "automation": [
        ("Python", {"ar": "برمجة وأتمتة", "en": "Programming & automation"}),
        ("OpenPyXL", {"ar": "أتمتة Excel", "en": "Excel automation"}),
        ("APScheduler", {"ar": "جدولة المهام", "en": "Job scheduling"})
    ]
}

SERVICES = {
    "ar": [
        ("تطوير لوحات تحكم", "بناء لوحات تحكم تفاعلية مخصصة"),
        ("تحويل Excel إلى WebApp", "تحويل الملفات التقليدية إلى تطبيقات ويب"),
        ("أتمتة العمليات", "أتمتة المهام الروتينية لتحسين الكفاءة"),
        ("تحليل البيانات", "استخراج تقارير وInsight قابلة للتنفيذ")
    ],
    "en": [
        ("Dashboard Development", "Building custom interactive dashboards"),
        ("Excel → WebApp", "Converting traditional files into web applications"),
        ("Process Automation", "Automating routine tasks to improve efficiency"),
        ("Data Analysis", "Actionable reporting and insights")
    ]
}

# ============ THEME & CSS (dark-only) ============
def apply_theme_dark_and_fonts():
    # Use dark palette
    base_primary = "#8B5CF6"
    base_secondary = "#5B21B6"
    bg_dark = "#0f1724"  # deep dark
    card = "#0b1220"
    text_light = "#E6EEF8"
    text_muted = "#94A3B8"
    border = "#1f2937"

    # Import Tajawal for Arabic name, fallbacks included
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    :root {{
        --primary: {base_primary};
        --secondary: {base_secondary};
        --bg: {bg_dark};
        --card: {card};
        --text: {text_light};
        --muted: {text_muted};
        --border: {border};
    }}

    html, body, .stApp {{
        background: linear-gradient(180deg, rgba(6,10,15,0.7), rgba(6,10,15,0.85)), var(--bg);
        color: var(--text);
        font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }}

    /* Hero simple text (no card) */
    .hero-simple {{
        padding: 6px 2px;
        margin-bottom: 12px;
    }}
    .hero-simple h1 {{
        margin: 0;
        font-size: 32px;
        font-weight: 800;
        color: var(--text);
    }}
    /* Arabic name styling: Tajawal bold */
    .hero-simple .arabic-name {{
        font-family: 'Tajawal', Inter, sans-serif;
        font-weight: 800;
        letter-spacing: 0.2px;
        direction: rtl;
    }}
    .hero-simple h2 {{
        margin: 6px 0 0 0;
        font-size: 15px;
        font-weight: 600;
        color: var(--muted);
    }}
    .hero-simple p {{
        margin: 8px 0 0 0;
        font-size: 14px;
        color: var(--muted);
    }}

    /* Card */
    .card {{
        background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 8px 30px rgba(2,6,23,0.6);
        transition: transform .18s ease, box-shadow .18s ease;
    }}
    .card:hover {{
        transform: translateY(-6px);
        box-shadow: 0 22px 60px rgba(3,6,23,0.75);
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
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        box-shadow: 0 8px 20px rgba(139,92,246,0.18);
    }}

    .tag {{
        display:inline-block;
        margin:4px 6px 4px 0;
        padding:6px 10px;
        border-radius:999px;
        font-size:12px;
        color:var(--muted);
        background: rgba(255,255,255,0.02);
        border: 1px solid var(--border);
    }}

    a.primary-btn {{
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        color: white !important;
        padding: 8px 12px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 700;
        display:inline-block;
    }}
    a.ghost-btn {{
        background: transparent;
        color: var(--text);
        padding: 8px 12px;
        border-radius: 8px;
        text-decoration: none;
        border: 1px solid var(--border);
        font-weight: 700;
        margin-left:8px;
        display:inline-block;
    }}

    /* section title */
    h2.section-title {{
        color: var(--text);
        font-weight: 700;
        padding-bottom: 6px;
        margin-bottom: 12px;
        position: relative;
        display: inline-block;
    }}
    h2.section-title::after {{
        content: "";
        display: block;
        height: 4px;
        width: 72px;
        margin-top: 8px;
        border-radius: 6px;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        opacity: 0.95;
    }}

    /* Inputs (dark-friendly) */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {{
        background-color: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.04) !important;
        box-shadow: none !important;
        color: var(--text) !important;
    }}
    .stTextInput>div>label, .stTextArea>div>label {{
        color: var(--muted) !important;
    }}

    /* Form submit button styling: override Streamlit button */
    .stButton>button {{
        border-radius: 8px;
        padding: 8px 12px;
        font-weight: 700;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        color: white;
        border: none;
    }}
    .stButton>button:focus {{
        outline: none;
        box-shadow: 0 8px 30px rgba(139,92,246,0.18);
    }}

    /* anchors fallback */
    a.primary-btn, a.ghost-btn {{
        text-decoration: none;
    }}

    /* responsive */
    @media (max-width: 900px) {{
        .hero-simple h1 {{ font-size: 22px; }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# ============ Render Functions ============
def top_control_bar():
    # ensure session_state keys
    if 'language' not in st.session_state:
        st.session_state.language = 'en'

    cols = st.columns([6, 1])
    with cols[1]:
        # language toggle only (English default)
        lang_label = "عربي" if st.session_state.language == "en" else "EN"
        if st.button(lang_label):
            # toggle language
            st.session_state.language = "ar" if st.session_state.language == "en" else "en"
            try:
                st.rerun()
            except Exception:
                # safe fallback: do nothing (page will update next interaction)
                pass


def render_hero():
    c = CONTENT[st.session_state.language]
    u = USER
    # choose name rendering style: Arabic name uses Tajawal class
    if st.session_state.language == 'ar':
        name_html = f"<span class='arabic-name'>{u['name_ar']}</span>"
        role = u['role_ar']
        tagline = u['tagline_ar']
    else:
        name_html = u['name_en']
        role = u['role_en']
        tagline = u['tagline_en']

    st.markdown("<div class='hero-simple'>", unsafe_allow_html=True)
    st.markdown(f"<h1>{name_html}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2>{role}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p>{tagline}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def render_about():
    lang = st.session_state.language
    st.markdown(f"<h2 class='section-title'>{CONTENT[lang]['about']}</h2>", unsafe_allow_html=True)
    about_text = {
        "ar": """
        مطور متخصص في بناء حلول تحليل البيانات التفاعلية باستخدام Streamlit.
        أركز على تحويل العمليات اليدوية إلى أنظمة أوتوماتيكية، وتحويل ملفات Excel
        إلى تطبيقات ويب تفاعلية تسهل اتخاذ القرار.
        """,
        "en": """
        Developer specializing in interactive data solutions using Streamlit.
        I focus on turning manual processes into automated systems and converting Excel
        into interactive web apps that streamline decision making.
        """
    }
    st.markdown(about_text[lang])


def render_skills():
    lang = st.session_state.language
    st.markdown(f"<h2 class='section-title'>{CONTENT[lang]['skills']}</h2>", unsafe_allow_html=True)
    cols = st.columns(3)
    keys = list(SKILLS.keys())
    for i, k in enumerate(keys):
        with cols[i]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            # category title
            if k == "data":
                title = "تحليل البيانات" if lang == "ar" else "Data Analysis"
            elif k == "streamlit":
                title = "تطوير Streamlit" if lang == "ar" else "Streamlit Development"
            else:
                title = "أتمتة" if lang == "ar" else "Automation"
            st.markdown(f"### {title}")
            for name, desc in SKILLS[k]:
                # desc is dict with 'ar' and 'en'
                st.markdown(f"**{name}** — <span style='color:var(--muted); font-size:13px'>{desc[lang]}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)


def render_services():
    lang = st.session_state.language
    st.markdown(f"<h2 class='section-title'>{CONTENT[lang]['services']}</h2>", unsafe_allow_html=True)
    cols = st.columns(2)
    for i, (title, desc) in enumerate(SERVICES[lang]):
        with cols[i % 2]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"### {title}")
            st.markdown(f"<span style='color:var(--muted); font-size:13px'>{desc}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)


def render_projects():
    lang = st.session_state.language
    st.markdown(f"<h2 class='section-title'>🚀 {CONTENT[lang]['projects']}</h2>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, proj in enumerate(PROJECTS):
        with cols[i % 3]:
            title = proj['title_ar'] if lang == 'ar' else proj['title_en']
            desc = proj['desc_ar'] if lang == 'ar' else proj['desc_en']
            tags_html = "".join([f"<span class='tag'>#{t}</span>" for t in proj["tags"]])
            st.markdown(f"""
            <div class="card">
                <div class="project-icon">{proj['icon']}</div>
                <h4 style="color:var(--primary); margin-top:8px;">{title}</h4>
                <div style="color:var(--muted); font-size:13px; margin-top:6px;">{desc}</div>
                <div style="margin-top:10px;">{tags_html}</div>
                <div style="margin-top:12px;">
                    <a class="primary-btn" href="{proj['url']}" target="_blank">{CONTENT[lang]['view_live']}</a>
                    <a class="ghost-btn" href="{USER['github']}" target="_blank">{CONTENT[lang]['view_code']}</a>
                </div>
            </div>
            """, unsafe_allow_html=True)


def render_contact():
    lang = st.session_state.language
    st.markdown(f"<h2 class='section-title'>{CONTENT[lang]['contact']}</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {CONTENT[lang]['get_in_touch']}")
        st.markdown(f"**📧 {USER['email']}**  ")
        st.markdown(f"**📱 WhatsApp:** {USER['whatsapp']}  ")
        if USER['linkedin']:
            st.markdown(f"**💼 LinkedIn:** {USER['linkedin']}  ")
        st.markdown(f"**💻 GitHub:** <a href='{USER['github']}' target='_blank'>{USER['github']}</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### ✉️ " + (CONTENT[lang]['send_message']))
        # contact form
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input(CONTENT[lang]['name'])
            email = st.text_input(CONTENT[lang]['email'])
            message = st.text_area(CONTENT[lang]['message'], height=160)
            submitted = st.form_submit_button(CONTENT[lang]['send_message'])
            if submitted:
                if name.strip() and email.strip() and message.strip():
                    st.success(CONTENT[lang]['message_sent'])
                else:
                    st.warning(CONTENT[lang]['fill_fields'])
        st.markdown("</div>", unsafe_allow_html=True)


# ============ MAIN ============
def main():
    # apply dark theme + fonts
    apply_theme_dark_and_fonts()

    # top control (language toggle only)
    top_control_bar()

    # hero
    render_hero()

    # tabs for content
    lang = st.session_state.language
    tabs = st.tabs([
        CONTENT[lang]['about'],
        CONTENT[lang]['skills'],
        CONTENT[lang]['projects'],
        CONTENT[lang]['contact']
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

    # footer
    st.markdown("---")
    st.markdown(
        f"<div style='text-align:center; color:var(--muted); padding: 16px;'>© {datetime.datetime.now().year} {USER['name_en']} • Built with ❤️ using Streamlit</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()