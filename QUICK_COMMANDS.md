# 📟 Commandes Rapides Railway

## ⚡ 1-2-3 Déploiement

```bash
# 1. Générer une SECRET_KEY
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# 2. Vérifier que tout fonctionne
python manage.py migrate --plan
python manage.py collectstatic --noinput --dry-run

# 3. Commit et push
git add .
git commit -m "Deploy to Railway"
git push origin main
```

## 🎯 Configuration Railway - Variables Essentielles

Copiez-collez dans Railway → Variables:

```
DEBUG=False
SECRET_KEY=<votre-clé-générée>
ALLOWED_HOSTS=yourdomain.railway.app
SITE_URL=https://yourdomain.railway.app
DJANGO_SETTINGS_MODULE=moncv.settings_railway
PAYMENT_ENVIRONMENT=production
```

## 🔧 Après Déploiement - Commands à Exécuter

```bash
# Dans Railway → Shell:

# 1. Migrations
python manage.py migrate

# 2. Créer un superuser
python manage.py createsuperuser

# 3. Collectez les fichiers statiques
python manage.py collectstatic --noinput

# 4. Créer les répertoires de logs
mkdir -p logs
```

## 🧪 Tests Locaux

```bash
# Avant d'envoyer sur Railway, testez localement:

# 1. Migrer la base
python manage.py migrate

# 2. Vérifier la syntaxe
python -m py_compile moncv/settings_railway.py

# 3. Collecter les statics
python manage.py collectstatic --noinput

# 4. Lancer le serveur
python manage.py runserver
```

## 🐛 Dépannage Rapide

### Site ne charge pas
```bash
# 1. Vérifier les logs
# Railway → Votre service → Logs

# 2. Vérifier les migrations
python manage.py migrate

# 3. Vérifier les statics
python manage.py collectstatic --noinput
```

### Erreur "ModuleNotFoundError"
```bash
# Ajouter le package dans requirements.txt
pip install <nom-du-package>
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add missing package"
git push
```

### Erreur "ALLOWED_HOSTS"
```bash
# Vérifier dans Railway → Variables
# ALLOWED_HOSTS doit contenir votre domaine
ALLOWED_HOSTS=yourdomain.railway.app,www.yourdomain.com
```

### Erreur "Static files not found"
```bash
# Railway → Shell:
python manage.py collectstatic --noinput
```

## 📊 Monitoring

```bash
# Voir les logs en temps réel
# Railway → Votre service → Logs

# Voir l'utilisation des ressources
# Railway → Metrics

# Voir les variables d'environnement
# Railway → Variables
```

## 🔄 Mettre à Jour le Site

```bash
# Simplement pusher votre code!
git add .
git commit -m "Your message"
git push origin main

# Railway redéploie automatiquement
```

## 🗄️ Gérer la Base de Données

```bash
# Railway → Postgres database → Connect
# Utilisez pgAdmin ou DBeaver pour gérer

# Ou via shell Django:
python manage.py dbshell
```

## 💾 Sauvegarde de la Base

```bash
# Dans Railway Shell:
python manage.py dumpdata > backup.json

# Pour restaurer:
python manage.py loaddata backup.json
```

## 📈 Optimisations Futures

```bash
# Ajouter Redis pour le cache
# Railway → Add → Redis

# Augmenter la RAM
# Railway → Settings → Increase Memory

# Scaler horizontalement
# Railway → Settings → Replicas
```

## 🔐 Mise à Jour de SECRET_KEY

```bash
# 1. Générer une nouvelle clé
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# 2. L'ajouter dans Railway → Variables
SECRET_KEY=<nouvelle-clé>

# 3. Railway redéploie automatiquement
```

## 🌍 Ajouter un Domaine Custom

1. Railway → Settings → Domains
2. Ajouter votre domaine
3. Mettre à jour les DNS
4. Railroad génère automatiquement un certificat SSL

## 📞 Utiles

```bash
# Générer SECRET_KEY
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Vérifier les migrations
python manage.py migrate --plan

# Vérifier les statics
python manage.py collectstatic --noinput --dry-run

# Nettoyer la base
python manage.py flush

# Créer un superuser
python manage.py createsuperuser

# Voir les tables
python manage.py dbshell

# Exporter les données
python manage.py dumpdata > data.json

# Importer les données
python manage.py loaddata data.json
```

---

**Besoin d'aide?** → Consultez `DEPLOY_RAILWAY.md` pour le guide complet!

