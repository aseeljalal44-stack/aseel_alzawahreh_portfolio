import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
import base64
from io import BytesIO
import json
import openpyxl

# إعدادات الصفحة
st.set_page_config(
    page_title="أسيل الزواهرة | مطور لوحات تحكم تفاعلية",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS مخصص
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Cairo', sans-serif !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 20px;
        margin: 1rem;
        padding: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    
    /* الهيدر */
    .hero-section {
        background: linear-gradient(135deg, #1a237e 0%, #311b92 100%);
        border-radius: 20px;
        padding: 4rem 2rem;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0,0 L100,0 L100,100 Z" fill="rgba(255,255,255,0.05)"/></svg>');
        background-size: cover;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        background: linear-gradient(45deg, #fff, #bbdefb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
    }
    
    .hero-subtitle {
        font-size: 1.6rem;
        opacity: 0.95;
        margin-bottom: 1.5rem;
        color: #e3f2fd;
        position: relative;
    }
    
    /* التصميم العام */
    h1, h2, h3, h4 {
        color: #1a237e;
    }
    
    /* البطاقات */
    .custom-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        border: 1px solid rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .custom-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, #667eea, #764ba2, #1a237e);
    }
    
    .custom-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 60px rgba(0,0,0,0.25);
    }
    
    .card-title {
        color: #1a237e;
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 15px;
        font-weight: 800;
    }
    
    /* الأزرار */
    .stButton>button {
        background: linear-gradient(135deg, #1a237e 0%, #311b92 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2.5rem;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.3s;
        box-shadow: 0 6px 20px rgba(26, 35, 126, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.03);
        box-shadow: 0 12px 30px rgba(26, 35, 126, 0.4);
    }
    
    /* التبويبات */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        padding: 0 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f5f7ff;
        border-radius: 12px;
        padding: 15px 30px;
        font-weight: 700;
        border: 2px solid transparent;
        transition: all 0.3s;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1a237e 0%, #311b92 100%) !important;
        color: white !important;
        border: 2px solid white !important;
        box-shadow: 0 8px 25px rgba(26, 35, 126, 0.3);
        transform: translateY(-2px);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        border-color: #1a237e;
    }
    
    </style>
    """, unsafe_allow_html=True)

local_css()

# بيانات المطور
developer_info = {
    "name": "أسيل الزواهرة",
    "name_english": "Aseel Alzawahreh",
    "title": "مطور لوحات تحكم تفاعلية | أتمتة العمليات | تحويل Excel إلى WebApp",
    "tagline": "محول البيانات إلى رؤى، ومطور الحلول التفاعلية",
    "about": """
    **مطور متخصص في تحويل البيانات التقليدية إلى تطبيقات ويب تفاعلية باستخدام Streamlit و Python.**

    أمتلك خبرة واسعة في تطوير لوحات التحكم الاحترافية لمختلف المجالات:
    
    **🎯 تخصصاتي الرئيسية:**
    • **لوحات تحليل المبيعات**: تحليل شامل للمبيعات، تتبع الطلبات، تحليل العملاء (RFM)
    • **أنظمة التجارة الإلكترونية**: متابعة المخزون، تحليل المنتجات، تقارير الربحية
    • **أنظمة الموارد البشرية**: إدارة الموظفين، الرواتب، التقييمات، الحضور والانصراف
    • **تحويل ملفات Excel**: تحويل التقارير الورقية إلى تطبيقات ويب تفاعلية
    
    **💡 رؤيتي:**
    تحويل العمليات اليدوية المعقدة إلى أنظمة تلقائية سهلة الاستخدام، مما يوفر الوقت ويقلل الأخطاء ويزيد من كفاءة العمل.
    
    **🚀 شغفي:**
    بناء حلول تقنية تواكب العصر الرقمي وتلبي احتياجات السوق المحلي والعربي.
    """,
    "skills": {
        "Streamlit Development": 95,
        "Python Programming": 92,
        "Data Analysis & Visualization": 90,
        "Dashboard Design": 88,
        "Excel to WebApp Conversion": 85,
        "Arabic UI/UX Design": 90,
        "Database Integration": 82,
        "Business Intelligence": 87
    },
    "tech_stack": ["Streamlit", "Python", "Pandas", "Plotly", "NumPy", "SQL", "OpenPyXL", "Altair", "Matplotlib", "SciPy"],
    "projects": [
        {
            "name": "لوحة تحليل المبيعات الاحترافية",
            "domain": "المبيعات والتجارة الإلكترونية",
            "description": "نظام تحليل متكامل لبيانات المبيعات مع تحليل RFM للعملاء وتوزيع المنتجات",
            "features": ["تحميل CSV/Excel", "فلاتر زمنية", "تحليل RFM", "توزيع جغرافي", "تقارير تفاعلية"],
            "live_url": "https://salesdashboards.streamlit.app/",
            "github_url": "https://github.com/aseeljalal44-stack/Salesdashboard"
        },
        {
            "name": "نظام إدارة الموارد البشرية",
            "domain": "الموارد البشرية",
            "description": "منصة متكاملة لإدارة الموظفين، الرواتب، الإجازات، والتقييمات",
            "features": ["إدارة الموظفين", "تتبع الحضور", "حساب الرواتب", "تقييم الأداء", "تقارير HR"]
        },
        {
            "name": "منصة التجارة الإلكترونية",
            "domain": "التجارة الإلكترونية",
            "description": "لوحة تحكم متقدمة لمتجر إلكتروني مع تحليل المبيعات والعملاء والمخزون",
            "features": ["تحليل المبيعات", "إدارة المخزون", "تحليل العملاء", "تتبع الطلبات", "تحليل الربحية"]
        },
        {
            "name": "محول Excel إلى WebApp",
            "domain": "أتمتة العمليات",
            "description": "أداة لتحويل ملفات Excel التقليدية إلى تطبيقات ويب تفاعلية بدون كتابة كود",
            "features": ["تحميل Excel", "معالجة تلقائية", "واجهة تفاعلية", "تصدير التقارير", "مشاركة التطبيق"]
        }
    ],
    "contact": {
        "email": "aseeljalal45@gmail.com",
        "whatsapp": "+962785094075",
        "linkedin": "https://linkedin.com/in/aseel-alzawahreh",
        "github": "https://github.com/aseeljalal44-stack",
        "portfolio": "https://aseel-portfolio.streamlit.app"
    },
    "services": [
        "تطوير لوحات تحكم تفاعلية مخصصة",
        "تحويل ملفات Excel إلى تطبيقات ويب",
        "أتمتة العمليات التجارية",
        "تحليل البيانات واستخراج التقارير",
        "تصميم واجهات عربية احترافية",
        "استشارات تقنية للشركات الناشئة"
    ]
}

# الهيدر الرئيسي
def render_hero():
    st.markdown(f"""
    <div class="hero-section">
        <h1 class="hero-title">👨‍💻 {developer_info['name']}</h1>
        <p class="hero-subtitle">{developer_info['title']}</p>
        <div style="margin-top: 2rem; font-size: 1.3rem; color: #e3f2fd;">
            {developer_info['tagline']}
        </div>
        <div style="margin-top: 2rem;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.7rem 2rem; border-radius: 50px; margin: 0.5rem; display: inline-block; font-weight: 600;">
                ✨ محول Excel إلى تطبيقات ويب
            </span>
            <span style="background: rgba(255,255,255,0.2); padding: 0.7rem 2rem; border-radius: 50px; margin: 0.5rem; display: inline-block; font-weight: 600;">
                🚀 متخصص في Streamlit
            </span>
            <span style="background: rgba(255,255,255,0.2); padding: 0.7rem 2rem; border-radius: 50px; margin: 0.5rem; display: inline-block; font-weight: 600;">
                📊 مطور لوحات تحكم تفاعلية
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# قسم عني
def render_about():
    st.markdown("## 👤 عني")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="custom-card">
            <h3 style="color: #1a237e; margin-bottom: 1.5rem; border-bottom: 3px solid #1a237e; padding-bottom: 0.5rem;">🎯 من أنا؟</h3>
            <div style="font-size: 1.1rem; line-height: 1.9; color: #424242;">
            {developer_info['about']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="custom-card" style="text-align: center;">
            <h3 style="color: #1a237e; margin-bottom: 1.5rem;">📈 إحصائياتي</h3>
            <div style="background: linear-gradient(135deg, #f5f7ff, #ffffff); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
                <div style="font-size: 2.8rem; font-weight: 900; color: #1a237e; margin-bottom: 0.5rem;">15+</div>
                <div style="color: #666; font-weight: 600;">مشروع مكتمل</div>
            </div>
            <div style="background: linear-gradient(135deg, #f5f7ff, #ffffff); padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
                <div style="font-size: 2.8rem; font-weight: 900; color: #1a237e; margin-bottom: 0.5rem;">8+</div>
                <div style="color: #666; font-weight: 600;">مجالات مختلفة</div>
            </div>
            <div style="background: linear-gradient(135deg, #f5f7ff, #ffffff); padding: 1.5rem; border-radius: 15px;">
                <div style="font-size: 2.8rem; font-weight: 900; color: #1a237e; margin-bottom: 0.5rem;">100%</div>
                <div style="color: #666; font-weight: 600;">رضا العملاء</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# عرض المهارات
def render_skills():
    st.markdown("## 💪 مهاراتي التقنية")
    
    st.markdown("### 🔧 التقنيات التي أستخدمها")
    
    tech_html = ""
    for tech in developer_info['tech_stack']:
        tech_html += f'<span style="background: linear-gradient(135deg, #1a237e, #311b92); color: white; padding: 0.6rem 1.4rem; border-radius: 25px; margin: 0.3rem; display: inline-block; font-weight: 600; box-shadow: 0 4px 15px rgba(26, 35, 126, 0.2);">{tech}</span> '
    
    st.markdown(f'<div style="margin-bottom: 3rem; text-align: center;">{tech_html}</div>', unsafe_allow_html=True)
    
    # أشرطة المهارات
    st.markdown("### 📊 مستوى المهارات")
    
    cols = st.columns(2)
    skills = developer_info['skills']
    
    for idx, (skill, level) in enumerate(skills.items()):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem; box-shadow: 0 5px 20px rgba(0,0,0,0.08);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.8rem;">
                    <span style="font-weight: 700; color: #1a237e;">{skill}</span>
                    <span style="font-weight: 700; color: #1a237e;">{level}%</span>
                </div>
                <div style="background-color: #e8eaf6; border-radius: 10px; height: 10px; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, #1a237e, #311b92); height: 100%; width: {level}%; border-radius: 10px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# عرض المشاريع
def render_projects():
    st.markdown("## 🚀 مشاريعي")
    
    projects = developer_info['projects']
    
    for project in projects:
        st.markdown(f"""
        <div class="custom-card" style="margin-bottom: 2rem;">
            <div class="card-title">
                <span style="background: #1a237e; color: white; width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem;">
                    {projects.index(project) + 1}
                </span>
                {project['name']}
            </div>
            
            <div style="display: inline-block; background: linear-gradient(135deg, #1a237e, #311b92); color: white; padding: 0.4rem 1.2rem; border-radius: 20px; font-size: 0.95rem; margin-bottom: 1rem; font-weight: 600;">
                {project['domain']}
            </div>
            
            <p style="color: #424242; font-size: 1.1rem; margin-bottom: 1.5rem; line-height: 1.8;">
            {project['description']}
            </p>
            
            <div style="background: #f8f9fa; padding: 1.2rem; border-radius: 12px; margin-bottom: 1.5rem;">
                <div style="color: #1a237e; font-weight: 700; margin-bottom: 0.8rem; font-size: 1.1rem;">المميزات:</div>
                <div style="display: flex; flex-wrap: wrap; gap: 0.6rem;">
        """, unsafe_allow_html=True)
        
        for feature in project['features']:
            st.markdown(f'<span style="background: #e8eaf6; color: #1a237e; padding: 0.4rem 1rem; border-radius: 15px; font-size: 0.9rem; font-weight: 600;">✓ {feature}</span>', unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        # روابط المشروع (إذا كانت موجودة)
        if 'live_url' in project or 'github_url' in project:
            st.markdown("<div style='border-top: 2px solid #e8eaf6; padding-top: 1.2rem;'>", unsafe_allow_html=True)
            if 'live_url' in project:
                st.markdown(f"""
                <a href="{project['live_url']}" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #1a237e; color: white; padding: 0.7rem 1.5rem; border-radius: 25px; text-decoration: none; font-weight: 600; margin-right: 1rem; margin-bottom: 0.5rem;">
                    🌐 عرض التطبيق الحي
                </a>
                """, unsafe_allow_html=True)
            
            if 'github_url' in project:
                st.markdown(f"""
                <a href="{project['github_url']}" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #333; color: white; padding: 0.7rem 1.5rem; border-radius: 25px; text-decoration: none; font-weight: 600; margin-bottom: 0.5rem;">
                    💻 عرض كود المصدر
                </a>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# عرض حي للمشروع الرئيسي
def render_live_demo():
    st.markdown("## 🎬 عرض حي: لوحة تحليل المبيعات")
    
    st.info("""
    **هذا مشروع حقيقي قمت بتنفيذه بالفعل!**  
    يمكنك زيارة التطبيق الحي ورؤية كود المصدر:
    - **🌐 التطبيق الحي:** [salesdashboards.streamlit.app](https://salesdashboards.streamlit.app/)
    - **💻 كود المصدر:** [github.com/aseeljalal44-stack/Salesdashboard](https://github.com/aseeljalal44-stack/Salesdashboard)
    """)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 نظرة عامة", "📈 تحليل المنتجات", "👥 تحليل العملاء", "📁 نموذج البيانات"])
    
    with tab1:
        st.markdown("### لوحة تحليل المبيعات الاحترافية")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # بيانات وهمية للمبيعات الشهرية
            sales_data = pd.DataFrame({
                'الشهر': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر'],
                'المبيعات': [150000, 180000, 220000, 195000, 240000, 280000, 310000, 290000, 330000, 350000, 380000, 420000],
                'الطلبات': [120, 145, 180, 160, 200, 230, 250, 240, 270, 290, 310, 340]
            })
            
            fig = px.line(sales_data, x='الشهر', y='المبيعات', 
                         title='تطور المبيعات الشهري خلال السنة',
                         markers=True)
            fig.update_traces(line=dict(width=4, color='#1a237e'))
            fig.update_layout(plot_bgcolor='white')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.metric("🏆 إجمالي المبيعات السنوية", "3,265,000 ر.س", "+23%")
            st.metric("📦 إجمالي الطلبات", "2,935 طلب", "+18%")
            st.metric("👥 متوسط قيمة الطلب", "1,112 ر.س", "+8%")
            st.metric("📈 أعلى شهر مبيعات", "ديسمبر", "420,000 ر.س")
            
            st.markdown("---")
            
            st.markdown("""
            **🎯 مميزات النظام:**
            - تحليل المبيعات الزمني
            - تحليل العملاء RFM
            - توزيع المنتجات والمناطق
            - تنبؤات المبيعات الذكية
            - تقارير قابلة للتحميل
            """)
    
    with tab2:
        st.markdown("### تحليل المنتجات")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # أفضل المنتجات مبيعاً
            products_data = pd.DataFrame({
                'المنتج': ['قابلة أول', 'كاميرا كانون', 'هاتف سامسونج', 'لابتوب ديل', 'سماعات بلوتوث', 'ساعة ذكية', 'تابلت'],
                'الإيرادات': [943485, 840905, 800966, 707723, 664474, 550000, 480000],
                'الكمية': [881, 650, 720, 540, 890, 450, 380]
            })
            
            fig = px.bar(products_data, x='الإيرادات', y='المنتج', orientation='h',
                        title='أفضل المنتجات حسب الإيرادات',
                        color='الإيرادات',
                        color_continuous_scale='Viridis')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # توزيع إيرادات المنتجات
            fig = px.pie(products_data, values='الإيرادات', names='المنتج',
                        title='توزيع إيرادات المنتجات',
                        hole=0.4)
            st.plotly_chart(fig, use_container_width=True)
            
            # جدول البيانات
            st.dataframe(products_data.sort_values('الإيرادات', ascending=False), 
                        use_container_width=True)
    
    with tab3:
        st.markdown("### تحليل العملاء")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # تحليل RFM
            rfm_data = pd.DataFrame({
                'RFM Score': ['434', '444', '433', '422', '411', '332', '321', '212'],
                'التصنيف': ['أفضل العملاء', 'عملاء مخلصون', 'عملاء محتملون', 'عملاء عاديون', 
                           'عملاء مهددون', 'عملاء نائمون', 'عملاء جدد', 'عملاء شبه مفقودين'],
                'عدد العملاء': [15, 42, 38, 120, 85, 62, 45, 28]
            })
            
            fig = px.bar(rfm_data, x='عدد العملاء', y='التصنيف', orientation='h',
                        title='توزيع العملاء حسب تحليل RFM',
                        color='عدد العملاء',
                        color_continuous_scale='Plasma')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # أفضل العملاء
            top_customers = pd.DataFrame({
                'العميل': ['شركة التقنية المتحدة', 'مجموعة النور التجارية', 'أكاديمية العلم للتعليم',
                          'مركز النخبة الطبي', 'مؤسسة المستقبل العقارية', 'مجموعة الهدى', 'شركة الأصالة'],
                'الإيرادات': [2688311, 2399252, 2220702, 2164717, 2146777, 2118414, 2027901],
                'عدد الطلبات': [146, 134, 133, 125, 119, 113, 107]
            })
            
            st.dataframe(top_customers, use_container_width=True)
            
            st.markdown("""
            **📊 مؤشرات العملاء:**
            - متوسط تكرار الشراء: 3.2 مرة/شهر
            - معدل الاحتفاظ بالعملاء: 78%
            - متوسط عمر العميل: 14 شهر
            - معدل التحويل: 4.3%
            """)
    
    with tab4:
        st.markdown("### نموذج بيانات Excel للمشروع")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("""
            **📁 نموذج بيانات المشروع:**
            
            يمكنك تحميل نموذج بيانات Excel الذي يستخدمه المشروع لتجربته بنفسك.
            
            **🎯 مميزات الملف:**
            - بيانات مبيعات واقعية
            - متعدد الأوراق
            - تنسيق احترافي
            - جاهز للتحليل
            """)
            
            # زر تحميل ملف تجريبي
            if st.button("📥 تحميل ملف Excel تجريبي"):
                # إنشاء ملف Excel تجريبي
                excel_file = BytesIO()
                
                # إنشاء البيانات
                sales_df = pd.DataFrame({
                    'تاريخ_الطلب': pd.date_range('2024-01-01', periods=100, freq='D'),
                    'رقم_الطلب': [f'ORD{1000+i}' for i in range(100)],
                    'المنتج': np.random.choice(['قابلة أول', 'كاميرا كانون', 'هاتف سامسونج', 'لابتوب ديل', 'سماعات بلوتوث'], 100),
                    'الكمية': np.random.randint(1, 10, 100),
                    'السعر': np.random.uniform(100, 5000, 100).round(2),
                    'العميل': np.random.choice(['شركة التقنية', 'مجموعة النور', 'أكاديمية العلم', 'مركز النخبة'], 100),
                    'المنطقة': np.random.choice(['الشمال', 'الجنوب', 'الشرق', 'الغرب', 'الوسط'], 100)
                })
                
                # حساب الإيرادات
                sales_df['الإيرادات'] = sales_df['الكمية'] * sales_df['السعر']
                
                # إنشاء ملف Excel
                with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
                    sales_df.to_excel(writer, sheet_name='المبيعات', index=False)
                    
                    # إضافة ورقة المنتجات
                    products_df = pd.DataFrame({
                        'المنتج': ['قابلة أول', 'كاميرا كانون', 'هاتف سامسونج', 'لابتوب ديل', 'سماعات بلوتوث'],
                        'التصنيف': ['إلكترونيات', 'إلكترونيات', 'إلكترونيات', 'إلكترونيات', 'إكسسوارات'],
                        'سعر_الشراء': [700, 1200, 2500, 3500, 150],
                        'سعر_البيع': [950, 1600, 3200, 4500, 250],
                        'المخزون': [150, 80, 120, 60, 300]
                    })
                    products_df.to_excel(writer, sheet_name='المنتجات', index=False)
                    
                    # إضافة ورقة العملاء
                    customers_df = pd.DataFrame({
                        'العميل': ['شركة التقنية', 'مجموعة النور', 'أكاديمية العلم', 'مركز النخبة'],
                        'التصنيف': ['شركة', 'شركة', 'مؤسسة', 'مركز'],
                        'تاريخ_التسجيل': ['2023-01-15', '2023-03-20', '2023-05-10', '2023-07-05'],
                        'إجمالي_المشتريات': [2688311, 2399252, 2220702, 2164717],
                        'عدد_الطلبات': [146, 134, 133, 125]
                    })
                    customers_df.to_excel(writer, sheet_name='العملاء', index=False)
                
                excel_file.seek(0)
                
                # زر التحميل
                st.download_button(
                    label="⬇️ انقر لتحميل الملف",
                    data=excel_file,
                    file_name="نموذج_بيانات_المبيعات.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        
        with col2:
            # عرض عينة من البيانات
            sample_data = pd.DataFrame({
                'التاريخ': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
                'المنتج': ['قابلة أول', 'كاميرا كانون', 'هاتف سامسونج', 'لابتوب ديل', 'سماعات بلوتوث'],
                'الكمية': [2, 1, 1, 1, 3],
                'السعر': [950.00, 1600.00, 3200.00, 4500.00, 250.00],
                'الإيرادات': [1900.00, 1600.00, 3200.00, 4500.00, 750.00],
                'العميل': ['شركة التقنية', 'مجموعة النور', 'أكاديمية العلم', 'مركز النخبة', 'شركة التقنية']
            })
            
            st.markdown("**📋 عينة من البيانات:**")
            st.dataframe(sample_data, use_container_width=True)
            
            st.markdown("""
            **📁 هيكل الملف:**
            
            1. **ورقة المبيعات**: تفاصيل جميع الطلبات
            2. **ورقة المنتجات**: معلومات المنتجات والمخزون
            3. **ورقة العملاء**: بيانات العملاء والتاريخ
            4. **ورقة التحليل**: تقارير وتحليلات تلقائية
            """)

# قسم الخدمات
def render_services():
    st.markdown("## 💼 الخدمات التي أقدمها")
    
    services = [
        {
            "icon": "📊",
            "title": "تطوير لوحات التحكم التفاعلية",
            "description": "بناء لوحات تحكم احترافية ومخصصة لمختلف المجالات التجارية",
            "features": ["تصميم عربي احترافي", "تقارير تفاعلية", "تحليل بيانات متقدم", "دعم فني مستمر"]
        },
        {
            "icon": "🔄",
            "title": "تحويل ملفات Excel إلى تطبيقات ويب",
            "description": "تحويل التقارير الورقية وملفات Excel المعقدة إلى تطبيقات ويب تفاعلية",
            "features": ["أتمتة العمليات", "واجهات سهلة الاستخدام", "مشاركة عبر الإنترنت", "تحديثات حية"]
        },
        {
            "icon": "🚀",
            "title": "أتمتة العمليات التجارية",
            "description": "تطوير أنظمة ذكية لأتمتة المهام الروتينية وزيادة الكفاءة",
            "features": ["توفير الوقت والجهد", "تقليل الأخطاء البشرية", "زيادة الإنتاجية", "تقارير تلقائية"]
        },
        {
            "icon": "🎯",
            "title": "تحليل البيانات واستخراج التقارير",
            "description": "تحليل البيانات المعقدة واستخراج رؤى قابلة للتنفيذ لاتخاذ قرارات أفضل",
            "features": ["تحليل إحصائي متقدم", "تنبؤات وتحليلات", "تصور بيانات احترافي", "تقارير مخصصة"]
        }
    ]
    
    cols = st.columns(2)
    
    for idx, service in enumerate(services):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="custom-card">
                <div style="font-size: 2.5rem; margin-bottom: 1rem; color: #1a237e;">
                    {service['icon']}
                </div>
                <div class="card-title">{service['title']}</div>
                <p style="color: #424242; font-size: 1.1rem; margin-bottom: 1.5rem; line-height: 1.7;">
                {service['description']}
                </p>
                <div style="background: #f8f9fa; padding: 1.2rem; border-radius: 12px;">
                    <div style="color: #1a237e; font-weight: 700; margin-bottom: 0.8rem; font-size: 1.1rem;">المميزات:</div>
                    <ul style="padding-right: 1.5rem; color: #424242;">
            """, unsafe_allow_html=True)
            
            for feature in service['features']:
                st.markdown(f'<li style="margin-bottom: 0.5rem; font-size: 1rem;">{feature}</li>', unsafe_allow_html=True)
            
            st.markdown("</ul></div></div>", unsafe_allow_html=True)

# قسم الاتصال
def render_contact():
    st.markdown("## 📞 تواصل معي")
    
    contact_info = developer_info['contact']
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"""
        <div style="background: white; border-radius: 20px; padding: 2rem; box-shadow: 0 10px 40px rgba(0,0,0,0.1);">
            <h3 style="color: #1a237e; margin-bottom: 1.5rem; text-align: center;">🌐 معلومات التواصل</h3>
            
            <div style="margin-bottom: 1.5rem; padding: 1.2rem; background: #f8f9fa; border-radius: 12px;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.8rem;">
                    <span style="font-size: 1.5rem;">📧</span>
                    <span style="font-weight: 600; color: #1a237e;">البريد الإلكتروني</span>
                </div>
                <div style="direction: ltr; text-align: center; font-size: 1.1rem; padding: 0.5rem; background: white; border-radius: 8px;">
                    {contact_info['email']}
                </div>
            </div>
            
            <div style="margin-bottom: 1.5rem; padding: 1.2rem; background: #f8f9fa; border-radius: 12px;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.8rem;">
                    <span style="font-size: 1.5rem;">💬</span>
                    <span style="font-weight: 600; color: #1a237e;">واتساب</span>
                </div>
                <div style="text-align: center; font-size: 1.1rem; padding: 0.5rem; background: white; border-radius: 8px;">
                    {contact_info['whatsapp']}
                </div>
            </div>
            
            <div style="margin-bottom: 1.5rem; padding: 1.2rem; background: #f8f9fa; border-radius: 12px;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.8rem;">
                    <span style="font-size: 1.5rem;">💼</span>
                    <span style="font-weight: 600; color: #1a237e;">LinkedIn</span>
                </div>
                <div style="text-align: center;">
                    <a href="{contact_info['linkedin']}" target="_blank" style="color: #0077b5; text-decoration: none; font-weight: 600;">زيارة الملف الشخصي</a>
                </div>
            </div>
            
            <div style="padding: 1.2rem; background: #f8f9fa; border-radius: 12px;">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.8rem;">
                    <span style="font-size: 1.5rem;">🐱</span>
                    <span style="font-weight: 600; color: #1a237e;">GitHub</span>
                </div>
                <div style="text-align: center;">
                    <a href="{contact_info['github']}" target="_blank" style="color: #333; text-decoration: none; font-weight: 600;">مشاهدة المشاريع</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; border-radius: 20px; padding: 2rem; box-shadow: 0 10px 40px rgba(0,0,0,0.1); height: 100%;">
            <h3 style="color: #1a237e; margin-bottom: 1.5rem; text-align: center;">📝 أرسل لي رسالة</h3>
            
            <form>
            <div style="margin-bottom: 1.5rem;">
                <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #1a237e;">الاسم الكامل</label>
                <input type="text" placeholder="أدخل اسمك الكامل" style="width: 100%; padding: 0.8rem 1rem; border: 2px solid #e8eaf6; border-radius: 10px; font-size: 1rem;">
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #1a237e;">البريد الإلكتروني</label>
                <input type="email" placeholder="أدخل بريدك الإلكتروني" style="width: 100%; padding: 0.8rem 1rem; border: 2px solid #e8eaf6; border-radius: 10px; font-size: 1rem;">
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #1a237e;">نوع المشروع</label>
                <select style="width: 100%; padding: 0.8rem 1rem; border: 2px solid #e8eaf6; border-radius: 10px; font-size: 1rem;">
                    <option value="">اختر نوع المشروع</option>
                    <option value="dashboard">لوحة تحكم تفاعلية</option>
                    <option value="excel">تحويل Excel إلى WebApp</option>
                    <option value="automation">أتمتة عمليات</option>
                    <option value="consultation">استشارة تقنية</option>
                </select>
            </div>
            
            <div style="margin-bottom: 2rem;">
                <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #1a237e;">الرسالة</label>
                <textarea placeholder="اكتب رسالتك هنا..." rows="6" style="width: 100%; padding: 0.8rem 1rem; border: 2px solid #e8eaf6; border-radius: 10px; font-size: 1rem; resize: vertical;"></textarea>
            </div>
            
            <button style="background: linear-gradient(135deg, #1a237e, #311b92); color: white; border: none; border-radius: 50px; padding: 1rem 2.5rem; font-weight: 700; font-size: 1.1rem; width: 100%; cursor: pointer; transition: all 0.3s;">
                إرسال الرسالة
            </button>
            </form>
            
            <div style="margin-top: 2rem; padding-top: 1.5rem; border-top: 2px solid #e8eaf6; text-align: center; color: #666;">
                <p>⏰ وقت الاستجابة: خلال 24 ساعة</p>
                <p>💼 متاح للمشاريع الحرة والعقود الطويلة</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# الفوتر
def render_footer():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0d1117, #161b22); border-radius: 20px; padding: 4rem 2rem; color: white; margin-top: 4rem; text-align: center; position: relative;">
        <h3 style="color: white; margin-bottom: 1.5rem;">✨ دعنا نعمل معًا لتحويل أفكارك إلى واقع</h3>
        <p style="color: #bbb; margin-bottom: 2rem; max-width: 600px; margin-left: auto; margin-right: auto; font-size: 1.1rem;">
        مستعد لبدء مشروعك التالي؟ تواصل معي اليوم وسنناقش كيف يمكنني مساعدتك في تحقيق أهدافك.
        </p>
        
        <div style="display: flex; justify-content: center; gap: 3rem; margin-top: 2rem; flex-wrap: wrap;">
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🚀</div>
                <div style="font-weight: 700;">تطوير سريع</div>
                <div style="color: #bbb; font-size: 0.9rem;">إنجاز المشاريع في الوقت المحدد</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">💡</div>
                <div style="font-weight: 700;">حلول مبدعة</div>
                <div style="color: #bbb; font-size: 0.9rem;">تصميمات مبتكرة تلبي احتياجاتك</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔄</div>
                <div style="font-weight: 700;">دعم مستمر</div>
                <div style="color: #bbb; font-size: 0.9rem;">متواجد بعد التسليم لأي استفسارات</div>
            </div>
        </div>
        
        <div style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1);">
            <p style="font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;">© 2024 أسيل الزواهرة | جميع الحقوق محفوظة</p>
            <p style="color: #bbb; font-size: 1rem;">مطور لوحات تحكم تفاعلية باستخدام Streamlit و Python</p>
            <p style="color: #888; font-size: 0.9rem; margin-top: 1rem;">🇯🇴 مطور أردني متخصص في الحلول التقنية للشركات العربية</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# السايدبار
def render_sidebar():
    with st.sidebar:
        st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🚀</div>
            <h3 style="color: #1a237e; margin-bottom: 0.5rem;">{developer_info['name']}</h3>
            <p style="color: #666; font-size: 1rem; margin-bottom: 1rem;">{developer_info['title']}</p>
            <div style="background: linear-gradient(135deg, #1a237e, #311b92); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; display: inline-block;">
                {developer_info['name_english']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("### 📋 التنقل السريع")
        
        menu_options = ["🏠 الرئيسية", "👤 عني", "💪 مهاراتي", "🚀 مشاريعي", "🎬 مشروعي الحقيقي", "💼 خدماتي", "📞 تواصل"]
        selected_option = st.radio("", menu_options, label_visibility="collapsed")
        
        st.markdown("---")
        
        st.markdown("### ⭐ تقييم البروتفوليو")
        rating = st.slider("", 1, 5, 5, label_visibility="collapsed")
        st.markdown(f"**التقييم:** {'⭐' * rating}")
        
        if rating == 5:
            st.success("شكرًا على تقييمك الممتاز! ✨")
        
        st.markdown("---")
        
        st.markdown("### 📥 روابط سريعة")
        
        if st.button("📄 تحميل السيرة الذاتية"):
            st.info("سيتم إضافة ملف PDF للسيرة الذاتية قريبًا")
        
        if st.button("💼 زيارة مشروعي الحي"):
            st.markdown(f'<meta http-equiv="refresh" content="0;url={developer_info["projects"][0]["live_url"]}">', unsafe_allow_html=True)
            st.success("جاري التوجيه إلى مشروع لوحة المبيعات...")
        
        st.markdown("---")
        
        st.markdown("### 🌐 اللغة")
        language = st.radio("اختر اللغة:", ["العربية 🇸🇦", "English 🇺🇸"], index=0)
        
        if language == "English 🇺🇸":
            st.info("English version coming soon!")

# الدالة الرئيسية
def main():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    render_sidebar()
    render_hero()
    render_about()
    render_skills()
    render_projects()
    render_live_demo()
    render_services()
    render_contact()
    render_footer()
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()