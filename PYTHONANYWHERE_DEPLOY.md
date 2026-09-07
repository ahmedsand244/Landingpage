# 🚀 دليل رفع وتشغيل المشروع على PythonAnywhere (PythonAnywhere Deployment Guide)

دليل خطوة بخطوة لربط وتشغيل موقع **Code+ Studio** على سيرفر **PythonAnywhere** بأعلى أداء.

---

### 1. سحب المشروع من GitHub إلى PythonAnywhere
افتح الـ **Bash Console** في حسابك على PythonAnywhere ونفّذ:

```bash
git clone https://github.com/ahmedsand244/Landingpage.git
cd Landingpage
```

---

### 2. إنشاء وتفعيل البيئة الافتراضية (Virtualenv) وتثبيت المكتبات

```bash
# إنشاء بيئة عمل بايثون 3.10 أو أحدث
mkvirtualenv --python=/usr/bin/python3.10 landing-env

# أو باستخدام virtualenv العادي:
# python3.10 -m venv ~/.virtualenvs/landing-env
# source ~/.virtualenvs/landing-env/bin/activate

# تثبيت متطلبات المشروع
pip install -r requirements.txt
```

---

### 3. تطبيق المايجريشن وجمع الملفات الثابتة (Static Files)

```bash
# تطبيق الترحيل لقاعدة البيانات
python manage.py migrate

# تغذية البيانات الأولية والمشاريع ثنائية اللغة
python seed.py

# تجميع ملفات الـ CSS والـ JS والصور
python manage.py collectstatic --noinput
```

---

### 4. إعدادات لوحة تحكم الويب (Web Tab on PythonAnywhere)

1. اذهب إلى تبويب **Web** في PythonAnywhere.
2. أنشئ تطبيق ويب يدوي **Manual Configuration** باختيار **Python 3.10**.
3. في قسم **Virtualenv**، ضع المسار:
   `/home/<your-username>/.virtualenvs/landing-env`
4. في قسم **Source code**، ضع المسار:
   `/home/<your-username>/Landingpage`
5. في قسم **Working directory**، ضع المسار:
   `/home/<your-username>/Landingpage`

---

### 5. إعداد الملفات الثابتة (Static Files & Media Mappings)
في قسم **Static files** في صفحة Web، أضف السطور التالية:

| URL | Directory Path |
| :--- | :--- |
| `/static/` | `/home/<your-username>/Landingpage/staticfiles` |
| `/media/` | `/home/<your-username>/Landingpage/media` |

---

### 6. ضبط ملف الـ WSGI (WSGI Configuration File)
اضغط على رابط ملف الـ **WSGI configuration file** في صفحة Web وعدّله ليصبح كالتالي:

```python
import os
import sys

# مسار مجلد المشروع
path = '/home/<your-username>/Landingpage'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
*(استبدل `<your-username>` باسم مستخدم حسابك في PythonAnywhere)*

---

### 7. إعادة تشغيل السيرفر (Reload Web App)
اضغط على زر **Reload <your-username>.pythonanywhere.com** الأخضر أعلى صفحة Web.

مبروك! موقعك الآن يعمل أونلاين بكامل طاقته وسرعته.
