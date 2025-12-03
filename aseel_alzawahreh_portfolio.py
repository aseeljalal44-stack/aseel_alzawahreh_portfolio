import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import io
import base64

# إعدادات الصفحة
st.set_page_config(
    page_title="Aseel Alzawahreh | Portfolio",
    page_icon="🚀",
    layout="wide"
)

# إدارة اللغة في حالة الجلسة
if 'language' not in st.session_state:
    st.session_state.language = 'ar'

# بيانات ثنائية اللغة
translations = {
    'ar': {
        'title': 'أسيل الزواهرة | مطور لوحات تحكم تفاعلية',
        'hero_title': 'أسيل الزواهرة',
        'hero_subtitle': 'مطور لوحات تحكم تفاعلية | أتمتة العمليات',
        'about': 'عنّي',
        'about_content': '''
        مطور متخصص في تحويل البيانات التقليدية إلى تطبيقات ويب تفاعلية باستخدام Streamlit و Python.
        
        **تخصصاتي:**
        • تطوير لوحات تحكم للمبيعات والتجارة الإلكترونية
        • تحويل ملفات Excel إلى تطبيقات ويب تفاعلية
        • أتمتة العمليات التجارية
        • تحليل البيانات وإعداد التقارير
        
        **شغفي:** بناء حلول تقنية تلبي احتياجات السوق العربي وتواكب التحول الرقمي.
        ''',
        'skills': 'المهارات',
        'projects': 'المشاريع',
        'contact': 'التواصل',
        'view_demo': 'عرض تجريبي',
        'view_code': 'عرض الكود',
        'download_cv': 'تحميل السيرة الذاتية',
        'get_in_touch': 'تواصل معي',
        'email': 'البريد الإلكتروني',
        'whatsapp': 'واتساب',
        'linkedin': 'لينكدإن',
        'github': 'جيت هاب',
        'live_project': 'المشروع الحي',
        'sales_dashboard': 'لوحة تحليل المبيعات',
        'dashboard_desc': 'لوحة تحكم تفاعلية لتحليل بيانات المبيعات والعملاء',
        'excel_converter': 'محول Excel إلى WebApp',
        'excel_desc': 'أداة لتحويل ملفات Excel إلى تطبيقات ويب تفاعلية',
        'hr_system': 'نظام الموارد البشرية',
        'hr_desc': 'منصة متكاملة لإدارة الموظفين والرواتب',
        'ecommerce': 'منصة التجارة الإلكترونية',
        'ecommerce_desc': 'لوحة تحكم متقدمة لمتجر إلكتروني'
    },
    'en': {
        'title': 'Aseel Alzawahreh | Interactive Dashboard Developer',
        'hero_title': 'Aseel Alzawahreh',
        'hero_subtitle': 'Interactive Dashboard Developer | Process Automation',
        'about': 'About Me',
        'about_content': '''
        A developer specializing in transforming traditional data into interactive web applications using Streamlit and Python.
        
        **My Specialties:**
        • Developing dashboards for sales and e-commerce
        • Converting Excel files into interactive web applications
        • Business process automation
        • Data analysis and reporting
        
        **My Passion:** Building technical solutions that meet the needs of the Arab market and keep pace with digital transformation.
        ''',
        'skills': 'Skills',
        'projects': 'Projects',
        'contact': 'Contact',
        'view_demo': 'View Demo',
        'view_code': 'View Code',
        'download_cv': 'Download CV',
        'get_in_touch': 'Get in Touch',
        'email': 'Email',
        'whatsapp': 'WhatsApp',
        'linkedin': 'LinkedIn',
        'github': 'GitHub',
        'live_project': 'Live Project',
        'sales_dashboard': 'Sales Analysis Dashboard',
        'dashboard_desc': 'Interactive dashboard for analyzing sales and customer data',
        'excel_converter': 'Excel to WebApp Converter',
        'excel_desc': 'Tool to convert Excel files into interactive web applications',
        'hr_system': 'HR Management System',
        'hr_desc': 'Integrated platform for employee and payroll management',
        'ecommerce': 'E-commerce Platform',
        'ecommerce_desc': 'Advanced dashboard for online stores'
    }
}

# CSS بسيط
def local_css():
    st.markdown("""
    <style>
    /* تصميم نظيف */
    .main {
        padding: 0 1rem;
    }
    
    /* تباين واضح للنص */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* إزالة الهوامش الزائدة */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* تخصيص الأزرار */
    .stButton > button {
        background-color: #2c3e50;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: 500;
    }
    
    .stButton > button:hover {
        background-color: #1a252f;
    }
    
    /* تخصيص التبويبات */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
    }
    
    /* تصميم البطاقات */
    .project-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #2c3e50;
    }
    
    /* تصميم المهارات */
    .skill-item {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        box-shadow: 0 1px 5px rgba(0,0,0,0.1);
    }
    
    </style>
    """, unsafe_allow_html=True)

local_css()

# دالة لتحميل الصورة الشخصية
def load_profile_image():
    try:
        # جرب تحميل الصورة الشخصية
        image = Image.open("profile.jpg")
        return image
    except:
        try:
            # جرب تحميل من مجلد assets
            image = Image.open("assets/profile.jpg")
            return image
        except:
            # أنشئ صورة افتراضية
            st.markdown("""
            <div style='text-align: center; margin: 2rem 0;'>
                <div style='width: 150px; height: 150px; background: #2c3e50; 
                            border-radius: 50%; display: inline-flex; 
                            align-items: center; justify-content: center; 
                            color: white; font-size: 3rem;'>
                    A
                </div>
            </div>
            """, unsafe_allow_html=True)
            return None

# شريط جانبي للتحكم
with st.sidebar:
    # زر تبديل اللغة
    if st.button("🇸🇦 العربية" if st.session_state.language == 'en' else "🇺🇸 English"):
        st.session_state.language = 'ar' if st.session_state.language == 'en' else 'en'
        st.rerun()
    
    st.markdown("---")
    
    # القائمة الرئيسية
    st.markdown("### **📍 التنقل**" if st.session_state.language == 'ar' else "### **📍 Navigation**")
    
    # تحميل الصورة الشخصية في الشريط الجانبي
    profile_img = load_profile_image()
    if profile_img:
        st.image(profile_img, width=150)
    
    st.markdown("---")
    
    # معلومات الاتصال في الشريط الجانبي
    lang = st.session_state.language
    st.markdown(f"**📧 {translations[lang]['email']}:**")
    st.markdown("aseeljalal45@gmail.com")
    
    st.markdown(f"**📱 {translations[lang]['whatsapp']}:**")
    st.markdown("+962785094075")
    
    st.markdown("---")
    
    # روابط سريعة
    st.markdown(f"**🔗 {translations[lang]['linkedin']}:**")
    st.markdown("[linkedin.com/in/aseel-alzawahreh](https://linkedin.com)")
    
    st.markdown(f"**💻 {translations[lang]['github']}:**")
    st.markdown("[github.com/aseeljalal44-stack](https://github.com/aseeljalal44-stack/Salesdashboard)")
    
    st.markdown(f"**🚀 {translations[lang]['live_project']}:**")
    st.markdown("[salesdashboards.streamlit.app](https://salesdashboards.streamlit.app/)")

# المحتوى الرئيسي
lang = st.session_state.language
t = translations[lang]

# قسم البطل
col1, col2 = st.columns([3, 1])

with col1:
    st.title(t['hero_title'])
    st.markdown(f"### {t['hero_subtitle']}")
    
    # أزرار سريعة
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button(t['view_demo']):
            st.markdown(f"[{t['sales_dashboard']}](https://salesdashboards.streamlit.app/)")
    with col_b:
        if st.button(t['view_code']):
            st.markdown(f"[GitHub](https://github.com/aseeljalal44-stack/Salesdashboard)")
    with col_c:
        if st.button(t['download_cv']):
            st.info("CV will be available soon")

st.markdown("---")

# تبويبات للمحتوى الرئيسي
tab1, tab2, tab3, tab4 = st.tabs([
    f"👤 {t['about']}",
    f"💪 {t['skills']}",
    f"🚀 {t['projects']}",
    f"📞 {t['contact']}"
])

with tab1:
    # قسم عني
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(t['about_content'])
    
    with col2:
        # عرض صورة شخصية كبيرة إذا كانت موجودة
        if profile_img:
            st.image(profile_img, use_column_width=True)
        
        # مؤشرات سريعة
        st.markdown("""
        <div style='background: white; padding: 1.5rem; border-radius: 10px;'>
            <h4 style='color: #2c3e50;'>📊 إنجازات سريعة</h4>
            <p>✅ 15+ مشروع مكتمل</p>
            <p>✅ 8+ مجالات مختلفة</p>
            <p>✅ 100% رضا عملاء</p>
            <p>✅ 50+ لوحة تحكم</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    # قسم المهارات المبسط
    st.markdown("### 💻 **المهارات التقنية الأساسية**")
    
    cols = st.columns(3)
    
    skills = [
        ("Streamlit", "تطوير تطبيقات ويب تفاعلية", 95),
        ("Python", "برمجة وتحليل البيانات", 92),
        ("Pandas", "معالجة وتحليل البيانات", 90),
        ("Plotly", "تصور البيانات التفاعلي", 88),
        ("Excel Automation", "أتمتة ملفات Excel", 85),
        ("Arabic UI/UX", "تصميم واجهات عربية", 90)
    ] if lang == 'ar' else [
        ("Streamlit", "Interactive web applications", 95),
        ("Python", "Programming & data analysis", 92),
        ("Pandas", "Data processing & analysis", 90),
        ("Plotly", "Interactive data visualization", 88),
        ("Excel Automation", "Excel file automation", 85),
        ("Arabic UI/UX", "Arabic interface design", 90)
    ]
    
    for idx, (skill, desc, level) in enumerate(skills):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class='skill-item'>
                <h4>{skill}</h4>
                <p style='color: #666; font-size: 0.9rem;'>{desc}</p>
                <div style='background: #e0e0e0; border-radius: 5px; height: 8px; margin: 10px 0;'>
                    <div style='background: #2c3e50; width: {level}%; height: 100%; border-radius: 5px;'></div>
                </div>
                <span style='color: #2c3e50; font-weight: bold;'>{level}%</span>
            </div>
            """, unsafe_allow_html=True)

with tab3:
    # قسم المشاريع
    st.markdown(f"### 🚀 **{t['projects']}**")
    
    # مشروع لوحة المبيعات (الحقيقي)
    st.markdown(f"""
    <div class='project-card'>
        <h3>📊 {t['sales_dashboard']}</h3>
        <p>{t['dashboard_desc']}</p>
        
        <div style='display: flex; gap: 10px; margin-top: 15px;'>
            <a href='https://salesdashboards.streamlit.app/' target='_blank' 
               style='background: #2c3e50; color: white; padding: 8px 16px; 
                      border-radius: 5px; text-decoration: none;'>
               🌐 {t['view_demo']}
            </a>
            <a href='https://github.com/aseeljalal44-stack/Salesdashboard' target='_blank'
               style='background: #333; color: white; padding: 8px 16px; 
                      border-radius: 5px; text-decoration: none;'>
               💻 {t['view_code']}
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # مشاريع أخرى
    projects = [
        (t['excel_converter'], t['excel_desc']),
        (t['hr_system'], t['hr_desc']),
        (t['ecommerce'], t['ecommerce_desc'])
    ]
    
    for project_title, project_desc in projects:
        st.markdown(f"""
        <div class='project-card'>
            <h3>✨ {project_title}</h3>
            <p>{project_desc}</p>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    # قسم التواصل
    st.markdown(f"### 📞 **{t['get_in_touch']}**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # نموذج الاتصال
        st.markdown(f"#### ✉️ {t['get_in_touch']}")
        
        with st.form("contact_form"):
            name = st.text_input("الاسم" if lang == 'ar' else "Name")
            email = st.text_input("البريد الإلكتروني" if lang == 'ar' else "Email")
            message = st.text_area("الرسالة" if lang == 'ar' else "Message", height=150)
            
            submitted = st.form_submit_button("إرسال" if lang == 'ar' else "Send")
            
            if submitted:
                if name and email and message:
                    st.success("شكراً! سأتصل بك قريباً." if lang == 'ar' else "Thanks! I'll contact you soon.")
                else:
                    st.warning("يرجى ملء جميع الحقول" if lang == 'ar' else "Please fill all fields")
    
    with col2:
        # معلومات الاتصال
        st.markdown(f"""
        <div style='background: white; padding: 2rem; border-radius: 10px;'>
            <h4>📍 {t['contact']}</h4>
            
            <div style='margin: 1.5rem 0;'>
                <p><strong>📧 {t['email']}:</strong></p>
                <p>aseeljalal45@gmail.com</p>
            </div>
            
            <div style='margin: 1.5rem 0;'>
                <p><strong>📱 {t['whatsapp']}:</strong></p>
                <p>+962785094075</p>
                <a href='https://wa.me/962785094075' target='_blank' 
                   style='background: #25D366; color: white; padding: 8px 16px; 
                          border-radius: 5px; text-decoration: none; display: inline-block; margin-top: 5px;'>
                   📲 ارسل رسالة
                </a>
            </div>
            
            <div style='margin: 1.5rem 0;'>
                <p><strong>💼 {t['linkedin']}:</strong></p>
                <a href='https://linkedin.com'>linkedin.com/in/aseel-alzawahreh</a>
            </div>
            
            <div style='margin: 1.5rem 0;'>
                <p><strong>💻 {t['github']}:</strong></p>
                <a href='https://github.com/aseeljalal44-stack'>github.com/aseeljalal44-stack</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

# الفوتر
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>© 2024 أسيل الزواهرة | Aseel Alzawahreh</p>
    <p>مطور لوحات تحكم تفاعلية باستخدام Streamlit و Python</p>
    <p>Interactive Dashboard Developer using Streamlit & Python</p>
</div>
""", unsafe_allow_html=True)