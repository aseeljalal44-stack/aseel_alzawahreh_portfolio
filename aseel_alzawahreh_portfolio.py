import streamlit as st
import base64
from pathlib import Path

# إعدادات الصفحة
st.set_page_config(
    page_title="Aseel Alzawahreh | Portfolio",
    page_icon="🚀",
    layout="centered",
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
        'tagline': 'تحويل البيانات إلى رؤى، والأفكار إلى تطبيقات',
        
        # عني
        'about_title': 'مرحباً، أنا أسيل 👋',
        'about_text': '''
        مطور متخصص في بناء لوحات التحكم التفاعلية وتطبيقات تحليل البيانات.
        
        **أعمل على:**
        • تطوير لوحات تحكم للمبيعات والتجارة الإلكترونية
        • تحويل ملفات Excel إلى تطبيقات ويب
        • أتمتة العمليات التجارية
        • تحليل البيانات وإعداد التقارير
        
        **التقنيات الرئيسية:** Streamlit, Python, Pandas, Plotly
        ''',
        
        # المهارات
        'skills_title': 'مهاراتي التقنية',
        'skill1': 'Streamlit',
        'skill1_desc': 'تطوير تطبيقات ويب تفاعلية',
        'skill2': 'Python',
        'skill2_desc': 'برمجة وتحليل البيانات',
        'skill3': 'Pandas',
        'skill3_desc': 'معالجة وتحليل البيانات',
        'skill4': 'Plotly',
        'skill4_desc': 'تصور البيانات التفاعلي',
        'skill5': 'Excel Automation',
        'skill5_desc': 'أتمتة ملفات Excel',
        'skill6': 'Arabic UI/UX',
        'skill6_desc': 'تصميم واجهات عربية',
        
        # المشاريع
        'projects_title': 'مشاريعي',
        'project1_title': 'لوحة تحليل المبيعات',
        'project1_desc': 'لوحة تحكم تفاعلية لتحليل بيانات المبيعات والعملاء',
        'project2_title': 'محول Excel إلى WebApp',
        'project2_desc': 'أداة لتحويل ملفات Excel إلى تطبيقات ويب',
        'project3_title': 'نظام الموارد البشرية',
        'project3_desc': 'منصة لإدارة الموظفين والرواتب',
        'project4_title': 'منصة التجارة الإلكترونية',
        'project4_desc': 'لوحة تحكم متقدمة للمتاجر الإلكترونية',
        'view_live': 'عرض التطبيق',
        'view_code': 'عرض الكود',
        
        # التواصل
        'contact_title': 'لنعمل معاً',
        'contact_text': 'مستعد لمشروعك القادم؟ تواصل معي',
        'email': 'البريد الإلكتروني',
        'whatsapp': 'واتساب',
        'github': 'GitHub',
        'send_message': 'إرسال رسالة',
        
        # الفوتر
        'footer': '© 2024 أسيل الزواهرة. جميع الحقوق محفوظة.'
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
        'tagline': 'Turning data into insights, ideas into applications',
        
        # About
        'about_title': 'Hi, I\'m Aseel 👋',
        'about_text': '''
        A developer specializing in building interactive dashboards and data analysis applications.
        
        **I work on:**
        • Developing dashboards for sales and e-commerce
        • Converting Excel files to web applications
        • Business process automation
        • Data analysis and reporting
        
        **Main Technologies:** Streamlit, Python, Pandas, Plotly
        ''',
        
        # Skills
        'skills_title': 'Technical Skills',
        'skill1': 'Streamlit',
        'skill1_desc': 'Interactive web applications',
        'skill2': 'Python',
        'skill2_desc': 'Programming & data analysis',
        'skill3': 'Pandas',
        'skill3_desc': 'Data processing & analysis',
        'skill4': 'Plotly',
        'skill4_desc': 'Interactive data visualization',
        'skill5': 'Excel Automation',
        'skill5_desc': 'Excel file automation',
        'skill6': 'Arabic UI/UX',
        'skill6_desc': 'Arabic interface design',
        
        # Projects
        'projects_title': 'My Projects',
        'project1_title': 'Sales Analysis Dashboard',
        'project1_desc': 'Interactive dashboard for sales and customer data analysis',
        'project2_title': 'Excel to WebApp Converter',
        'project2_desc': 'Tool to convert Excel files to web applications',
        'project3_title': 'HR Management System',
        'project3_desc': 'Platform for employee and payroll management',
        'project4_title': 'E-commerce Platform',
        'project4_desc': 'Advanced dashboard for online stores',
        'view_live': 'View App',
        'view_code': 'View Code',
        
        # Contact
        'contact_title': "Let's Work Together",
        'contact_text': 'Ready for your next project? Get in touch',
        'email': 'Email',
        'whatsapp': 'WhatsApp',
        'github': 'GitHub',
        'send_message': 'Send Message',
        
        # Footer
        'footer': '© 2024 Aseel Alzawahreh. All rights reserved.'
    }
}

# CSS ديناميكي للثيم
def get_css(theme):
    if theme == 'dark':
        return """
        <style>
        /* الثيم الداكن */
        :root {
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --accent: #3b82f6;
            --border: #334155;
        }
        
        .stApp {
            background-color: var(--bg-primary);
            color: var(--text-primary);
        }
        
        .card {
            background-color: var(--bg-secondary);
            border: 1px solid var(--border);
        }
        
        h1, h2, h3, h4 {
            color: var(--text-primary);
        }
        
        p {
            color: var(--text-secondary);
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
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --accent: #2563eb;
            --border: #e2e8f0;
        }
        
        .stApp {
            background-color: var(--bg-primary);
            color: var(--text-primary);
        }
        
        .card {
            background-color: var(--bg-secondary);
            border: 1px solid var(--border);
        }
        
        h1, h2, h3, h4 {
            color: var(--text-primary);
        }
        
        p {
            color: var(--text-secondary);
        }
        </style>
        """

# دالة لتحميل الصورة
def load_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# شريط التحكم العلوي
def render_controls():
    col1, col2, col3, col4 = st.columns([6, 1, 1, 1])
    
    with col2:
        # زر تبديل اللغة
        if st.button("عربى" if st.session_state.language == 'en' else "EN", 
                    help="تبديل اللغة"):
            st.session_state.language = 'ar' if st.session_state.language == 'en' else 'en'
            st.rerun()
    
    with col3:
        # زر تبديل الثيم
        theme_icon = "🌙" if st.session_state.theme == 'light' else "☀️"
        if st.button(theme_icon, help="تبديل الثيم"):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()
    
    return col1

# الهيدر الرئيسي
def render_header(lang):
    c = content[lang]
    
    # محاولة تحميل الصورة الشخصية
    img_b64 = load_image("profile.jpg") or load_image("assets/profile.jpg")
    
    col1, col2 = st.columns([2, 1], vertical_alignment="center")
    
    with col1:
        st.title(c['title'])
        st.markdown(f"### {c['subtitle']}")
        st.markdown(f"*{c['tagline']}*")
        
        # روابط سريعة
        st.markdown("---")
        cols = st.columns(4)
        with cols[0]:
            st.markdown(f"[🌐 {c['nav_about']}](#about)", unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f"[💼 {c['nav_projects']}](#projects)", unsafe_allow_html=True)
        with cols[2]:
            st.markdown(f"[📧 {c['nav_contact']}](#contact)", unsafe_allow_html=True)
        with cols[3]:
            st.markdown(f"[💻 GitHub](https://github.com/aseeljalal44-stack)")
    
    with col2:
        if img_b64:
            st.markdown(f"""
            <div style="text-align: center; margin-top: 1rem;">
                <img src="data:image/jpeg;base64,{img_b64}" 
                     style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover; border: 3px solid var(--accent);">
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; margin-top: 1rem;">
                <div style="width: 150px; height: 150px; border-radius: 50%; 
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            display: inline-flex; align-items: center; 
                            justify-content: center; color: white; font-size: 3rem;
                            border: 3px solid var(--accent);">
                    A
                </div>
            </div>
            """, unsafe_allow_html=True)

# قسم عني
def render_about(lang):
    c = content[lang]
    
    st.markdown(f"## 👤 {c['about_title']}")
    st.markdown(c['about_text'])
    
    # معلومات سريعة
    st.markdown("---")
    
    cols = st.columns(4)
    with cols[0]:
        st.metric("المشاريع", "15+")
    with cols[1]:
        st.metric("العملاء", "12+")
    with cols[2]:
        st.metric("الخبرة", "2+ سنة")
    with cols[3]:
        st.metric("التقنيات", "8+")

# قسم المهارات
def render_skills(lang):
    c = content[lang]
    
    st.markdown(f"## 💪 {c['skills_title']}")
    
    # تنظيم المهارات في شبكة
    cols = st.columns(3)
    
    skills = [
        (c['skill1'], c['skill1_desc'], 95),
        (c['skill2'], c['skill2_desc'], 92),
        (c['skill3'], c['skill3_desc'], 90),
        (c['skill4'], c['skill4_desc'], 88),
        (c['skill5'], c['skill5_desc'], 85),
        (c['skill6'], c['skill6_desc'], 90)
    ]
    
    for idx, (skill, desc, level) in enumerate(skills):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="card" style="padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong>{skill}</strong>
                    <span style="color: var(--accent); font-weight: bold;">{level}%</span>
                </div>
                <p style="font-size: 0.9rem; margin: 0.5rem 0;">{desc}</p>
                <div style="height: 6px; background: var(--border); border-radius: 3px; overflow: hidden;">
                    <div style="height: 100%; width: {level}%; background: var(--accent);"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# قسم المشاريع
def render_projects(lang):
    c = content[lang]
    
    st.markdown(f"## 🚀 {c['projects_title']}")
    
    # مشروع رئيسي (حقيقي)
    st.markdown(f"""
    <div class="card" style="padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem;">
        <h3 style="color: var(--accent); margin-bottom: 0.5rem;">📊 {c['project1_title']}</h3>
        <p style="margin-bottom: 1rem;">{c['project1_desc']}</p>
        
        <div style="display: flex; gap: 1rem;">
            <a href="https://salesdashboards.streamlit.app/" target="_blank"
               style="background: var(--accent); color: white; padding: 0.5rem 1rem; 
                      border-radius: 6px; text-decoration: none; font-weight: 500;">
               🌐 {c['view_live']}
            </a>
            <a href="https://github.com/aseeljalal44-stack/Salesdashboard" target="_blank"
               style="background: var(--bg-secondary); color: var(--text-primary); 
                      padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; 
                      font-weight: 500; border: 1px solid var(--border);">
               💻 {c['view_code']}
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # مشاريع أخرى
    projects = [
        (c['project2_title'], c['project2_desc']),
        (c['project3_title'], c['project3_desc']),
        (c['project4_title'], c['project4_desc'])
    ]
    
    cols = st.columns(3)
    for idx, (title, desc) in enumerate(projects):
        with cols[idx]:
            st.markdown(f"""
            <div class="card" style="padding: 1rem; border-radius: 10px; height: 100%;">
                <h4 style="color: var(--accent); margin-bottom: 0.5rem;">✨ {title}</h4>
                <p style="font-size: 0.9rem;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# قسم التواصل
def render_contact(lang):
    c = content[lang]
    
    st.markdown(f"## 📞 {c['contact_title']}")
    st.markdown(c['contact_text'])
    
    # معلومات الاتصال
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="card" style="padding: 1.5rem; border-radius: 10px;">
            <h4 style="color: var(--accent); margin-bottom: 1rem;">📬 {c['contact_title']}</h4>
            
            <div style="margin-bottom: 1rem;">
                <strong>📧 {c['email']}:</strong><br>
                <code>aseeljalal45@gmail.com</code>
            </div>
            
            <div style="margin-bottom: 1rem;">
                <strong>📱 {c['whatsapp']}:</strong><br>
                +962 78 509 4075
            </div>
            
            <div>
                <strong>💻 {c['github']}:</strong><br>
                <a href="https://github.com/aseeljalal44-stack" target="_blank">
                    github.com/aseeljalal44-stack
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # نموذج اتصال بسيط
        with st.form("contact_form"):
            st.markdown(f"#### ✉️ {c['send_message']}")
            
            name = st.text_input("الاسم" if lang == 'ar' else "Name")
            email = st.text_input("البريد الإلكتروني" if lang == 'ar' else "Email")
            message = st.text_area("الرسالة" if lang == 'ar' else "Message", height=100)
            
            submitted = st.form_submit_button(c['send_message'])
            
            if submitted:
                if name and email and message:
                    st.success("تم إرسال رسالتك بنجاح!" if lang == 'ar' else "Message sent successfully!")
                else:
                    st.warning("يرجى ملء جميع الحقول" if lang == 'ar' else "Please fill all fields")

# الفوتر
def render_footer(lang):
    c = content[lang]
    
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0; color: var(--text-secondary);">
        <p>{c['footer']}</p>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">
            Built with ❤️ using Streamlit & Python
        </p>
    </div>
    """, unsafe_allow_html=True)

# التطبيق الرئيسي
def main():
    # تطبيق CSS
    st.markdown(get_css(st.session_state.theme), unsafe_allow_html=True)
    
    # شريط التحكم
    render_controls()
    
    # المحتوى
    lang = st.session_state.language
    c = content[lang]
    
    # الهيدر
    render_header(lang)
    
    st.markdown("---")
    
    # الأقسام
    render_about(lang)
    st.markdown("---")
    render_skills(lang)
    st.markdown("---")
    render_projects(lang)
    st.markdown("---")
    render_contact(lang)
    
    # الفوتر
    render_footer(lang)

if __name__ == "__main__":
    main()