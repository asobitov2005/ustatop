# Ustatop

## O'rnatish bo'yicha ko'rsatmalar

### 1. Git orqali loyihani yuklab olish

```bash
git clone https://github.com/asobitov2005/ustatop.git
cd ustatop
```

### 2. Virtual muhit yaratish va faollashtirish
```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3. Talab qilinadigan kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4. Migratsiyalarni bajarish

```bash
python manage.py migrate
```

### 5. Superuser yaratish
```bash
python manage.py createsuperuser
```

### 6. Serverni ishga tushirish
```bash
python manage.py runserver
```
