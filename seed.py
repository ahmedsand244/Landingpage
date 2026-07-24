import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from projects.models import Category, Project
from services.models import Technology
from pages.models import FAQ, Testimonial

def seed_data():
    print("Deleting old records...")
    FAQ.objects.all().delete()
    Testimonial.objects.all().delete()
    Project.objects.all().delete()
    Technology.objects.all().delete()
    Category.objects.all().delete()

    print("Creating Categories...")
    cat_ai = Category.objects.create(name="AI / Data Science")
    cat_mobile = Category.objects.create(name="Mobile Apps")
    cat_web = Category.objects.create(name="Web Development")
    cat_cloud = Category.objects.create(name="Cloud & DevOps")

    print("Creating Technologies...")
    tech_python = Technology.objects.create(name="Python", description="Core language for AI and script automation.", category=cat_ai)
    tech_django = Technology.objects.create(name="Django", description="High-level Python web framework.", category=cat_web)
    tech_flutter = Technology.objects.create(name="Flutter", description="Google mobile cross-platform SDK.", category=cat_mobile)
    tech_docker = Technology.objects.create(name="Docker", description="Containerization engine for deployments.", category=cat_cloud)
    tech_aws = Technology.objects.create(name="AWS", description="Amazon Web Services cloud hosting.", category=cat_cloud)
    tech_postgres = Technology.objects.create(name="PostgreSQL", description="Powerful open-source relational database.", category=cat_cloud)

    print("Creating FAQs...")
    FAQ.objects.create(
        question="What happens if my project fails the defense?",
        answer="We offer a Defense Guarantee. If your project fails to meet the technical requirements outlined in your initial academic proposal, we provide full refactoring and support until it passes, at no additional cost.",
        category="general",
        order=1
    )
    FAQ.objects.create(
        question="Do you provide documentation for the academic report?",
        answer="Yes. Every project delivery includes comprehensive system architecture diagrams, database schemas, and API documentation required for standard university thesis reports.",
        category="general",
        order=2
    )
    FAQ.objects.create(
        question="Who owns the intellectual property?",
        answer="Upon full payment, you retain 100% intellectual property rights and full source code ownership. Graduation Projects Studio claims no equity or IP rights.",
        category="technical",
        order=1
    )
    FAQ.objects.create(
        question="Can I pay in installments?",
        answer="Yes, we structure payments around project milestones (typically 30% kickoff, 40% beta delivery, 30% final deployment).",
        category="pricing",
        order=1
    )
    FAQ.objects.create(
        question="Can this project be launched as a real startup?",
        answer="Absolutely. Our 'Enterprise' tier is designed specifically for students intending to take their graduation project to market. We use scalable architecture (AWS/GCP, Docker) to ensure commercial readiness.",
        category="support",
        order=1
    )

    print("Creating Testimonials...")
    Testimonial.objects.create(
        name="Sarah J.",
        role_university="M.Sc. Civil Engineering",
        review_text="The structural analysis framework we developed here set a new faculty standard.",
        rating=5
    )
    Testimonial.objects.create(
        name="Alex M.",
        role_university="B.Sc. Computer Science",
        review_text="Optimizing neural pathways for latency in a high-stakes setting was perfect. Got full distinction.",
        rating=5
    )
    Testimonial.objects.create(
        name="Elena R.",
        role_university="B.Sc. Architecture",
        review_text="Sustainable urban integration models designed here were highly praised by the assessment committee.",
        rating=5
    )

    print("Creating Projects...")
    proj1 = Project.objects.create(
        title="Cognitive Diagnostics API",
        project_type="graduation",
        client_name="MedTech University",
        country="Egypt",
        summary="A scalable RESTful API leveraging deep learning for early-stage disease detection from medical imaging, achieving 94% accuracy.",
        overview="This project addresses the critical challenge of dynamic medical diagnosis in unstructured environments. By implementing a novel deep convolutional neural network, the system achieves a 40% reduction in error rates compared to baseline systems.\n\nThe system is packaged inside a high-performance Django REST framework interface and is fully containerized with Docker, deployable to AWS ECS.",
        deliverables=["Source Code", "IEEE Thesis PDF", "Presentation Slide", "Docker Compose"],
        is_featured=True
    )
    proj1.technologies.add(tech_python, tech_django, tech_postgres)

    proj2 = Project.objects.create(
        title="Urban Mobility Tracker",
        project_type="graduation",
        client_name="MetroGov Corp",
        country="KSA",
        summary="A cross-platform mobile application utilizing real-time GPS and predictive algorithms to optimize public transit routing for smart cities.",
        overview="Urban Transit optimization is key for smart city growth. This mobile application built with Flutter links dynamically to a central routing API. It incorporates graph algorithms and historic travel data to forecast delays and offer alternative routes in sub-second timelines.",
        deliverables=["Mobile App Build (.apk)", "Architecture Design Doc", "Presentation Slides"],
        is_featured=True
    )
    proj2.technologies.add(tech_flutter, tech_aws)

    proj3 = Project.objects.create(
        title="FinTech Trading Terminal",
        project_type="commercial",
        client_name="Capital Dynamics",
        country="UAE",
        summary="A high-performance, real-time web dashboard for algorithmic trading analysis, featuring WebSocket integration and sub-second latency.",
        overview="A high-fidelity trading dashboard built to monitor stock exchange APIs. Using WebSockets for dynamic data pipelines, the terminal handles up to 10,000 tick updates per second with zero browser lag. Built with React and Django backend, with Redis caching.",
        deliverables=["System Source Code", "Deployment Manual", "API Reference Guide"],
        is_featured=True
    )
    proj3.technologies.add(tech_django, tech_postgres, tech_docker)

    print("Data seeding completed successfully!")

if __name__ == '__main__':
    seed_data()
