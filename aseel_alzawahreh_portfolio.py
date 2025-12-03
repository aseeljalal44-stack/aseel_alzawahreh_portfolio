import streamlit as st
import base64
import requests
from PIL import Image
import io

# إعدادات الصفحة
st.set_page_config(
    page_title="أسيل الزواهرة | Aseel Alzawahreh",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إدارة الحالة
if 'language' not in st.session_state:
    st.session_state.language = 'ar'
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# بيانات ثنائية اللغة
content = {
    'ar': {
        # التنقل
        'nav_home': 'الرئيسية',
        'nav_about': 'عنّي',
        'nav_skills': 'المهارات',
        'nav_projects': 'المشاريع',
        'nav_contact': 'تواصل',
        
        # الهيدر
        'title': 'أسيل الزواهرة',
        'subtitle': 'مطور لوحات تحكم تفاعلية',
        'tagline': 'تحويل البيانات إلى رؤى عملية',
        
        # عني
        'about_title': 'مرحباً 👋',
        'about_text': '''
        مطور متخصص في بناء حلول تحليل البيانات التفاعلية باستخدام Streamlit.
        
        **أركز على:**
        • تطوير لوحات تحكم احترافية للمبيعات والتجارة الإلكترونية
        • تحويل ملفات Excel إلى تطبيقات ويب تفاعلية
        • أتمتة العمليات التجارية وتحليل البيانات
        • تصميم واجهات عربية سلسة وسهلة الاستخدام
        ''',
        
        # المهارات
        'skills_title': 'المهارات التقنية',
        'skills_subtitle': 'أدوات وخبرات متخصصة',
        
        # المشاريع
        'projects_title': 'المشاريع',
        'project1_title': 'لوحة تحليل المبيعات',
        'project1_desc': 'لوحة تحكم تفاعلية متكاملة لتحليل بيانات المبيعات والعملاء',
        'project2_title': 'محول Excel إلى تطبيق ويب',
        'project2_desc': 'أداة لتحويل ملفات Excel التقليدية إلى تطبيقات ويب تفاعلية',
        'project3_title': 'نظام إدارة الموارد البشرية',
        'project3_desc': 'منصة متكاملة لإدارة الموظفين والرواتب والتقييمات',
        'project4_title': 'منصة التجارة الإلكترونية',
        'project4_desc': 'لوحة تحكم متقدمة للمتاجر الإلكترونية مع تحليلات متكاملة',
        'view_live': 'عرض التطبيق',
        'view_code': 'عرض الكود',
        
        # التواصل
        'contact_title': 'لنتواصل',
        'contact_text': 'مستعد لمساعدتك في مشروعك القادم',
        'email': 'البريد الإلكتروني',
        'whatsapp': 'واتساب',
        'github': 'GitHub',
        'linkedin': 'LinkedIn',
        'send_message': 'إرسال رسالة',
        'get_in_touch': 'تواصل معي',
        
        # الفوتر
        'footer': '© 2024 أسيل الزواهرة',
        'rights': 'جميع الحقوق محفوظة'
    },
    'en': {
        # Navigation
        'nav_home': 'Home',
        'nav_about': 'About',
        'nav_skills': 'Skills',
        'nav_projects': 'Projects',
        'nav_contact': 'Contact',
        
        # Header
        'title': 'Aseel Alzawahreh',
        'subtitle': 'Interactive Dashboard Developer',
        'tagline': 'Turning Data into Actionable Insights',
        
        # About
        'about_title': 'Hello 👋',
        'about_text': '''
        A developer specializing in building interactive data analysis solutions using Streamlit.
        
        **I focus on:**
        • Developing professional dashboards for sales and e-commerce
        • Converting Excel files into interactive web applications
        • Business process automation and data analysis
        • Designing smooth, user-friendly Arabic interfaces
        ''',
        
        # Skills
        'skills_title': 'Technical Skills',
        'skills_subtitle': 'Specialized Tools & Expertise',
        
        # Projects
        'projects_title': 'Projects',
        'project1_title': 'Sales Analysis Dashboard',
        'project1_desc': 'Comprehensive interactive dashboard for sales and customer data analysis',
        'project2_title': 'Excel to Web App Converter',
        'project2_desc': 'Tool to convert traditional Excel files into interactive web applications',
        'project3_title': 'HR Management System',
        'project3_desc': 'Integrated platform for employee, payroll, and performance management',
        'project4_title': 'E-commerce Platform',
        'project4_desc': 'Advanced dashboard for online stores with comprehensive analytics',
        'view_live': 'View App',
        'view_code': 'View Code',
        
        # Contact
        'contact_title': 'Get in Touch',
        'contact_text': 'Ready to help with your next project',
        'email': 'Email',
        'whatsapp': 'WhatsApp',
        'github': 'GitHub',
        'linkedin': 'LinkedIn',
        'send_message': 'Send Message',
        'get_in_touch': 'Contact Me',
        
        # Footer
        'footer': '© 2024 Aseel Alzawahreh',
        'rights': 'All rights reserved'
    }
}

# CSS متقدم مع ثيمين
def get_css(theme):
    if theme == 'dark':
        return """
        <style>
        /* الثيم الداكن */
        :root {
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-card: #1e293b;
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --accent: #3b82f6;
            --accent-hover: #2563eb;
            --border: #334155;
            --border-light: #475569;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            --radius: 12px;
        }
        </style>
        """
    else:
        return """
        <style>
        /* الثيم الفاتح */
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-card: #ffffff;
            --text-primary: #1e293b;
            --text-secondary: #475569;
            --text-muted: #64748b;
            --accent: #2563eb;
            --accent-hover: #1d4ed8;
            --border: #e2e8f0;
            --border-light: #f1f5f9;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            --radius: 12px;
        }
        </style>
        """

# تطبيق CSS العام
def apply_global_css():
    st.markdown("""
    <style>
    /* تطبيق متغيرات CSS */
    .stApp {
        background-color: var(--bg-primary);
        color: var(--text-primary);
        transition: all 0.3s ease;
    }
    
    /* تخصيص النصوص */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary) !important;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    
    p, span, div {
        color: var(--text-secondary);
    }
    
    /* إزالة الهوامش الزائدة */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* تصميم البطاقات */
    .custom-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 1.5rem;
        box-shadow: var(--shadow);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .custom-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    /* تخصيص الأزرار */
    .stButton > button {
        background-color: var(--accent);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: var(--accent-hover);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    
    /* تخصيص حقول الإدخال */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        color: var(--text-primary);
        border-radius: 8px;
    }
    
    /* تخصيص التبويبات */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid var(--border);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        color: var(--text-secondary);
        font-weight: 500;
        border: 1px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: var(--bg-secondary);
        color: var(--accent);
    }
    
    .stTabs [aria-selected="true"] {
        background: var(--accent) !important;
        color: white !important;
        border-color: var(--accent);
    }
    
    /* شريط التقدم */
    .skill-progress {
        height: 8px;
        background: var(--border);
        border-radius: 4px;
        overflow: hidden;
        margin: 8px 0;
    }
    
    .skill-progress-bar {
        height: 100%;
        background: linear-gradient(90deg, var(--accent), var(--accent-hover));
        border-radius: 4px;
        transition: width 1s ease-in-out;
    }
    
    /* تحسينات للهواتف */
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem;
        }
        
        h1 {
            font-size: 2rem;
        }
        
        h2 {
            font-size: 1.5rem;
        }
    }
    
    </style>
    """, unsafe_allow_html=True)

# دالة لتحميل الصورة الشخصية من الرابط
def load_profile_image():
    try:
        # رابط الصورة الشخصية من Google Drive
        # يمكن تغيير هذا الرابط حسب الصورة التي تريدها
        profile_url = "https://drive.google.com/uc?id=1L8Kk0ylfqWmD75TgpR_n1PtRVO9wVpb3"
        
        response = requests.get(profile_url)
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))
            return image
    except:
        pass
    
    # إذا فشل التحميل، استخدم صورة افتراضية
    return None

# شريط التحكم العلوي
def render_top_bar():
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    
    with col1:
        pass  # سيتم ملؤه بالمحتوى
    
    with col2:
        if st.button("عربي" if st.session_state.language == 'en' else "English", 
                    use_container_width=True):
            st.session_state.language = 'ar' if st.session_state.language == 'en' else 'en'
            st.rerun()
    
    with col3:
        theme_icon = "🌙" if st.session_state.theme == 'light' else "☀️"
        if st.button(theme_icon, use_container_width=True):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()
    
    return col1

# الهيدر الرئيسي مع الصورة
def render_header():
    lang = st.session_state.language
    c = content[lang]
    
    # تحميل الصورة الشخصية
    profile_image = load_profile_image()
    
    col1, col2 = st.columns([3, 2], vertical_alignment="center")
    
    with col1:
        st.markdown(f"# {c['title']}")
        st.markdown(f"## {c['subtitle']}")
        st.markdown(f"*{c['tagline']}*")
        
        # فجوة
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        # روابط سريعة
        cols = st.columns(4)
        with cols[0]:
            st.markdown(f"**[👤 {c['nav_about']}](#about)**", unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f"**[💪 {c['nav_skills']}](#skills)**", unsafe_allow_html=True)
        with cols[2]:
            st.markdown(f"**[🚀 {c['nav_projects']}](#projects)**", unsafe_allow_html=True)
        with cols[3]:
            st.markdown(f"**[📞 {c['nav_contact']}](#contact)**", unsafe_allow_html=True)
    
    with col2:
        if profile_image:
            st.image(profile_image, width=200, use_column_width=False, 
                    caption=c['title'] if lang == 'ar' else "Aseel Alzawahreh")
        else:
            # صورة افتراضية جميلة
            st.markdown(f"""
            <div style='text-align: center;'>
                <div style='
                    width: 200px;
                    height: 200px;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    border-radius: 50%;
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-size: 4rem;
                    font-weight: bold;
                    border: 4px solid var(--accent);
                    box-shadow: var(--shadow);
                '>
                    A
                </div>
                <p style='margin-top: 1rem; color: var(--text-secondary);'>
                    {c['title']}
                </p>
            </div>
            """, unsafe_allow_html=True)

# قسم عني
def render_about():
    lang = st.session_state.language
    c = content[lang]
    
    st.markdown(f"<h2 id='about'>👤 {c['about_title']}</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown(c['about_text'])
        
        # معلومات مختصرة
        st.markdown("---")
        cols = st.columns(4)
        metrics = [
            ("🎯", "المشاريع", "Projects", "15+"),
            ("🚀", "التقنيات", "Technologies", "8+"),
            ("💼", "العملاء", "Clients", "12+"),
            ("📈", "الرضا", "Satisfaction", "100%")
        ]
        
        for idx, (icon, ar_text, en_text, value) in enumerate(metrics):
            with cols[idx]:
                text = ar_text if lang == 'ar' else en_text
                st.markdown(f"""
                <div style='text-align: center; padding: 1rem;'>
                    <div style='font-size: 2rem; margin-bottom: 0.5rem;'>{icon}</div>
                    <div style='font-size: 1.8rem; font-weight: bold; color: var(--accent);'>
                        {value}
                    </div>
                    <div style='color: var(--text-secondary); font-size: 0.9rem;'>
                        {text}
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    with col2:
        # مهارات سريعة
        st.markdown(f"### 🛠️ {c['skills_subtitle'] if lang == 'ar' else 'Quick Skills'}")
        
        quick_skills = [
            ("🎨", "Streamlit Development", "تطوير Streamlit", 95),
            ("🐍", "Python Programming", "برمجة Python", 92),
            ("📊", "Data Analysis", "تحليل البيانات", 90),
            ("🔄", "Excel Automation", "أتمتة Excel", 88),
            ("🌐", "Web Applications", "تطبيقات ويب", 87),
            ("🎯", "Arabic UI/UX", "واجهات عربية", 90)
        ]
        
        for icon, en_skill, ar_skill, level in quick_skills:
            skill_text = ar_skill if lang == 'ar' else en_skill
            st.markdown(f"""
            <div style='margin: 1rem 0;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div style='display: flex; align-items: center; gap: 10px;'>
                        <span style='font-size: 1.2rem;'>{icon}</span>
                        <span style='font-weight: 500;'>{skill_text}</span>
                    </div>
                    <span style='color: var(--accent); font-weight: bold;'>{level}%</span>
                </div>
                <div class='skill-progress'>
                    <div class='skill-progress-bar' style='width: {level}%;'></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# عرض المهارات بشكل مبتكر
def render_skills():
    lang = st.session_state.language
    c = content[lang]
    
    st.markdown(f"<h2 id='skills'>💪 {c['skills_title']}</h2>", unsafe_allow_html=True)
    
    # مهارات رئيسية مع أيقونات
    skills_data = [
        {
            "icon": "🚀",
            "category": "تطوير Streamlit" if lang == 'ar' else "Streamlit Development",
            "skills": ["تطبيقات تفاعلية", "لوحات تحكم", "أتمتة العمليات"] if lang == 'ar' 
                     else ["Interactive Apps", "Dashboards", "Process Automation"],
            "color": "#3b82f6"
        },
        {
            "icon": "🐍",
            "category": "برمجة Python" if lang == 'ar' else "Python Programming",
            "skills": ["تحليل البيانات", "معالجة الملفات", "الخوارزميات"] if lang == 'ar'
                     else ["Data Analysis", "File Processing", "Algorithms"],
            "color": "#10b981"
        },
        {
            "icon": "📊",
            "category": "تصور البيانات" if lang == 'ar' else "Data Visualization",
            "skills": ["Plotly", "مخططات تفاعلية", "تقارير متحركة"] if lang == 'ar'
                     else ["Plotly", "Interactive Charts", "Animated Reports"],
            "color": "#8b5cf6"
        },
        {
            "icon": "🔄",
            "category": "أتمتة Excel" if lang == 'ar' else "Excel Automation",
            "skills": ["تحويل إلى WebApp", "معالجة تلقائية", "تصدير تقارير"] if lang == 'ar'
                     else ["WebApp Conversion", "Auto Processing", "Report Export"],
            "color": "#f59e0b"
        },
        {
            "icon": "🌐",
            "category": "تطوير الويب" if lang == 'ar' else "Web Development",
            "skills": ["واجهات عربية", "تصميم متجاوب", "أداء عالي"] if lang == 'ar'
                     else ["Arabic UI", "Responsive Design", "High Performance"],
            "color": "#ef4444"
        },
        {
            "icon": "🎯",
            "category": "حلول الأعمال" if lang == 'ar' else "Business Solutions",
            "skills": ["تحليل المبيعات", "إدارة العملاء", "تقارير أداء"] if lang == 'ar'
                     else ["Sales Analysis", "Customer Management", "Performance Reports"],
            "color": "#06b6d4"
        }
    ]
    
    # عرض المهارات في شبكة
    cols = st.columns(3)
    
    for idx, skill in enumerate(skills_data):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class='custom-card'>
                <div style='
                    width: 50px;
                    height: 50px;
                    background: {skill['color']}20;
                    border: 2px solid {skill['color']};
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 1.5rem;
                    margin-bottom: 1rem;
                    color: {skill['color']};
                '>
                    {skill['icon']}
                </div>
                
                <h4 style='margin-bottom: 1rem; color: var(--text-primary);'>
                    {skill['category']}
                </h4>
                
                <div style='margin-top: 1rem;'>
            """, unsafe_allow_html=True)
            
            for item in skill['skills']:
                st.markdown(f"""
                <div style='
                    display: inline-block;
                    background: var(--bg-secondary);
                    color: var(--text-secondary);
                    padding: 0.4rem 0.8rem;
                    border-radius: 20px;
                    margin: 0.2rem;
                    font-size: 0.85rem;
                    border: 1px solid var(--border);
                '>
                    • {item}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div></div>", unsafe_allow_html=True)

# قسم المشاريع
def render_projects():
    lang = st.session_state.language
    c = content[lang]
    
    st.markdown(f"<h2 id='projects'>🚀 {c['projects_title']}</h2>", unsafe_allow_html=True)
    
    # مشروع رئيسي (حقيقي)
    st.markdown(f"""
    <div class='custom-card'>
        <div style='
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
            gap: 1rem;
        '>
            <div>
                <h3 style='color: var(--accent); margin-bottom: 0.5rem;'>📊 {c['project1_title']}</h3>
                <p style='color: var(--text-secondary); line-height: 1.6;'>
                    {c['project1_desc']}
                </p>
            </div>
            
            <div style='display: flex; gap: 1rem; flex-wrap: wrap;'>
                <a href='https://salesdashboards.streamlit.app/' target='_blank'
                   style='
                        background: var(--accent);
                        color: white;
                        padding: 0.75rem 1.5rem;
                        border-radius: 8px;
                        text-decoration: none;
                        font-weight: 500;
                        display: inline-flex;
                        align-items: center;
                        gap: 8px;
                        transition: all 0.3s ease;
                        border: none;
                        cursor: pointer;
                   '
                   onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(37, 99, 235, 0.3)';"
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';"
                >
                    🌐 {c['view_live']}
                </a>
                
                <a href='https://github.com/aseeljalal44-stack/Salesdashboard' target='_blank'
                   style='
                        background: transparent;
                        color: var(--text-primary);
                        padding: 0.75rem 1.5rem;
                        border-radius: 8px;
                        text-decoration: none;
                        font-weight: 500;
                        display: inline-flex;
                        align-items: center;
                        gap: 8px;
                        border: 1px solid var(--border);
                        transition: all 0.3s ease;
                        cursor: pointer;
                   '
                   onmouseover="this.style.background='var(--bg-secondary)'; this.style.transform='translateY(-2px)';"
                   onmouseout="this.style.background='transparent'; this.style.transform='translateY(0)';"
                >
                    💻 {c['view_code']}
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # مشاريع أخرى
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    projects = [
        (c['project2_title'], c['project2_desc'], "🔄"),
        (c['project3_title'], c['project3_desc'], "👥"),
        (c['project4_title'], c['project4_desc'], "🛒")
    ]
    
    cols = st.columns(3)
    
    for idx, (title, desc, icon) in enumerate(projects):
        with cols[idx]:
            st.markdown(f"""
            <div class='custom-card'>
                <div style='
                    font-size: 2rem;
                    margin-bottom: 1rem;
                    color: var(--accent);
                '>
                    {icon}
                </div>
                
                <h4 style='color: var(--text-primary); margin-bottom: 0.75rem;'>
                    {title}
                </h4>
                
                <p style='color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;'>
                    {desc}
                </p>
            </div>
            """, unsafe_allow_html=True)

# قسم التواصل
def render_contact():
    lang = st.session_state.language
    c = content[lang]
    
    st.markdown(f"<h2 id='contact'>📞 {c['contact_title']}</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"""
        <div class='custom-card'>
            <h3 style='color: var(--accent); margin-bottom: 1.5rem;'>📍 {c['get_in_touch']}</h3>
            
            <div style='margin-bottom: 1.5rem;'>
                <div style='
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    margin-bottom: 0.5rem;
                '>
                    <span style='color: var(--accent);'>📧</span>
                    <strong style='color: var(--text-primary);'>{c['email']}:</strong>
                </div>
                <code style='
                    background: var(--bg-secondary);
                    padding: 0.5rem 1rem;
                    border-radius: 6px;
                    display: block;
                    color: var(--text-primary);
                    border: 1px solid var(--border);
                '>
                    aseeljalal45@gmail.com
                </code>
            </div>
            
            <div style='margin-bottom: 1.5rem;'>
                <div style='
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    margin-bottom: 0.5rem;
                '>
                    <span style='color: #25D366;'>📱</span>
                    <strong style='color: var(--text-primary);'>{c['whatsapp']}:</strong>
                </div>
                <div style='
                    background: var(--bg-secondary);
                    padding: 0.5rem 1rem;
                    border-radius: 6px;
                    border: 1px solid var(--border);
                '>
                    +962 78 509 4075
                </div>
                <a href='https://wa.me/962785094075' target='_blank'
                   style='
                        display: inline-block;
                        margin-top: 0.5rem;
                        background: #25D366;
                        color: white;
                        padding: 0.5rem 1rem;
                        border-radius: 6px;
                        text-decoration: none;
                        font-weight: 500;
                        transition: all 0.3s ease;
                   '
                   onmouseover="this.style.transform='translateY(-2px)';"
                   onmouseout="this.style.transform='translateY(0)';"
                >
                    📲 إرسال رسالة
                </a>
            </div>
            
            <div style='margin-bottom: 1rem;'>
                <div style='
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    margin-bottom: 0.5rem;
                '>
                    <span style='color: #0077b5;'>💼</span>
                    <strong style='color: var(--text-primary);'>{c['linkedin']}:</strong>
                </div>
                <a href='https://linkedin.com' target='_blank' 
                   style='color: var(--accent); text-decoration: none;'>
                    linkedin.com/in/aseel-alzawahreh
                </a>
            </div>
            
            <div>
                <div style='
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    margin-bottom: 0.5rem;
                '>
                    <span style='color: #333;'>💻</span>
                    <strong style='color: var(--text-primary);'>{c['github']}:</strong>
                </div>
                <a href='https://github.com/aseeljalal44-stack' target='_blank'
                   style='color: var(--accent); text-decoration: none;'>
                    github.com/aseeljalal44-stack
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        with st.form("contact_form"):
            st.markdown(f"#### ✉️ {c['send_message']}")
            
            name = st.text_input("الاسم" if lang == 'ar' else "Name")
            email = st.text_input("البريد الإلكتروني" if lang == 'ar' else "Email")
            message = st.text_area("الرسالة" if lang == 'ar' else "Message", height=150)
            
            col_btn1, col_btn2 = st.columns([1, 3])
            with col_btn1:
                submitted = st.form_submit_button(c['send_message'], use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success("✅ تم إرسال رسالتك بنجاح!" if lang == 'ar' else "✅ Message sent successfully!")
                else:
                    st.warning("⚠️ يرجى ملء جميع الحقول" if lang == 'ar' else "⚠️ Please fill all fields")

# الفوتر
def render_footer():
    lang = st.session_state.language
    c = content[lang]
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(f"""
        <div style='text-align: center; padding: 2rem 0; color: var(--text-muted);'>
            <p style='font-size: 1.1rem; font-weight: 500; margin-bottom: 0.5rem;'>
                {c['footer']}
            </p>
            <p style='font-size: 0.9rem;'>
                {c['rights']} • Built with ❤️ using Streamlit
            </p>
            <p style='font-size: 0.8rem; margin-top: 1rem; opacity: 0.7;'>
                aseeljalal45@gmail.com • +962 78 509 4075
            </p>
        </div>
        """, unsafe_allow_html=True)

# التطبيق الرئيسي
def main():
    # تطبيق CSS
    st.markdown(get_css(st.session_state.theme), unsafe_allow_html=True)
    apply_global_css()
    
    # شريط التحكم العلوي
    render_top_bar()
    
    # المحتوى الرئيسي
    render_header()
    
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    render_about()
    
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    render_skills()
    
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    render_projects()
    
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    render_contact()
    
    # الفوتر
    render_footer()

if __name__ == "__main__":
    main()