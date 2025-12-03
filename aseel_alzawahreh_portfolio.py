import streamlit as st
import pandas as pd

# ============ إعدادات الصفحة ============
st.set_page_config(
    page_title="Aseel Alzawahreh | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============ إدارة الحالة ============
if 'language' not in st.session_state:
    st.session_state.language = 'ar'
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# ============ بيانات ثنائية اللغة ============
CONTENT = {
    'ar': {
        # الهيدر
        'title': 'أسيل الزواهرة',
        'role': 'مطور لوحات تحكم تفاعلية',
        'tagline': 'تحويل البيانات إلى قرارات ذكية',
        
        # القيم الرئيسية
        'projects': 'مشاريع',
        'clients': 'عميل',
        'satisfaction': 'رضا',
        'experience': 'خبرة',
        
        # الأقسام
        'about': 'عنّي',
        'skills': 'المهارات',
        'projects_section': 'المشاريع',
        'contact': 'تواصل',
        'services': 'الخدمات',
        
        # المحتوى
        'about_text': '''
        مطور متخصص في بناء حلول تحليل البيانات التفاعلية باستخدام Streamlit.
        أركز على تحويل العمليات اليدوية إلى أنظمة أوتوماتيكية، وتحويل ملفات Excel
        إلى تطبيقات ويب تفاعلية تسهل اتخاذ القرارات.
        
        **التخصصات الرئيسية:**
        • تطوير لوحات تحكم للمبيعات والتجارة الإلكترونية
        • أتمتة العمليات التجارية وتحليل البيانات
        • تحويل ملفات Excel إلى تطبيقات ويب
        • تصميم واجهات عربية احترافية
        ''',
        
        # المشاريع
        'featured_project': 'المشروع المميز',
        'sales_dashboard': 'لوحة تحليل المبيعات',
        'sales_desc': 'لوحة تحكم متكاملة لتحليل بيانات المبيعات والعملاء',
        'view_live': 'عرض التطبيق',
        'view_code': 'عرض الكود',
        
        # المهارات
        'core_skills': 'المهارات الأساسية',
        'technologies': 'التقنيات',
        'methodologies': 'المنهجيات',
        
        # التواصل
        'get_in_touch': 'تواصل معي',
        'email': 'البريد الإلكتروني',
        'whatsapp': 'واتساب',
        'github': 'GitHub',
        'linkedin': 'LinkedIn',
        'send_message': 'إرسال رسالة',
        'name': 'الاسم',
        'message': 'الرسالة',
        
        # الخدمات
        'services_title': 'الخدمات المقدمة',
        'service1': 'تطوير لوحات تحكم',
        'service1_desc': 'بناء لوحات تحكم تفاعلية مخصصة',
        'service2': 'تحويل Excel إلى WebApp',
        'service2_desc': 'تحويل الملفات التقليدية إلى تطبيقات ويب',
        'service3': 'أتمتة العمليات',
        'service3_desc': 'تطوير أنظمة لأتمتة المهام الروتينية',
        'service4': 'تحليل البيانات',
        'service4_desc': 'تحليل البيانات واستخراج التقارير',
        
        # الأزرار
        'view_all_projects': 'عرض جميع المشاريع',
        'download_cv': 'تحميل السيرة الذاتية'
    },
    'en': {
        # Header
        'title': 'Aseel Alzawahreh',
        'role': 'Interactive Dashboard Developer',
        'tagline': 'Transforming Data into Smart Decisions',
        
        # Key Values
        'projects': 'Projects',
        'clients': 'Clients',
        'satisfaction': 'Satisfaction',
        'experience': 'Experience',
        
        # Sections
        'about': 'About',
        'skills': 'Skills',
        'projects_section': 'Projects',
        'contact': 'Contact',
        'services': 'Services',
        
        # Content
        'about_text': '''
        A developer specializing in building interactive data analysis solutions using Streamlit.
        I focus on transforming manual processes into automated systems, and converting Excel
        files into interactive web applications that facilitate decision-making.
        
        **Main Specializations:**
        • Developing dashboards for sales and e-commerce
        • Business process automation and data analysis
        • Converting Excel files to web applications
        • Professional Arabic interface design
        ''',
        
        # Projects
        'featured_project': 'Featured Project',
        'sales_dashboard': 'Sales Analysis Dashboard',
        'sales_desc': 'Comprehensive dashboard for analyzing sales and customer data',
        'view_live': 'View App',
        'view_code': 'View Code',
        
        # Skills
        'core_skills': 'Core Skills',
        'technologies': 'Technologies',
        'methodologies': 'Methodologies',
        
        # Contact
        'get_in_touch': 'Get in Touch',
        'email': 'Email',
        'whatsapp': 'WhatsApp',
        'github': 'GitHub',
        'linkedin': 'LinkedIn',
        'send_message': 'Send Message',
        'name': 'Name',
        'message': 'Message',
        
        # Services
        'services_title': 'Services Offered',
        'service1': 'Dashboard Development',
        'service1_desc': 'Building customized interactive dashboards',
        'service2': 'Excel to WebApp Conversion',
        'service2_desc': 'Converting traditional files into web applications',
        'service3': 'Process Automation',
        'service3_desc': 'Developing systems to automate routine tasks',
        'service4': 'Data Analysis',
        'service4_desc': 'Data analysis and report extraction',
        
        # Buttons
        'view_all_projects': 'View All Projects',
        'download_cv': 'Download CV'
    }
}

# ============ أنظمة الألوان للثيم ============
THEMES = {
    'light': {
        'primary': '#2563eb',
        'primary_hover': '#1d4ed8',
        'bg_primary': '#ffffff',
        'bg_secondary': '#f8fafc',
        'bg_card': '#ffffff',
        'text_primary': '#1e293b',
        'text_secondary': '#475569',
        'text_muted': '#64748b',
        'border': '#e2e8f0',
        'border_light': '#f1f5f9',
        'shadow': '0 4px 6px -1px rgba(0, 0, 0, 0.1)'
    },
    'dark': {
        'primary': '#3b82f6',
        'primary_hover': '#2563eb',
        'bg_primary': '#0f172a',
        'bg_secondary': '#1e293b',
        'bg_card': '#1e293b',
        'text_primary': '#f1f5f9',
        'text_secondary': '#cbd5e1',
        'text_muted': '#94a3b8',
        'border': '#334155',
        'border_light': '#475569',
        'shadow': '0 4px 6px -1px rgba(0, 0, 0, 0.3)'
    }
}

# ============ تطبيق الثيم ============
def apply_theme():
    theme = THEMES[st.session_state.theme]
    
    css = f"""
    <style>
    :root {{
        --primary: {theme['primary']};
        --primary-hover: {theme['primary_hover']};
        --bg-primary: {theme['bg_primary']};
        --bg-secondary: {theme['bg_secondary']};
        --bg-card: {theme['bg_card']};
        --text-primary: {theme['text_primary']};
        --text-secondary: {theme['text_secondary']};
        --text-muted: {theme['text_muted']};
        --border: {theme['border']};
        --border-light: {theme['border_light']};
        --shadow: {theme['shadow']};
    }}
    
    .stApp {{
        background-color: var(--bg-primary);
        color: var(--text-primary);
        transition: all 0.3s ease;
    }}
    
    /* تصميم البطاقات */
    .custom-card {{
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: var(--shadow);
        transition: all 0.3s ease;
        height: 100%;
    }}
    
    .custom-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }}
    
    /* شريط المهارات */
    .skill-meter {{
        height: 8px;
        background: var(--border);
        border-radius: 4px;
        overflow: hidden;
        margin: 8px 0;
    }}
    
    .skill-fill {{
        height: 100%;
        background: linear-gradient(90deg, var(--primary), var(--primary-hover));
        border-radius: 4px;
    }}
    
    /* تخصيص الأزرار */
    .stButton > button {{
        background-color: var(--primary);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        background-color: var(--primary-hover);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }}
    
    /* تحسين التبويبات */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        border-bottom: 1px solid var(--border);
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        color: var(--text-secondary);
        font-weight: 500;
        border: 1px solid transparent;
        transition: all 0.3s ease;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: var(--primary) !important;
        color: white !important;
        border-color: var(--primary);
    }}
    
    /* تحسينات النصوص */
    h1, h2, h3, h4 {{
        color: var(--text-primary) !important;
    }}
    
    p {{
        color: var(--text-secondary);
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)

# ============ شريط التحكم العلوي ============
def render_control_bar():
    col1, col2, col3 = st.columns([6, 1, 1])
    
    with col2:
        if st.button("عربي" if st.session_state.language == 'en' else "English"):
            st.session_state.language = 'ar' if st.session_state.language == 'en' else 'en'
            st.rerun()
    
    with col3:
        theme_icon = "🌙" if st.session_state.theme == 'light' else "☀️"
        if st.button(theme_icon):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()
    
    return col1

# ============ الهيدر الرئيسي ============
def render_header():
    c = CONTENT[st.session_state.language]
    
    st.markdown(f"# {c['title']}")
    st.markdown(f"### {c['role']}")
    st.markdown(f"*{c['tagline']}*")
    
    # المقاييس الرئيسية
    st.markdown("---")
    
    cols = st.columns(4)
    metrics = [
        ("🚀", c['projects'], "15+"),
        ("👥", c['clients'], "12+"),
        ("⭐", c['satisfaction'], "100%"),
        ("📅", c['experience'], "2+ Years")
    ]
    
    for idx, (icon, label, value) in enumerate(metrics):
        with cols[idx]:
            st.markdown(f"""
            <div style="text-align: center; padding: 1rem;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
                <div style="font-size: 2rem; font-weight: bold; color: var(--primary);">
                    {value}
                </div>
                <div style="color: var(--text-secondary); font-size: 0.9rem;">
                    {label}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")

# ============ نظام المهارات المنظم ============
def render_skills():
    c = CONTENT[st.session_state.language]
    
    st.markdown(f"## 💪 {c['core_skills']}")
    
    # مهارات تقنية منظمة حسب الفئات
    skill_categories = [
        {
            "title": "📊 تحليل البيانات" if st.session_state.language == 'ar' else "📊 Data Analysis",
            "skills": [
                {"name": "Pandas", "level": 95, "desc": "تحليل ومعالجة البيانات" if st.session_state.language == 'ar' else "Data analysis and processing"},
                {"name": "NumPy", "level": 88, "desc": "الحسابات العلمية" if st.session_state.language == 'ar' else "Scientific computing"},
                {"name": "SQL", "level": 85, "desc": "استعلامات وقواعد بيانات" if st.session_state.language == 'ar' else "Database queries"}
            ]
        },
        {
            "title": "🎨 تطوير Streamlit" if st.session_state.language == 'ar' else "🎨 Streamlit Development",
            "skills": [
                {"name": "Streamlit", "level": 96, "desc": "تطبيقات ويب تفاعلية" if st.session_state.language == 'ar' else "Interactive web apps"},
                {"name": "Plotly", "level": 92, "desc": "تصور البيانات التفاعلي" if st.session_state.language == 'ar' else "Interactive data viz"},
                {"name": "Altair", "level": 82, "desc": "تصورات إحصائية" if st.session_state.language == 'ar' else "Statistical visualizations"}
            ]
        },
        {
            "title": "🔄 أتمتة العمليات" if st.session_state.language == 'ar' else "🔄 Process Automation",
            "skills": [
                {"name": "Python", "level": 94, "desc": "برمجة وأتمتة" if st.session_state.language == 'ar' else "Programming & automation"},
                {"name": "OpenPyXL", "level": 90, "desc": "أتمتة ملفات Excel" if st.session_state.language == 'ar' else "Excel automation"},
                {"name": "APScheduler", "level": 80, "desc": "جدولة المهام" if st.session_state.language == 'ar' else "Task scheduling"}
            ]
        }
    ]
    
    # عرض المهارات في شبكة
    cols = st.columns(3)
    
    for idx, category in enumerate(skill_categories):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="custom-card">
                <h4 style="color: var(--text-primary); margin-bottom: 1.5rem;">
                    {category['title']}
                </h4>
            """, unsafe_allow_html=True)
            
            for skill in category['skills']:
                st.markdown(f"""
                <div style="margin-bottom: 1.5rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: 600; color: var(--text-primary);">
                            {skill['name']}
                        </span>
                        <span style="color: var(--primary); font-weight: bold;">
                            {skill['level']}%
                        </span>
                    </div>
                    <p style="color: var(--text-secondary); font-size: 0.9rem; margin: 4px 0;">
                        {skill['desc']}
                    </p>
                    <div class="skill-meter">
                        <div class="skill-fill" style="width: {skill['level']}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    # مهارات إضافية
    st.markdown("<br>", unsafe_allow_html=True)
    
    additional_skills = {
        "ar": {
            "methodologies": ["تحليل RFM", "لوحات تحكم KPI", "تصور البيانات الزمنية", "تقارير تفاعلية"],
            "tools": ["Git", "VS Code", "Docker", "Streamlit Cloud", "Google Sheets API"]
        },
        "en": {
            "methodologies": ["RFM Analysis", "KPI Dashboards", "Time Series Visualization", "Interactive Reports"],
            "tools": ["Git", "VS Code", "Docker", "Streamlit Cloud", "Google Sheets API"]
        }
    }
    
    lang_key = st.session_state.language
    skills = additional_skills[lang_key]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### 📋 {c['methodologies']}")
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        for method in skills["methodologies"]:
            st.markdown(f"• {method}")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"### 🛠️ {c['technologies']}")
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        for tool in skills["tools"]:
            st.markdown(f"• {tool}")
        st.markdown("</div>", unsafe_allow_html=True)

# ============ قسم المشاريع ============
def render_projects():
    c = CONTENT[st.session_state.language]
    
    st.markdown(f"## 🚀 {c['projects_section']}")
    
    # المشروع الرئيسي
    st.markdown(f"### {c['featured_project']}")
    
    project_card = f"""
    <div class="custom-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
            <div>
                <h3 style="color: var(--primary); margin-bottom: 0.5rem;">📊 {c['sales_dashboard']}</h3>
                <p style="color: var(--text-secondary); line-height: 1.6;">
                    {c['sales_desc']}
                </p>
            </div>
        </div>
        
        <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
            <a href="https://salesdashboards.streamlit.app/" target="_blank"
               style="
                    background: var(--primary);
                    color: white;
                    padding: 0.75rem 1.5rem;
                    border-radius: 8px;
                    text-decoration: none;
                    font-weight: 500;
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                    transition: all 0.3s ease;
               "
               onmouseover="this.style.background='var(--primary-hover)'; this.style.transform='translateY(-2px)';"
               onmouseout="this.style.background='var(--primary)'; this.style.transform='translateY(0)';">
                🌐 {c['view_live']}
            </a>
            
            <a href="https://github.com/aseeljalal44-stack/Salesdashboard" target="_blank"
               style="
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
               "
               onmouseover="this.style.background='var(--bg-secondary)'; this.style.transform='translateY(-2px)';"
               onmouseout="this.style.background='transparent'; this.style.transform='translateY(0)';">
                💻 {c['view_code']}
            </a>
        </div>
    </div>
    """
    
    st.markdown(project_card, unsafe_allow_html=True)

# ============ قسم التواصل ============
def render_contact():
    c = CONTENT[st.session_state.language]
    
    st.markdown(f"## 📞 {c['contact']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # معلومات الاتصال
        contact_info = f"""
        <div class="custom-card">
            <h3 style="color: var(--primary); margin-bottom: 1.5rem;">📍 {c['get_in_touch']}</h3>
            
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.5rem;">
                    <span style="color: var(--primary);">📧</span>
                    <strong style="color: var(--text-primary);">{c['email']}:</strong>
                </div>
                <code style="
                    background: var(--bg-secondary);
                    padding: 0.5rem 1rem;
                    border-radius: 6px;
                    display: block;
                    color: var(--text-primary);
                    border: 1px solid var(--border);
                ">
                    aseeljalal45@gmail.com
                </code>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.5rem;">
                    <span style="color: #25D366;">📱</span>
                    <strong style="color: var(--text-primary);">{c['whatsapp']}:</strong>
                </div>
                <div style="
                    background: var(--bg-secondary);
                    padding: 0.5rem 1rem;
                    border-radius: 6px;
                    border: 1px solid var(--border);
                ">
                    +962 78 509 4075
                </div>
                <a href="https://wa.me/962785094075" target="_blank"
                   style="
                        display: inline-block;
                        margin-top: 0.5rem;
                        background: #25D366;
                        color: white;
                        padding: 0.5rem 1rem;
                        border-radius: 6px;
                        text-decoration: none;
                        font-weight: 500;
                   ">
                    📲 إرسال رسالة
                </a>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.5rem;">
                    <span style="color: #0077b5;">💼</span>
                    <strong style="color: var(--text-primary);">{c['linkedin']}:</strong>
                </div>
                <a href="https://linkedin.com" target="_blank" 
                   style="color: var(--primary); text-decoration: none;">
                    linkedin.com/in/aseel-alzawahreh
                </a>
            </div>
            
            <div>
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.5rem;">
                    <span style="color: #333;">💻</span>
                    <strong style="color: var(--text-primary);">{c['github']}:</strong>
                </div>
                <a href="https://github.com/aseeljalal44-stack" target="_blank"
                   style="color: var(--primary); text-decoration: none;">
                    github.com/aseeljalal44-stack
                </a>
            </div>
        </div>
        """
        
        st.markdown(contact_info, unsafe_allow_html=True)
    
    with col2:
        # نموذج الاتصال
        with st.form("contact_form"):
            st.markdown(f"#### ✉️ {c['send_message']}")
            
            name = st.text_input(c['name'])
            email = st.text_input(c['email'])
            message = st.text_area(c['message'], height=120)
            
            submitted = st.form_submit_button(c['send_message'])
            
            if submitted:
                if name and email and message:
                    st.success("✅ تم إرسال رسالتك بنجاح!" if st.session_state.language == 'ar' else "✅ Message sent successfully!")
                else:
                    st.warning("⚠️ يرجى ملء جميع الحقول" if st.session_state.language == 'ar' else "⚠️ Please fill all fields")

# ============ التطبيق الرئيسي ============
def main():
    # تطبيق الثيم
    apply_theme()
    
    # شريط التحكم
    render_control_bar()
    
    # المحتوى الرئيسي
    c = CONTENT[st.session_state.language]
    
    # الهيدر
    render_header()
    
    # تبويبات للمحتوى
    tab1, tab2, tab3, tab4 = st.tabs([
        f"👤 {c['about']}",
        f"💪 {c['skills']}",
        f"🚀 {c['projects_section']}",
        f"📞 {c['contact']}"
    ])
    
    with tab1:
        # قسم عني
        st.markdown(c['about_text'])
        
        # خدمات
        st.markdown(f"### 🛠️ {c['services_title']}")
        
        services = [
            (c['service1'], c['service1_desc'], "📊"),
            (c['service2'], c['service2_desc'], "🔄"),
            (c['service3'], c['service3_desc'], "⚡"),
            (c['service4'], c['service4_desc'], "📈")
        ]
        
        cols = st.columns(2)
        
        for idx, (title, desc, icon) in enumerate(services):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="custom-card">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">
                        {icon}
                    </div>
                    <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">
                        {title}
                    </h4>
                    <p style="color: var(--text-secondary);">
                        {desc}
                    </p>
                </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        # قسم المهارات
        render_skills()
    
    with tab3:
        # قسم المشاريع
        render_projects()
        
        # مشاريع أخرى
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button(c['view_all_projects'], type="secondary"):
            st.info("جميع المشاريع متاحة على GitHub: github.com/aseeljalal44-stack" 
                   if st.session_state.language == 'ar' 
                   else "All projects available on GitHub: github.com/aseeljalal44-stack")
    
    with tab4:
        # قسم التواصل
        render_contact()
    
    # الفوتر
    st.markdown("---")
    
    footer_text = f"""
    <div style="text-align: center; padding: 2rem 0; color: var(--text-muted);">
        <p style="font-size: 1.1rem; font-weight: 500; margin-bottom: 0.5rem;">
            © 2024 {c['title']}
        </p>
        <p style="font-size: 0.9rem;">
            Built with ❤️ using Streamlit • {c['email']} • +962 78 509 4075
        </p>
    </div>
    """
    
    st.markdown(footer_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()