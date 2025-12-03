# 🚀 Railway Setup - Étapes Simples

## 📍 Status Actuel
- ✅ Fichiers corrigés et poussés sur GitHub
- ⏳ Awaiting: Configuration manuelle sur Railway

---

## 🎯 À Faire Maintenant (5 minutes)

### Étape 1️⃣ : Variables d'Environnement

**Dans Railway:**
```
Railway → Votre projet → Service "web" → Variables
```

**Copiez-collez ceci (remplacez le domaine):**

```env
DEBUG=False
SECRET_KEY=django-insecure-u&$6k_$uw$=c5-y67e!v+@8j#z!=z-&l!*3h5+n#&=m3h7-3(l
ALLOWED_HOSTS=web-production-0a048.up.railway.app
SITE_URL=https://web-production-0a048.up.railway.app
DJANGO_SETTINGS_MODULE=moncv.settings_railway
PAYMENT_ENVIRONMENT=sandbox
```

✅ **Cliquez sur Save**

---

### Étape 2️⃣ : Ajouter PostgreSQL (Si ce n'est pas fait)

**Dans Railway:**
```
Railway → Votre projet → + Add → Database → PostgreSQL
```

- Railroad génère automatiquement **DATABASE_URL**
- Elle apparaît dans **Variables** du service web
- ✅ Rien à faire manuellement!

---

### Étape 3️⃣ : Redéployer

**Deux options:**

**Option A - Depuis Railway:**
```
Railway → Service web → Settings → Redeploy Latest
```

**Option B - Depuis GitHub:**
```bash
git commit --allow-empty -m "Trigger Railway redeploy"
git push origin main
```

Railway redéploiera automatiquement! 🚀

---

## ✅ Vérifier que ça Fonctionne

### Dans Railway - Logs
```
Railway → Service web → View Logs
```

**Cherchez:**
- ✅ `Starting development server` = Bon signe!
- ❌ `ERROR` = Mauvais signe

### Test d'Accès
- **Site**: https://web-production-0a048.up.railway.app
- **Admin**: https://web-production-0a048.up.railway.app/admin/
- **Status**: Doit retourner 200 OK

---

## 🔧 Après le Déploiement Réussi

Une fois que le site charge:

### Dans Railway - Shell
```
Railway → Service web → Shell
```

**Exécutez ces commandes:**
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

---

## 📊 Résumé Visual

```
┌─────────────────────────────────────────┐
│         RAILWAY CONFIGURATION           │
├─────────────────────────────────────────┤
│                                         │
│  1. Ajouter Variables ✅                │
│     └─ SECRET_KEY, DEBUG, etc.         │
│                                         │
│  2. Ajouter PostgreSQL ✅               │
│     └─ DATABASE_URL généré auto        │
│                                         │
│  3. Redéployer ✅                       │
│     └─ Via Railway ou GitHub push      │
│                                         │
│  4. Vérifier Logs ✅                    │
│     └─ Pas d'erreur (pas de rouge)     │
│                                         │
│  5. Exécuter Migrations ✅              │
│     └─ Railway → Shell                 │
│                                         │
│  6. Profit! ��                          │
│     └─ Site en ligne!                  │
│                                         │
└─────────────────────────────────────────┘
```

---

## ⚠️ Problèmes Courants

### "Build Failed"
**Cause:** Variables manquantes
**Solution:** Ajouter DEBUG, SECRET_KEY, ALLOWED_HOSTS

### "ModuleNotFoundError"
**Cause:** Dépendances manquantes
**Solution:** Vérifier requirements.txt

### "Relation does not exist"
**Cause:** Migrations non exécutées
**Solution:** Railway → Shell → `python manage.py migrate`

### "Static files not found"
**Cause:** collectstatic non exécuté
**Solution:** Railway → Shell → `python manage.py collectstatic --noinput`

---

## 🎯 Next Steps

1. ✅ Ajouter les variables sur Railway
2. ✅ Ajouter PostgreSQL
3. ✅ Redéployer
4. ✅ Vérifier les logs
5. ✅ Exécuter les migrations
6. 🎉 Profit!

**Total: ~10 minutes pour aller en production!**

