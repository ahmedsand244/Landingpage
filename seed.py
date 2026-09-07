import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from projects.models import Category, Project, ProjectGallery
from services.models import Technology
from pages.models import FAQ, Testimonial, SiteSetting, StudioMetric
from django.core.cache import cache

def seed_data():
    print("Deleting old records...")
    cache.clear()
    ProjectGallery.objects.all().delete()
    Project.objects.all().delete()
    Technology.objects.all().delete()
    Category.objects.all().delete()
    StudioMetric.objects.all().delete()
    FAQ.objects.all().delete()
    Testimonial.objects.all().delete()

    print("Creating Site Settings & Studio Metrics...")
    SiteSetting.objects.get_or_create(id=1, defaults={
        'academic_site_url': 'https://wa.me/201554397407?text=أهلاً%20بكم،%20أود%20الاستفسار%20عن%20تفاصيل%20مشروع%20تخرج%20أكاديمي',
        'academic_button_text': 'تحدث معنا لمشروع التخرج',
        'academic_button_text_en': 'Talk to Us for Graduation Project'
    })

    StudioMetric.objects.create(
        title="مشاريع وأنظمة منجزة",
        title_en="Completed Projects & Systems",
        value="+60",
        subtitle="تطبيقات موبايل ومنصات سحابية حية في السوق",
        subtitle_en="Live mobile apps & cloud platforms in the market",
        icon_name="rocket_launch",
        color_theme="primary",
        order=1
    )
    StudioMetric.objects.create(
        title="نسبة نجاح مشاريع التخرج",
        title_en="Graduation Projects Success Rate",
        value="100%",
        subtitle="تقديرات امتياز وتوثيق أكاديمي معتمد",
        subtitle_en="Straight-A honors & accredited thesis documentation",
        icon_name="workspace_premium",
        color_theme="emerald",
        order=2
    )
    StudioMetric.objects.create(
        title="أنظمة ومتاجر قيد التشغيل",
        title_en="Active Operating Systems & Stores",
        value="+15",
        subtitle="منصات ERP وتجارة إلكترونية تعمل بكفاءة حقيقية",
        subtitle_en="High-efficiency ERP & E-Commerce platforms in production",
        icon_name="storefront",
        color_theme="secondary",
        order=3
    )
    StudioMetric.objects.create(
        title="تسليم الكود المصدري كاملاً",
        title_en="Full Source Code Ownership",
        value="100%",
        subtitle="ملكية تامة للكود والدعم الفني المباشر",
        subtitle_en="Complete IP ownership & direct post-launch support",
        icon_name="code",
        color_theme="amber",
        order=4
    )

    print("Creating Categories...")
    cat_erp = Category.objects.create(name="إدارة المؤسسات والـ ERP", name_en="ERP & Enterprise", slug="erp-enterprise")
    cat_ecom = Category.objects.create(name="التجارة الإلكترونية", name_en="E-Commerce & Retail", slug="ecommerce-retail")
    cat_ai = Category.objects.create(name="الذكاء الاصطناعي وتعلم الآلة", name_en="AI & Machine Learning", slug="ai-machine-learning")
    cat_web = Category.objects.create(name="المنصات السحابية والويب", name_en="Web & Cloud Platforms", slug="web-cloud-platforms")
    cat_industrial = Category.objects.create(name="الأنظمة الصناعية والهندسية", name_en="Industrial & Engineering", slug="industrial-engineering")

    print("Creating Technologies...")
    t_python = Technology.objects.create(
        name="بايثون / Python", 
        name_en="Python", 
        description="اللغة الأساسية للباك إند والذكاء الاصطناعي ومعالجة البيانات وبناء الخدمات البرمجية القوية.",
        description_en="Core backend language for AI, data pipelines and robust web services.", 
        category=cat_ai
    )
    t_django = Technology.objects.create(
        name="دجانغو / Django & DRF", 
        name_en="Django & DRF", 
        description="إطار عمل بايثون فائق الأمان والسرعة لتطوير واجهات الـ API وقواعد البيانات المعقدة.",
        description_en="High-level Python web framework for secure, scalable web APIs and databases.", 
        category=cat_web
    )
    t_flutter = Technology.objects.create(
        name="فلاتر / Flutter & Dart", 
        name_en="Flutter & Dart", 
        description="إطار عمل تطبيقات الموبايل لتطوير تطبيقات أصلية فائقة السلاسة لنظامي iOS و Android بكود واحد.",
        description_en="Cross-platform native mobile app framework for iOS & Android.", 
        category=cat_erp
    )
    t_tailwind = Technology.objects.create(
        name="تيلويند / Tailwind CSS", 
        name_en="Tailwind CSS", 
        description="إطار عمل التصميم الحديث لبناء واجهات مستخدم متجاوبة وفائقة الجمال والأناقة.",
        description_en="Utility-first modern CSS framework for custom responsive interfaces.", 
        category=cat_web
    )
    t_alpine = Technology.objects.create(
        name="ألبين / Alpine.js", 
        name_en="Alpine.js", 
        description="مكتبة جافاسكريبت خفيفة للتفاعل الفوري والتجاوب اللحظي دون إبطاء المتصفح.",
        description_en="Lightweight reactive JavaScript framework for fast declarative interactions.", 
        category=cat_web
    )
    t_paymob = Technology.objects.create(
        name="باي موب / Paymob Gateway", 
        name_en="Paymob Gateway", 
        description="بوابة الدفع الإلكتروني المعتمدة للبطاقات البنكية والمحافظ الرقمية.",
        description_en="Enterprise online payment gateway integration for cards and digital wallets.", 
        category=cat_ecom
    )
    t_ai = Technology.objects.create(
        name="تعلم الآلة / Machine Learning", 
        name_en="Machine Learning", 
        description="خوارزميات التنبؤ وتحليل المخاطر والشبكات العصبية المتقدمة.",
        description_en="Predictive risk scoring algorithms, data modeling and neural architectures.", 
        category=cat_ai
    )
    t_postgres = Technology.objects.create(
        name="قواعد بيانات PostgreSQL / SQLite", 
        name_en="PostgreSQL / SQLite", 
        description="قواعد بيانات علائقية موثوقة للمعاملات المالية وحفظ البيانات الحساسة.",
        description_en="Reliable relational databases for transactional integrity.", 
        category=cat_erp
    )

    print("Creating FAQs...")
    FAQ.objects.create(
        question="هل تقدمون خدمات تطوير تطبيقات البزنس والـ MVP للشركات الناشئة؟",
        question_en="Do you provide MVP and custom business software development for startups?",
        answer="نعم، نحن متخصصون في تحويل أفكار البزنس والأنشطة التجارية إلى تطبيقات ويب وموبايل كاملة (MVP) جاهزة للإطلاق في السوق وربط وسائل الدفع الإلكتروني (Paymob/Stripe) وقواعد البيانات السحابية.",
        answer_en="Yes, we specialize in converting business ideas and commercial operations into market-ready web and mobile MVPs with integrated payment gateways (Paymob/Stripe) and cloud databases.",
        category="general",
        order=1
    )
    FAQ.objects.create(
        question="هل تغطون مشاريع التخرج والأبحاث الأكاديمية أيضاً؟",
        question_en="Do you also develop academic graduation projects and research thesis?",
        answer="بالتأكيد، لدينا مسار أكاديمي كامل يساعد طلاب الحاسبات والهندسة في تنفيذ وتوثيق مشاريع تخرجهم بأعلى المعايير وتوفير ملفات الشرح والتوثيق المعتمدة (IEEE) والمتابعة حتى يوم المناقشة.",
        answer_en="Absolutely, our dedicated Academic Track assists Computer Science & Engineering students with high-standard project implementation, IEEE thesis documentation, and defense coaching.",
        category="general",
        order=2
    )
    FAQ.objects.create(
        question="هل يتم تسليم الكود المصدري كاملاً وحقوق الملكية للعميل؟",
        question_en="Do we receive full source code ownership and intellectual property?",
        answer="نعم 100%، يحصل العميل على الكود المصدري بالكامل مع توثيق التثبيت وملفات الإعداد وبدون أي قيود أو اشتراكات حكرية.",
        answer_en="Yes 100%, the client receives full source code ownership, complete installation documentation, deployment guides, and zero vendor lock-in.",
        category="technical",
        order=3
    )
    FAQ.objects.create(
        question="ما هي المدة والآلية المتبعة لتنفيذ المشروع؟",
        question_en="What is the timeframe and development methodology for projects?",
        answer="نتبع منهجية Agile السريعة مع تسليم تدريجي ونماذج تفاعلية مستمرة، وتتراوح المدة حسب حجم المشروع من أسبوعين للنماذج الأولية وحتى شهرين للأنظمة المؤسسية الكبرى.",
        answer_en="We follow agile sprint methodology with continuous milestone demos. Timelines range from 2 weeks for MVPs to 1-2 months for full-scale enterprise systems.",
        category="pricing",
        order=4
    )

    print("Creating Testimonials...")
    Testimonial.objects.create(
        name="م. أحمد التميمي",
        role_university="مؤسس منصة تجارة إلكترونية - الإمارات",
        role_university_en="E-Commerce Founder - UAE",
        review_text="قام فريق Code+ بتطوير متجر نكسوس الإلكتروني وسلة المشتريات التفاعلية ولوحة التحكم بأعلى كفاءة وسرعة، وتم إطلاق المشروع بنجاح كبير.",
        review_text_en="The Code+ team built the NEXUS luxury e-commerce platform with interactive cart, live payment gateway, and admin dashboard with utmost speed and excellence.",
        rating=5,
        admin_reply="شكراً جزيلاً أستاذ أحمد، تشرفنا بالعمل على مشروع نكسوس ونتمنى لكم دوام التوسع والنجاح!",
        admin_reply_en="Thank you Eng. Ahmed! It was a pleasure building the NEXUS platform with you. Wishing you continued growth!"
    )
    Testimonial.objects.create(
        name="سارة محمود",
        role_university="خريجة حاسبات ومعلومات - مصر",
        role_university_en="CS Graduate - Egypt",
        review_text="مشروع التخرج في الذكاء الاصطناعي (RiskChain AI) كان مبنياً باحترافية شديدة، وحصلت على تقدير امتياز في المناقشة بفضل الشرح والتوثيق الممتاز.",
        review_text_en="Our AI graduation project (RiskChain AI) was built with top-tier professionalism. We achieved straight-A distinction in the defense thanks to their thorough documentation.",
        rating=5,
        admin_reply="ألف مبروك التخرج بامتياز يا سارة، دائماً فخورين بنجاح طلابنا!",
        admin_reply_en="Congratulations on your distinction, Sarah! Always proud of our academic graduates!"
    )

    print("Creating Real Projects...")

    # 1. Al-Namaa ERP & POS
    p1 = Project.objects.create(
        title="نظام النماء لإدارة المحلات والمخازن ونقاط البيع السحابية (Al-Namaa ERP & POS)",
        title_en="Al-Namaa Cloud Retail ERP & POS System",
        slug="alnamaa-erp-pos-system",
        project_type="commercial",
        client_name="النماء لحلول إدارة المتاجر ونقاط البيع (Al-Namaa Retail)",
        client_name_en="Al-Namaa Retail Solutions & Point of Sale",
        country="مصر والسعودية",
        country_en="Egypt & Saudi Arabia",
        summary="نظام سحابي متكامل لإدارة المخازن، نقاط البيع (Cloud POS)، المبيعات، الفواتير الإلكترونية والباركود مع تطبيق موبايل Flutter متكامل للمناديب.",
        summary_en="An integrated cloud ERP & Point of Sale system managing inventory, sales, electronic invoicing, barcode generation, and a dedicated Flutter mobile app for sales agents.",
        overview="منصة ERP & POS سحابية متقدمة مصممة خصيصاً لإدارة الأنشطة التجارية والمحلات والورش والمستودعات. يتميز النظام بالربط المباشر بين نقاط البيع وتطبيقات الموبايل وإدارة المخزون بدقة متناهية مع طباعة الفواتير الإلكترونية وإصدار تقارير الأرباح والتدفقات المالية لحظياً، مع دعم تعدد الفروع والصلاحيات.",
        overview_en="An advanced cloud-native ERP & POS platform designed for retail stores, warehouses, and commercial chains. Features real-time sync between POS terminals and mobile apps, automated inventory tracking, thermal receipt and electronic invoice generation, multi-branch control, and live cash-flow analytics.",
        project_url="https://webservises.pythonanywhere.com/",
        deliverables=[
            "الكود المصدري الكامل (Django Backend + Flutter Mobile App)",
            "لوحة تحكم سحابية لإدارة الفروع والمخزون ونقاط البيع",
            "تطبيق موبايل Flutter للمناديب وإدارة الطلبات السريعة",
            "محرك فواتير إلكترونية وطباعة باركود وإيصالات حرارية",
            "دليل النشر والاستخدام مع دعم فني مستمر 24/7"
        ],
        deliverables_en=[
            "Complete Full Source Code (Django Backend + Flutter Mobile App)",
            "Cloud Management Dashboard for Multi-Branch Inventory & POS",
            "Flutter Native Mobile App for Sales Agents & Field Operations",
            "Electronic Invoicing Engine & Thermal Barcode Printer Integration",
            "Full Deployment & User Guides with 24/7 Ongoing Tech Support"
        ],
        is_featured=True
    )
    p1.technologies.add(t_python, t_django, t_flutter, t_postgres, t_tailwind)
    ProjectGallery.objects.create(
        project=p1,
        image="projects/gallery/alnamaa_erp.jpg",
        caption="لوحة تحكم نظام النماء لإدارة المخازن ونقاط البيع السحابية (ERP & POS)"
    )

    # 2. NEXUS Luxury E-Commerce
    p2 = Project.objects.create(
        title="منصة نكسوس للمتاجر الإلكترونية الفاخرة (NEXUS Luxury E-Commerce Platform)",
        title_en="NEXUS Luxury E-Commerce & Shopping Experience",
        slug="nexus-luxury-ecommerce-platform",
        project_type="commercial",
        client_name="Nexus Luxury Goods & Electronics Store",
        client_name_en="NEXUS Luxury Goods & Retail Group",
        country="مصر والخليج العربي",
        country_en="Egypt & GCC Region",
        summary="منصة تجارة إلكترونية سريعة وفائقة الفخامة بتصميم Glassmorphism، سلة مشتريات تفاعلية AJAX، ربط بوابات الدفع Paymob، وتتبع تلقائي للموقع الجغرافي.",
        summary_en="An ultra-fast luxury e-commerce platform featuring modern glassmorphism aesthetics, dynamic AJAX cart drawer, Paymob payment gateway integration, and GPS shipping calculations.",
        overview="متجر إلكتروني ذكي وفاخر مبني بأحدث معايير الأداء والواجهات التفاعلية. يشتمل على سلة مشتريات منزلقة (AJAX Sliding Cart Drawer)، صفحة دفع موحدة (One-Page Checkout)، فلترة فورية للمنتجات بدون إعادة تحميل، ربط بوابة دفع إلكتروني Paymob، وتحديد موقع التوصيل الجغرافي عبر GPS، ونظام إشعارات فورية عبر الواتساب والبريد الإلكتروني للعميل والإدارة.",
        overview_en="A state-of-the-art e-commerce storefront engineered for high conversion and premium user experience. Includes instant AJAX slide-out cart, frictionless one-page checkout, live faceted product search, full Paymob card & digital wallet processing, and instant WhatsApp & Email order tracking.",
        project_url="https://shopproject.pythonanywhere.com/",
        deliverables=[
            "تطبيق المتجر الإلكتروني الكامل مع دعم الوضع الليلي والفاتح",
            "بوابة دفع إلكتروني Paymob مدمجة بالكامل لجميع البطاقات والمحافظ",
            "لوحة تحكم المشرف والمدير (Supervisor Control Center)",
            "نظام حساب تكلفة الشحن الجغرافي بالـ GPS التلقائي",
            "نظام محادثة حية وإشعارات فورية عبر الواتساب"
        ],
        deliverables_en=[
            "Full E-Commerce Web Platform with Dark/Light Theme Switching",
            "Fully Integrated Paymob Gateway for Credit Cards & Digital Wallets",
            "Admin & Operations Management Control Center",
            "Automated GPS Geolocation Shipping Cost Calculator",
            "Live WhatsApp Instant Order Dispatch & Customer Notifications"
        ],
        is_featured=True
    )
    p2.technologies.add(t_python, t_django, t_paymob, t_tailwind, t_alpine, t_postgres)
    ProjectGallery.objects.create(
        project=p2,
        image="projects/gallery/nexus_store.jpg",
        caption="واجهة منصة نكسوس للتجارة الإلكترونية الفاخرة وسلة المشتريات التفاعلية"
    )

    # 3. RiskChain AI
    p3 = Project.objects.create(
        title="نظام ريسك تشين للتنبؤ بمخاطر سلاسل الإمداد بالذكاء الاصطناعي (RiskChain AI)",
        title_en="RiskChain AI - Predictive Supply Chain Intelligence Platform",
        slug="riskchain-ai-supply-chain",
        project_type="graduation",
        client_name="مشروع تخرج وبحث علمي متقدم (AI & Machine Learning Lab)",
        client_name_en="Advanced Academic AI & Machine Learning Research",
        country="مصر وعالمياً (Global)",
        country_en="Egypt & Global",
        summary="محرك ذكاء اصطناعي ونظام API سحابي للتنبؤ بمخاطر سلاسل الإمداد والاضطرابات اللوجستية وتأمين واجهات البيانات.",
        summary_en="An AI predictive modeling engine and high-throughput REST API predicting supply chain bottlenecks, disruption risks, and securing enterprise data endpoints.",
        overview="منظومة متقدمة تجمع بين خوارزميات تعلم الآلة ونماذج تحليل المخاطر اللوجستية مع واجهة برمجية سريعة (RESTful API). يقوم النظام بتحليل مؤشرات الشحن والأسواق وتقلبات الإمداد للتنبؤ باحتماليات التأخير والتعطل قبل حدوثها بنسبة دقة تتجاوز 91%، مع نظام حماية Terminal Auth مشفر للمؤسسات.",
        overview_en="An intelligent end-to-end framework combining predictive machine learning models with high-speed Django REST APIs. Analyzes logistical delay probabilities, supplier disruptions, and market volatility with 91%+ predictive accuracy, secured via authenticated terminal access tokens.",
        project_url="https://riskchain.pythonanywhere.com/",
        deliverables=[
            "نماذج الذكاء الاصطناعي وتعلم الآلة المدربة والمختبرة بدقة 91%",
            "واجهات برمجة التطبيقات السحابية عالية السرعة (Django REST APIs)",
            "التوثيق الأكاديمي والبحثي الكامل وفق معايير IEEE لمشاريع التخرج",
            "نظام المصادقة المشفر الآمن Terminal Auth",
            "عرض تقديمي احترافي (Slides) وتدريب شامل على أسئلة المناقشة"
        ],
        deliverables_en=[
            "Trained & Validated Machine Learning Models with 91%+ Accuracy",
            "High-Throughput Cloud REST APIs (Django REST Framework)",
            "Complete IEEE Academic Research & Thesis Documentation",
            "Encrypted Terminal Authentication & Security Layer",
            "Professional Defense Presentation Slides & Comprehensive Defense Coaching"
        ],
        is_featured=True
    )
    p3.technologies.add(t_python, t_ai, t_django, t_postgres)
    ProjectGallery.objects.create(
        project=p3,
        image="projects/gallery/riskchain_ai.jpg",
        caption="لوحة مؤشرات الذكاء الاصطناعي وخريطة المخاطر الحية في نظام RiskChain AI"
    )

    # 4. BearingMaster Pro
    p4 = Project.objects.create(
        title="منصة بيرنج ماستر للأدلة الهندسية والصناعية (BearingMaster Pro)",
        title_en="BearingMaster Pro - Industrial Engineering Catalog",
        slug="bearingmaster-pro-industrial-guide",
        project_type="commercial",
        client_name="BearingMaster Industrial Catalog",
        client_name_en="BearingMaster Mechanical Industrial Catalog",
        country="مصر والقطاع الصناعي",
        country_en="Egypt & Industrial Sector",
        summary="منصة ويب تفاعلية فائقة السرعة للبحث والمطابقة الهندسية لمقاسات وبدائل رولمان البلي وقطع الغيار الميكانيكية.",
        summary_en="An ultra-fast interactive engineering search platform for finding exact mechanical bearing specifications, tolerances, and industrial interchange equivalents.",
        overview="محرك بحث صناعي وتطبيقي يتيح للمهندسين والمصانع والورش البحث الفوري والمطابقة الدقيقة بين مئات المقاسات والرموز الهندسية لرولمان البلي وقطع الحركة الميكانيكية، مع عرض الأبعاد الداخلية والخارجية والسرعات والبدائل المعتمدة فورياً وبواجهة فيكتور عصرية فائقة الخفة.",
        overview_en="An industrial engineering web catalog allowing factory operators and mechanical engineers to search, filter, and cross-reference hundreds of bearing dimensions, load ratings, RPM limits, and verified equivalent interchange part numbers with instant vector diagrams.",
        project_url="https://siteofbila-bearing.surge.sh/",
        deliverables=[
            "تطبيق ويب أحادي الصفحة فائق السرعة (Surge Deployed SPA)",
            "محرك بحث هندسي متعدد المعايير (الأقطار، السرعات، الأنواع)",
            "قاعدة بيانات تقنية دقيقة لمئات المقاسات والبدائل الصناعية",
            "تصميم متجاوب وسهل الاستخدام للورش والمصانع"
        ],
        deliverables_en=[
            "Lightning-Fast Single-Page Application (Surge Deployed SPA)",
            "Multi-Parametric Mechanical Search Engine (Inner/Outer Diameters, RPM, Types)",
            "Engineered Technical Database of Hundreds of Industrial Standards",
            "Ultra-Responsive Mobile-Ready Interface Tailored for Workshops & Factories"
        ],
        is_featured=True
    )
    p4.technologies.add(t_tailwind, t_alpine)
    ProjectGallery.objects.create(
        project=p4,
        image="projects/gallery/bearingmaster.jpg",
        caption="محرك البحث الصناعي وتطابق المقاسات الهندسية لرولمان البلي"
    )

    # 5. Code+ Studio Official Platform
    p5 = Project.objects.create(
        title="منصة استوديو كود بلس الرسمية للحلول البرمجية (Code+ Studio Platform)",
        title_en="Code+ Software & Business Solutions Official Platform",
        slug="codeplus-software-studio-platform",
        project_type="commercial",
        client_name="Code+ Software & Business Solutions",
        client_name_en="Code+ Software & Business Solutions Studio",
        country="مصر والوطن العربي",
        country_en="Egypt & Arab World",
        summary="منصة البوابة الرسمية لاستوديو البرمجيات Code+ مع دعم كامل للغتين (عربي/إنجليزي)، الوضع الليلي والفاتح، وسرعة استجابة فائقة (8ms).",
        summary_en="The official digital portal for Code+ Studio featuring seamless bilingual switching (AR/EN), instant dark/light mode toggle, and sub-10ms response times.",
        overview="المنصة التفاعلية الرسمية للشركة واستوديو تطوير المشاريع التجارية والأكاديمية. تتميز بمعمارية فائقة السرعة، رسوم متحركة تفاعلية Canvas دون استهلاك موارد المعالج، دعم كامل للثيم الفاتح والداكن، لوحة تحكم كاملة لإدارة المشاريع والإحصائيات والآراء والرسائل.",
        overview_en="The flagship web portal for Code+ Studio showcasing enterprise solutions, real-world case studies, dynamic client reviews, and instant WhatsApp consultation channels, built with lightweight Alpine.js, Tailwind CSS, and optimized Django caching.",
        project_url="https://codepage.pythonanywhere.com",
        deliverables=[
            "نظام إدارة المحتوى المتكامل مع Django ولوحة تحكم شاملة",
            "هوية بصرية ونظام تصميم فيكتور نقي مع دعم Dark/Light Mode",
            "محرك الترجمة الفورية باللغتين العربية والإنجليزية",
            "بنية برمجية فائقة السرعة مع تخزين مؤقت متطور"
        ],
        deliverables_en=[
            "Full-Featured Django Content Management & Administrative Dashboard",
            "Modern Vector Design System with Seamless Dark/Light Themes",
            "Instant Real-Time Client-Side Bilingual Localization (Arabic & English)",
            "Ultra-High Performance Architecture with Optimized Caching"
        ],
        is_featured=True
    )
    p5.technologies.add(t_python, t_django, t_tailwind, t_alpine, t_postgres)
    ProjectGallery.objects.create(
        project=p5,
        image="projects/gallery/codeplus_platform.jpg",
        caption="واجهة منصة استوديو كود بلس الرسمية وتجربة التفاعل الرقمي"
    )

    cache.clear()
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_data()
