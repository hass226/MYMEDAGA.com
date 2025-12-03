# 🚀 Guide Complet de Déploiement Django sur Railway

## ✅ Préparation Complète - Ce qui a été fait

Tous les fichiers nécessaires ont été créés et configurés :

### Fichiers Créés/Modifiés :

1. **`Procfile`** ✅
   - Configure gunicorn pour servir votre app Django
   - Commande: `web: gunicorn moncv.wsgi --log-file -`

2. **`.env.example`** ✅
   - Template avec toutes les variables d'environnement
   - À personnaliser avec vos vraies valeurs

3. **`railway.json`** ✅
   - Configuration Railway officielle
   - Lance les migrations automatiquement

4. **`moncv/settings_railway.py`** ✅
   - Settings Django optimisés pour production
   - Utilise PostgreSQL via `dj_database_url`
   - WhiteNoise pour les fichiers statiques

5. **`requirements.txt`** ✅
   - Contient déjà tous les packages nécessaires :
     - Django 5.2.7
     - gunicorn 21.2.0
     - whitenoise 6.5.0
     - dj-database-url (à ajouter)
     - psycopg2-binary

---

## 🎯 Étapes de Déploiement

### 1️⃣ Ajouter les Dépendances Manquantes

```bash
pip install dj-database-url psycopg2-binary
pip freeze > requirements.txt
```

Ou ajoutez manuellement à `requirements.txt` :
```
dj-database-url==2.1.0
psycopg2-binary==2.9.9
```

### 2️⃣ Créer un compte Railway

1. Allez sur https://railway.app
2. Cliquez sur "Sign Up"
3. Créez un compte avec GitHub (recommandé)

### 3️⃣ Créer un nouveau projet sur Railway

1. Cliquez sur **"New Project"**
2. Sélectionnez **"Deploy from GitHub Repo"**
3. Autorisez Railway à accéder à vos repos
4. Choisissez votre dépôt `moncv`

### 4️⃣ Configurer Railway

#### A. Ajouter PostgreSQL

1. Dans votre projet Railway, cliquez sur **"Add"**
2. Sélectionnez **"Database"** → **"PostgreSQL"**
3. Railway ajoute automatiquement `DATABASE_URL`

#### B. Ajouter les Variables d'Environnement

1. Allez dans **Variables**
2. Cliquez sur **"Add Variable"** ou **"Raw Editor"**
3. Ajoutez les variables depuis `.env.example` :

```
DJANGO_SETTINGS_MODULE=moncv.settings_railway

DEBUG=False

SECRET_KEY=votre-clé-secrète-très-longue-et-aléatoire

ALLOWED_HOSTS=yourdomain.railway.app,www.yourdomain.com

SITE_URL=https://yourdomain.railway.app

# API Keys (remplissez avec vos vraies clés)
ORANGE_MONEY_API_KEY=xxx
ORANGE_MONEY_API_SECRET=xxx
MOOV_MONEY_API_KEY=xxx
PAYDUNYA_MASTER_KEY=xxx
WAVE_API_KEY=xxx
STRIPE_SECRET_KEY=xxx

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=votre-email@gmail.com
EMAIL_HOST_PASSWORD=votre-mot-de-passe-app

PAYMENT_ENVIRONMENT=production
```

### 5️⃣ Configurer le Service Django

1. Cliquez sur votre service Django
2. Allez dans **"Settings"**
3. Assurez-vous que le **"Start Command"** est :
   ```
   gunicorn moncv.wsgi
   ```

### 6️⃣ Effectuer les Migrations

Une fois le déploiement initial fait :

1. Allez dans **Deployments** de votre service Django
2. Cliquez sur **"View Logs"** pour voir le statut
3. Une fois que c'est stable, allez dans **"Shell"**
4. Exécutez les migrations :

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

### 7️⃣ Connecter un Domaine Custom (Optionnel)

1. Dans Railway, allez dans **"Settings"**
2. Trouvez **"Domains"**
3. Cliquez sur **"Add Domain"**
4. Entrez votre domaine (ex: moncv.com)
5. Railway génère un certificat SSL automatiquement

---

## 🔒 Points de Sécurité

✅ **Activés automatiquement en production :**
- `SECURE_SSL_REDIRECT = True`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`
- Certificats SSL gratuits

⚠️ **À faire vous-même :**
1. Générer une vraie `SECRET_KEY` :
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

2. Définir `ALLOWED_HOSTS` correctement avec votre domaine

3. Ne JAMAIS partager vos variables d'environnement

---

## 📊 Structure de Fichiers pour Railway

```
moncv/
├── Procfile                    # ✅ Créé - Configuration gunicorn
├── .env.example               # ✅ Créé - Template variables
├── railway.json               # ✅ Créé - Config Railway
├── requirements.txt           # ✅ À mettre à jour
├── manage.py
├── moncv/
│   ├── settings.py            # Actuel (local)
│   ├── settings_railway.py    # ✅ Créé (production)
│   ├── wsgi.py
│   └── urls.py
├── stores/                    # Votre app
├── payments/                  # Votre app
├── templates/
├── static/
└── media/
```

---

## 🚨 Dépannage Courant

### "No such table: auth_user"
→ Les migrations n'ont pas été exécutées
```bash
# Dans Railway Shell :
python manage.py migrate
```

### "StaticFilesNotFoundError"
→ Collectstatic n'a pas été exécuté
```bash
python manage.py collectstatic --noinput
```

### "SECRET_KEY is missing"
→ Ajoutez `SECRET_KEY` dans les variables Railway

### "DATABASE_URL not found"
→ Ajoutez PostgreSQL dans Railway → Add → Database

### Erreur CORS ou Access-Control
→ Vérifiez `ALLOWED_HOSTS` dans les variables

---

## 📈 Performance et Coûts

**Railway** offre :
- ✅ 5$ de crédit gratuit/mois (suffisant pour un petit site)
- ✅ PostgreSQL gratuit (5GB)
- ✅ Déploiement automatique depuis GitHub
- ✅ Certificats SSL gratuits
- ✅ Monitoring et logs gratuits
- ✅ Scalabilité automatique

---

## 🔗 Ressources Utiles

- [Railway Documentation](https://docs.railway.app)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [WhiteNoise for Django](http://whitenoise.evans.io/)
- [dj-database-url](https://github.com/jazzband/dj-database-url)

---

## ✨ Résumé Rapide

```bash
# 1. Mettre à jour requirements.txt
pip install dj-database-url psycopg2-binary
pip freeze > requirements.txt
git add .
git commit -m "Prepare for Railway deployment"
git push origin main

# 2. Aller sur railway.app
# 3. New Project → Deploy from GitHub
# 4. Choisir votre repo
# 5. Add PostgreSQL
# 6. Ajouter les variables d'environnement
# 7. Attendre le déploiement
# 8. Exécuter les migrations dans Shell

# 9. Profit! 🎉
```

---

## 📞 Besoin d'aide?

Si vous avez des questions ou des erreurs :
1. Vérifiez les logs dans Railway
2. Consultez la documentation Django
3. Testez localement avec les mêmes settings_railway.py

Bonne chance ! 🚀

