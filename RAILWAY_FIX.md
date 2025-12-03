# 🚨 Fix pour Railway - Erreur de Build

## ❌ Problème Actuel
```
Failed to parse your service config. Error: build.builder: Invalid input
```

## ✅ Solution - FAIT!

Le fichier `railway.json` a été corrigé. 

---

## 🎯 Étapes à Faire Maintenant sur Railway

### 1️⃣ Configurer les Variables d'Environnement (OBLIGATOIRE!)

**⚠️ C'est l'étape la plus importante!**

Dans Railway:
1. Allez dans votre projet
2. Cliquez sur le service **web**
3. Allez dans **Variables**
4. Ajoutez ces variables OBLIGATOIRES:

```
DEBUG=False

SECRET_KEY=django-insecure-u&$6k_$uw$=c5-y67e!v+@8j#z!=z-&l!*3h5+n#&=m3h7-3(l

ALLOWED_HOSTS=web-production-0a048.up.railway.app

SITE_URL=https://web-production-0a048.up.railway.app

DJANGO_SETTINGS_MODULE=moncv.settings_railway

PAYMENT_ENVIRONMENT=sandbox
```

⚠️ **Remplacez le domaine** `web-production-0a048.up.railway.app` par votre vrai domaine!

### 2️⃣ Ajouter PostgreSQL (SI ce n'est pas fait)

1. Dans Railway, cliquez sur **+ Add**
2. Sélectionnez **Database** → **PostgreSQL**
3. Railway crée automatiquement **DATABASE_URL**
4. La variable apparaîtra dans **Variables**

### 3️⃣ Redéployer

Une fois les variables ajoutées:
1. Allez dans **Settings**
2. Cliquez sur **Redeploy Latest**
3. Ou commitez un changement sur GitHub et Railway redéploiera automatiquement

---

## 📋 Variables Minimalistes pour Tester

Si vous voulez tester rapidement, utilisez ceci:

```
DEBUG=False
SECRET_KEY=test-secret-key-for-testing-only-not-production
ALLOWED_HOSTS=*
DJANGO_SETTINGS_MODULE=moncv.settings_railway
DATABASE_URL=<auto-généré-par-PostgreSQL>
```

---

## 🔧 Si ça ne marche toujours pas

### Vérifier les Logs
1. Railway → Service web → **View Logs**
2. Cherchez les erreurs (rouge)
3. Les erreurs les plus communes:
   - `SECRET_KEY is missing` → Ajouter dans Variables
   - `relation does not exist` → Migrations non faites
   - `ALLOWED_HOSTS` → Domaine mal configuré

### Effectuer les Migrations
Une fois que le build réussit:
1. Railway → Service web → **Shell**
2. Exécutez:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

---

## ✅ Checklist Rapide

- [ ] Variables d'environnement ajoutées
- [ ] PostgreSQL ajouté
- [ ] Redéploiement lancé
- [ ] Build réussi (pas de messages d'erreur en rouge)
- [ ] Site accessible
- [ ] Migrations exécutées

---

## 📞 URL utiles

- **Votre site**: https://web-production-0a048.up.railway.app
- **Admin**: https://web-production-0a048.up.railway.app/admin/
- **Railway Docs**: https://docs.railway.app/

---

**Status**: ✅ railway.json fixé  
**Prochaine étape**: Ajouter les variables d'environnement sur Railway

