# 🚀 RENDER DEPLOYMENT GUIDE

Déployer votre Django sur Render en quelques minutes

---

## 📋 Vue d'ensemble

Ce projet est configuré pour se déployer sur [Render](https://render.com) avec:

- **Web Service**: Python 3.11 avec Gunicorn
- **Database**: PostgreSQL gratuite
- **Static Files**: WhiteNoise
- **Settings**: Configuration Django pour production

---

## ⚡ Quick Start (15 minutes)

### 1. Créer un compte Render
- Allez sur https://render.com
- Sign up avec GitHub

### 2. Créer un Web Service
- New → Web Service
- Connectez votre repo
- Configuration:
  ```
  Name: moncv
  Runtime: Python 3.11
  Build: pip install -r requirements.txt && python manage.py collectstatic --noinput
  Start: gunicorn moncv.wsgi
  ```

### 3. Ajouter PostgreSQL
- Data → New PostgreSQL
- Render génère `DATABASE_URL` automatiquement ✅

### 4. Configurer variables d'environnement
Copy-paste depuis `RENDER_COMPLETE_CONFIG.env`:
```
DEBUG=False
SECRET_KEY=django-insecure-...
ALLOWED_HOSTS=votre-url.onrender.com  ⚠️ À MODIFIER!
SITE_URL=https://votre-url.onrender.com  ⚠️ À MODIFIER!
DJANGO_SETTINGS_MODULE=moncv.settings_railway
```

### 5. Déployer
Render démarre le build automatiquement. Attendez 5-10 minutes.

### 6. Accéder au site
```
https://moncv.onrender.com
https://moncv.onrender.com/admin
```

---

## 📚 Documentation Complète

- **[RENDER_VISUAL_GUIDE.txt](RENDER_VISUAL_GUIDE.txt)** - Guide étape par étape avec captures
- **[RENDER_ACTION_PLAN.txt](RENDER_ACTION_PLAN.txt)** - Plan d'action rapide
- **[RENDER_COMPLETE_CONFIG.env](RENDER_COMPLETE_CONFIG.env)** - Toutes les variables

---

## 📁 Fichiers de déploiement

```
Procfile                    # Commandes de déploiement
render.yaml                 # Configuration Render (optionnel)
requirements.txt            # Dépendances Python
moncv/settings_railway.py   # Configuration Django
.env.example                # Variables d'exemple
```

---

## 🔧 Configuration détaillée

### Procfile
```
release: python manage.py migrate
web: gunicorn moncv.wsgi --log-file -
```

Le `release` command exécute les migrations automatiquement au déploiement.

### render.yaml
Optionnel mais recommandé pour l'infrastructure-as-code:
```yaml
services:
  - type: web
    name: moncv
    env: python
    startCommand: gunicorn moncv.wsgi
    buildCommand: pip install -r requirements.txt && python manage.py collectstatic --noinput
```

### settings_railway.py
Configuration Django production-ready:
- `DEBUG = False` en production
- `ALLOWED_HOSTS` depuis les variables
- `DATABASES` auto-détecte `DATABASE_URL`
- `WhiteNoise` pour les fichiers statiques
- Sécurité SSL/HTTPS activée

---

## 🔐 Variables d'environnement ESSENTIELLES

| Variable | Valeur | Exemple |
|----------|--------|---------|
| `DEBUG` | `False` | false |
| `SECRET_KEY` | Clé secrète Django | django-insecure-... |
| `ALLOWED_HOSTS` | Votre domaine | moncv.onrender.com |
| `SITE_URL` | URL complète | https://moncv.onrender.com |
| `DJANGO_SETTINGS_MODULE` | Chemin settings | moncv.settings_railway |
| `DATABASE_URL` | Auto-généré ✅ | postgres://... |

---

## ⚠️ Troubleshooting

### "Application failed to start"
1. Vérifier les logs (Logs tab)
2. Vérifier `ALLOWED_HOSTS`
3. Vérifier que `render.yaml` et `Procfile` existent
4. Cliquer "Redeploy"

### "502 Bad Gateway"
1. Attendre 1-2 minutes (démarrage)
2. Actualiser la page
3. Vérifier les logs

### "Database not found"
1. Attendre 3-5 minutes (PostgreSQL initialisation)
2. Vérifier `DATABASE_URL` dans Environment
3. Relancer le déploiement

### Static files manquants
1. Vérifier `collectstatic` dans Build Command
2. Vérifier `WHITENOISE_STORAGE` dans settings
3. Redéployer

---

## 🛠️ Commandes utiles (Shell Render)

```bash
# Créer un superuser
python manage.py createsuperuser

# Vérifier configuration
python manage.py check

# Voir migrations
python manage.py showmigrations

# Accéder à la base
python manage.py dbshell

# Collecter fichiers statiques
python manage.py collectstatic --noinput
```

---

## 📞 Support

**Render Documentation**: https://render.com/docs
**Django Documentation**: https://docs.djangoproject.com/

---

## ✅ Checklist avant déploiement

- [ ] Compte Render créé et repo connecté
- [ ] Web Service créé (Python 3.11)
- [ ] PostgreSQL ajoutée
- [ ] Variables d'environnement configurées
- [ ] `ALLOWED_HOSTS` et `SITE_URL` modifiés
- [ ] Build lancé avec succès
- [ ] Site accessible (https://votre-url.onrender.com)
- [ ] Admin accessible et fonctionnel
- [ ] Migrations exécutées

---

## 🎉 C'est tout!

Votre site Django est maintenant en production sur Render!

**Site**: https://moncv.onrender.com  
**Admin**: https://moncv.onrender.com/admin  
**Logs**: https://render.com/dashboard

