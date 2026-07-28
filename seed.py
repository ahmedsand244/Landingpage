import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from projects.models import Category, Project
from services.models import Technology
from pages.models import FAQ, Testimonial, SiteSetting, StudioMetric

def seed_data():
    print("Deleting old records...")
    FAQ.objects.all().delete()
    Testimonial.objects.all().delete()
    Project.objects.all().delete()
    Technology.objects.all().delete()
    Category.objects.all().delete()
    StudioMetric.objects.all().delete()

    print("Creating Site Settings & Studio Metrics...")
    SiteSetting.objects.get_or_create(id=1, defaults={
        'academic_site_url': '',
        'academic_button_text': 'تحدث معنا لمشروع التخرج'
    })

    StudioMetric.objects.create(
        title="مشروع بزنس و MVP مكتمل",
        value="+50",
        subtitle="منصات سحابية وتطبيقات جوال حية",
        icon_name="rocket_launch",
        color_theme="primary",
        order=1
    )
    StudioMetric.objects.create(
        title="نجاح مناقشات التخرج",
        value="100%",
        subtitle="تقديرات امتياز وتوثيق أكاديمي كامل",
        icon_name="workspace_premium",
        color_theme="emerald",
        order=2
    )
    StudioMetric.objects.create(
        title="دول عربية وخليجية",
        value="+6",
        subtitle="مشاريع مسلمة في السعودية، الإمارات، ومصر",
        icon_name="public",
        color_theme="secondary",
        order=3
    )
    StudioMetric.objects.create(
        title="ملكية الكود المصدري",
        value="100%",
        subtitle="تسليم كامل الملفات بدون اشتراكات خفية",
        icon_name="code",
        color_theme="amber",
        order=4
    )

    print("Creating Categories...")
    cat_biz = Category.objects.create(name="Business & SaaS")
    cat_ai = Category.objects.create(name="AI & Data Solutions")
    cat_mobile = Category.objects.create(name="Mobile Apps")
    cat_web = Category.objects.create(name="Web Applications")

    print("Creating Technologies...")
    tech_python = Technology.objects.create(name="Python", description="Core language for AI, data pipelines and automation.", category=cat_ai)
    tech_django = Technology.objects.create(name="Django / REST", description="Robust backend framework for enterprise web apps.", category=cat_web)
    tech_flutter = Technology.objects.create(name="Flutter", description="Google mobile cross-platform SDK for iOS & Android.", category=cat_mobile)
    tech_react = Technology.objects.create(name="React.js", description="Modern reactive frontend UI library for SaaS dashboards.", category=cat_biz)
    tech_docker = Technology.objects.create(name="Docker & Cloud", description="Containerization and cloud deployment infrastructure.", category=cat_biz)
    tech_postgres = Technology.objects.create(name="PostgreSQL", description="Enterprise relational database.", category=cat_web)

    print("Creating FAQs...")
    FAQ.objects.create(
        question="هل تقدمون خدمات تطوير المظهر وتطبيقات البزنس (MVP) للشركات الناشئة؟",
        answer="نعم، نحن متخصصون في تحويل أفكار البزنس والأنشطة التجارية إلى تطبيقات ويب وموبايل كاملة (MVP) جاهزة للإطلاق في السوق وربط وسائل الدفع الإلكتروني وقواعد البيانات.",
        category="general",
        order=1
    )
    FAQ.objects.create(
        question="هل تغطون مشاريع التخرج الأكاديمية أيضاً؟",
        answer="بالتأكيد، لدينا قسم أكاديمي كامل يساعد طلاب الحاسبات والهندسة في تنفيذ وتوثيق مشاريع تخرجهم بأعلى المعايير وتوفير ملفات الشرح والتوثيق للمناقشة.",
        category="general",
        order=2
    )

    print("Creating Testimonials...")
    Testimonial.objects.create(
        name="م. أحمد التميمي",
        role_university="مؤسس منصة لوجستية - الإمارات",
        review_text="قام الفريق بتطوير تطبيق البزنس ولوحة التحكم بالكامل خلال وقت قياسي جداً وبجودة عالية مكنتنا من انطلاق الخدمة.",
        rating=5
    )
    Testimonial.objects.create(
        name="سارة محمود",
        role_university="خريجة حاسبات ومعلومات - مصر",
        review_text="مشروع التخرج في الذكاء الاصطناعي كان مبنياً باحترافية شديدة، وحصلت على تقدير امتياز في المناقشة بفضل الشرح والتوثيق الممتاز.",
        rating=5
    )

    print("Creating Business & Academic Projects...")
    proj1 = Project.objects.create(
        title="منصة لوجستية وتتبع الشحنات (Smart Logistics SaaS)",
        project_type="commercial",
        client_name="ExpressLogistics Corp",
        country="UAE",
        summary="منصة بزنس متكاملة لإدارة الأسطول، تتبع الشحنات بالذكاء الاصطناعي، ولوحة تحكم حية للمبيعات والعمليات.",
        overview="نظام إدارة لوجستيات متكامل يعتمد على Django backend و React frontend. يربط بين السائقين والعملاء والإدارة عبر خرائط حية وتنبيهات لحظية لحالة الشحنات.",
        project_url="https://demo.expresslogistics.example.com",
        deliverables=["Full Source Code", "Web Admin Dashboard", "Mobile Apps (iOS/Android)", "Cloud Hosting Setup"],
        is_featured=True
    )
    proj1.technologies.add(tech_django, tech_react, tech_postgres, tech_docker)

    proj2 = Project.objects.create(
        title="تطبيق متجر إلكتروني ذكي (E-Commerce Mobile App)",
        project_type="commercial",
        client_name="RetailPlus Store",
        country="KSA",
        summary="تطبيق موبايل تجاري متكامل للبيع والتسوق الإلكتروني مع دعم الدفع عبر البوابة وتنبيهات العروض.",
        overview="تطبيق هواتف ذكية تم تطويره بلغة Flutter ليخدم أصحاب المتاجر والشركات التجارية مع دعم وسائل الدفع الإلكتروني المباشرة وإدارة المخزون والتوصيل.",
        project_url="https://retailplus-app.example.com",
        deliverables=["Flutter Source Code", "REST APIs", "Payment Gateway Integration"],
        is_featured=True
    )
    proj2.technologies.add(tech_flutter, tech_python, tech_django)

    proj3 = Project.objects.create(
        title="نظام التشخيص الطبي بالذكاء الاصطناعي (AI Cognitive Medical)",
        project_type="graduation",
        client_name="Faculty of Computer Science",
        country="Egypt",
        summary="مشروع تخرج أكاديمي متقدم يستخدم الشبكات العصبية العميقة للتشخيص المبكر للأمراض من الأشعة والتحاليل بنسبة دقة 95%.",
        overview="نظام ذكاء اصطناعي طبي متكامل يشمل واجهة RESTful API ونموذج Deep Learning مع التوثيق الأكاديمي الكامل والأبحاث المعتمدة للمناقشة.",
        project_url="https://ai-medical-demo.example.com",
        deliverables=["Source Code", "IEEE Thesis Paper PDF", "Presentation Deck", "Docker Setup"],
        is_featured=True
    )
    proj3.technologies.add(tech_python, tech_django, tech_postgres)

    print("Data seeding completed successfully!")

if __name__ == '__main__':
    seed_data()
