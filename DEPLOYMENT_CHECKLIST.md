# ✅ Checklist Déploiement Railway

## 🎯 Avant le Déploiement

### Préparation du Code
- [ ] Fichier `Procfile` créé
- [ ] Fichier `.env.example` créé
- [ ] Fichier `railway.json` créé
- [ ] Fichier `moncv/settings_railway.py` créé
- [ ] Fichier `requirements.txt` à jour avec:
  - [ ] Django >= 4.0
  - [ ] gunicorn >= 20.0
  - [ ] whitenoise >= 6.0
  - [ ] dj-database-url >= 1.0
  - [ ] psycopg2-binary >= 2.9
  - [ ] python-dotenv

### Tests Locaux
- [ ] Code sans erreurs de syntaxe
- [ ] `python manage.py collectstatic --noinput` fonctionne
- [ ] `python manage.py migrate` fonctionne
- [ ] Fichiers statiques sont générés

### Code Versioning (Git)
- [ ] Tous les changements commitpés
- [ ] Code pushé vers main/master sur GitHub

---

## 🚀 Sur Railway

### Créer le Projet
- [ ] Compte Railway créé
- [ ] Nouveau projet créé
- [ ] GitHub repo sélectionné
- [ ] Déploiement initial lancé

### Configurer la Base de Données
- [ ] PostgreSQL ajouté (Add → Database → PostgreSQL)
- [ ] Variable `DATABASE_URL` disponible
- [ ] Connexion PostgreSQL vérifiée

### Ajouter les Variables d'Environnement

#### Obligatoires
- [ ] `DEBUG=False`
- [ ] `SECRET_KEY=<votre-clé-générée>`
- [ ] `ALLOWED_HOSTS=yourdomain.railway.app,yourdomain.com`
- [ ] `SITE_URL=https://yourdomain.railway.app`
- [ ] `DJANGO_SETTINGS_MODULE=moncv.settings_railway`
- [ ] `DATABASE_URL=<auto-généré-par-PostgreSQL>`

#### APIs de Paiement (si utilisées)
- [ ] `ORANGE_MONEY_API_KEY`
- [ ] `ORANGE_MONEY_API_SECRET`
- [ ] `MOOV_MONEY_API_KEY`
- [ ] `MOOV_MONEY_API_SECRET`
- [ ] `PAYDUNYA_MASTER_KEY`
- [ ] `PAYDUNYA_PRIVATE_KEY`
- [ ] `PAYDUNYA_TOKEN`
- [ ] `WAVE_API_KEY`
- [ ] `STRIPE_SECRET_KEY`

#### Email (recommandé)
- [ ] `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
- [ ] `EMAIL_HOST=smtp.gmail.com` (ou votre provider)
- [ ] `EMAIL_PORT=587`
- [ ] `EMAIL_USE_TLS=True`
- [ ] `EMAIL_HOST_USER=votre-email@gmail.com`
- [ ] `EMAIL_HOST_PASSWORD=votre-mot-de-passe-app`

#### Production
- [ ] `PAYMENT_ENVIRONMENT=production`

### Configuration du Service
- [ ] Start Command: `gunicorn moncv.wsgi`
- [ ] Region sélectionné (de préférence proche)
- [ ] Auto-deploy activé (recommandé)

---

## 🔧 Après Déploiement

### Migrations et Setup Initial
- [ ] Aller dans le shell de Railway
  ```bash
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py collectstatic --noinput
  ```

### Vérifications
- [ ] Site accessible depuis votre domaine
- [ ] Admin panel accessible (`/admin/`)
- [ ] Pas d'erreurs dans les logs
- [ ] Fichiers statiques chargés correctement (CSS, JS)
- [ ] Base de données accessible
- [ ] SendGrid/Email fonctionne

### Domaine Custom (Optionnel)
- [ ] Domaine acheté
- [ ] Domaine configuré dans Railway
- [ ] Certificat SSL généré automatiquement
- [ ] DNS mis à jour (si nécessaire)

### Monitoring
- [ ] Logs Railway vérifiés
- [ ] No errors dans les logs
- [ ] Performance acceptable
- [ ] Quotas utilisés raisonnables

---

## 🆘 Dépannage Commun

### Erreur: "ModuleNotFoundError: No module named 'X'"
```bash
# Solution: Ajouter le package dans requirements.txt
pip install X
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add missing dependency"
git push
```

### Erreur: "relation does not exist"
```bash
# Solution: Migrations non appliquées
# Railway → Shell :
python manage.py migrate
```

### Erreur: "Static files not found"
```bash
# Solution: collectstatic non exécuté
# Railway → Shell :
python manage.py collectstatic --noinput
```

### Erreur: "ALLOWED_HOSTS"
```bash
# Solution: Vérifier la variable d'environnement
# Railway → Variables → ALLOWED_HOSTS
# Doit contenir: yourdomain.railway.app
```

### Erreur: "No Such Table"
```bash
# Solution: Les migrations n'ont pas été appliquées
# Railway → Shell :
python manage.py migrate
```

### Site très lent
- [ ] Vérifier les logs pour les erreurs
- [ ] Augmenter la RAM du dyno
- [ ] Optimiser les requêtes de base de données
- [ ] Utiliser Redis pour le cache

---

## 📚 Ressources Utiles

- [Railway Docs](https://docs.railway.app)
- [Django Deployment](https://docs.djangoproject.com/en/5.2/howto/deployment/)
- [Procfile Reference](https://devcenter.heroku.com/articles/procfile)
- [WhiteNoise Django](http://whitenoise.evans.io/)

---

## 🎉 Succès!

Si vous arrivez ici sans erreurs, votre site Django est live sur Railway! 🚀

Pour les mises à jour futures, faites simplement :
```bash
git push origin main
```

Et Railway se redéploie automatiquement!

