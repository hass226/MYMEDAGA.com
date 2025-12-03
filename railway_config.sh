#!/bin/bash

# Configuration automatique pour Railway
# Ce script configure les variables d'environnement Railway

echo "⚙️  Configuration automatique pour Railway"
echo ""

# Générer une SECRET_KEY
SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

# Obtenir le domaine Railway
RAILWAY_DOMAIN="yourdomain.railway.app"

# Créer un fichier .env temporaire pour les tests
cat > .env.railway.test << EOF
# Configuration Railway - À utiliser dans Railway Console
DEBUG=False
SECRET_KEY=$SECRET_KEY
ALLOWED_HOSTS=$RAILWAY_DOMAIN,localhost,127.0.0.1
SITE_URL=https://$RAILWAY_DOMAIN
DJANGO_SETTINGS_MODULE=moncv.settings_railway

# À compléter avec vos vraies clés
ORANGE_MONEY_API_KEY=
ORANGE_MONEY_API_SECRET=
MOOV_MONEY_API_KEY=
PAYDUNYA_MASTER_KEY=
WAVE_API_KEY=
STRIPE_SECRET_KEY=

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

PAYMENT_ENVIRONMENT=production
EOF

echo "✅ Fichier .env.railway.test créé avec:"
echo "   - SECRET_KEY générée"
echo "   - Domaine: $RAILWAY_DOMAIN"
echo "   - DEBUG=False (production)"
echo ""
echo "📝 Prochaines étapes:"
echo "   1. Modifier .env.railway.test avec vos vraies valeurs"
echo "   2. Copier-coller le contenu dans Railway → Variables"
echo ""
