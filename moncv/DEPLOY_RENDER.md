# Déploiement sur Render — Guide pas à pas
Ce guide explique comment déployer l'application Django `moncv` sur Render (Managed Service). Il suppose que tu as le repository connecté à Render (GitHub/GitLab). Ce guide automatise les étapes essentielles : dépendances, migrations, staticfiles et variables d'environnement.
- Compte Render (https://render.com)
- Accès au repository (GitHub/GitLab)
Dis-moi si tu veux que je configure aussi le stockage des médias sur S3 (j'ai déjà ajouté les dépendances) ou que j'ajoute un `render.yaml` avec une base PostgreSQL auto-créée (selon les capacités de ton compte Render).
- Clé AWS S3 (optionnel) si tu veux stocker les médias (recommandé)
### Guide rapide pour ajouter S3 sur Render
1. Crée un bucket S3 et note le nom et la région.
2. Dans Render > Environment, ajoute :
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_STORAGE_BUCKET_NAME`
   - `AWS_S3_REGION_NAME` (optionnel)
   - `USE_S3_STATIC=true` si tu veux servir aussi les static depuis S3 (sinon WhiteNoise les sert)
3. Déploie : Render exécutera `collectstatic`. Si `USE_S3_STATIC=true`, staticfiles iront sur S3.

### Guide rapide pour PostgreSQL sur Render
1. Dans Render, crée `New` -> `Postgres` -> choisis plan.
2. Après création, copie la `DATABASE_URL` dans l'environnement du Web Service.
3. Déploie — le `releaseCommand` exécutera `migrate`.

### Vérification post-déploiement
- Vérifie les logs Render pour `releaseCommand` → migrations et collectstatic.
- Ouvre l'URL fournie par Render et teste l'upload de médias.
- Vérifie que les assets static sont chargés et que les médias uploadés sont présents dans S3 (si activé).

## Fichiers importants
- `render.yaml` : configuration du service web (présent)
- `.env.example` : variables d'environnement recommandées
- `moncv/moncv/settings_base.py` et `moncv/moncv/settings_prod.py` : configuration
- `moncv/requirements.txt` et `moncv/backend/requirements.txt` : dépendances

## Étapes sur Render
1. Créer un nouveau Web Service dans Render
   - Type: `Web Service`
   - Branch: la branche contenant ton code (ex: `main`)
   - Environment: `Python`
   - Build Command: (déjà dans `render.yaml`) installe les dépendances
   - Start Command: (déjà dans `render.yaml`) `cd moncv && gunicorn moncv.wsgi:application --bind 0.0.0.0:$PORT --workers 3`

2. Définir les variables d'environnement (Environment Variables) dans le tableau de bord Render
   - `SECRET_KEY` : génère une clé Django sécurisée
   - `DATABASE_URL` : fourni par Render (voir étape Postgres) ou ta BDD externe
   - `ALLOWED_HOSTS` : domaine Render (ex: `moncv.onrender.com`)
   - `SITE_URL` : `https://<ton-domaine>.onrender.com`
   - Toutes les clefs API (paiements, OpenAI, etc.) listées dans `.env.example`

3. (Recommandé) Ajouter une base de données PostgreSQL via Render
   - Dans Render, crée un "Managed Database" PostgreSQL
   - Après création, copie la `DATABASE_URL` fournie et colle-la dans l'Environment Variable `DATABASE_URL` du Web Service

4. Stockage des médias (fichiers uploadés)
   - Option A (recommandé) : Utiliser AWS S3 ou autre stockage extérieur et configurer Django `DEFAULT_FILE_STORAGE` avec `django-storages`.
   - Option B (rapide) : Utiliser le stockage de fichiers local de Render — attention: les fichiers peuvent être volatils lors de nouveaux déploiements. Pas recommandé pour production.

5. Lancer le déploiement
   - Commit/push de ton code -> Render buildera automatiquement
   - Le `releaseCommand` dans `render.yaml` exécute : `python manage.py migrate` et `python manage.py collectstatic --noinput`

## Commandes utiles (local)
```sh
python -m pip install --upgrade pip
pip install -r moncv/moncv/requirements.txt -r moncv/backend/requirements.txt
cd moncv
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
gunicorn moncv.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

## Notes importantes
- `SECRET_KEY` ne doit jamais être commité dans le repo.
- Utilise PostgreSQL en production (le `settings_prod.py` supporte `dj_database_url`).
- WhiteNoise est configuré pour servir les fichiers statiques (`STATICFILES_STORAGE` + middleware).
- Pour les médias persistants, configure S3 et `django-storages`.

## Variables à vérifier/ajouter dans Render
- `SECRET_KEY`, `DATABASE_URL`, `ALLOWED_HOSTS`, `SITE_URL`
- `EMAIL_*` si tu veux activer l'envoi d'emails
- Toutes les clefs de paiement (ORANGE_MONEY_API_KEY, PAYDUNYA_*, etc.)

---
Si tu veux, je peux :
- créer la configuration pour utiliser S3 (`django-storages`) et ajouter les dépendances correspondantes,
- ou créer un `render.yaml` alternatif qui déploie un conteneur Docker (si tu préfères déployer par image).

Dis-moi si tu veux que je configure aussi le stockage des médias sur S3 ou que j'ajoute un `render.yaml` avec une base PostgreSQL auto-créée (selon les capacités de ton compte Render).