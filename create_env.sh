#!/bin/bash

# Script pour créer un fichier .env personnalisé

echo "🛠️  Configuration Interactive pour Railway"
echo ""
echo "Ce script va générer votre fichier .env personnalisé"
echo ""

# Générer une SECRET_KEY
echo "🔐 Génération d'une SECRET_KEY..."
SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
echo "✅ SECRET_KEY générée"
echo ""

# Demander les informations
read -p "📝 Votre domaine Railway (ex: mysite.railway.app): " DOMAIN
DOMAIN=${DOMAIN:-mysite.railway.app}

read -p "📝 Domaine custom (optionnel, ex: mysite.com) [Laisser vide]: " CUSTOM_DOMAIN

read -p "📧 Email (pour les notifications): " EMAIL
EMAIL=${EMAIL:-contact@example.com}

read -p "💳 Mode paiement (sandbox ou production) [sandbox]: " PAYMENT_MODE
PAYMENT_MODE=${PAYMENT_MODE:-sandbox}

echo ""
echo "⚙️  Création du fichier .env..."
echo ""

# Créer le fichier .env
cat > .env << EOF
# ============================================
# Configuration Django Production - Railway
# ============================================

# Debug (JAMAIS True en production!)
DEBUG=False

# Secret Key (IMPORTANT: Gardez-la secrète!)
SECRET_KEY=$SECRET_KEY

# Domaine(s) autorisé(s)
ALLOWED_HOSTS=$DOMAIN${CUSTOM_DOMAIN:+,$CUSTOM_DOMAIN}

# URL du site
SITE_URL=https://$DOMAIN

# Module de settings Django
DJANGO_SETTINGS_MODULE=moncv.settings_railway

# ============================================
# Base de Données (Railway PostgreSQL)
# ============================================
# DATABASE_URL est automatiquement défini par Railway
# Si besoin de tester localement:
# DATABASE_URL=postgresql://user:password@localhost:5432/moncv

# ============================================
# Email Configuration
# ============================================
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=$EMAIL
CONTACT_EMAIL=$EMAIL

# ============================================
# Configuration des Paiements
# ============================================
PAYMENT_ENVIRONMENT=$PAYMENT_MODE

# Orange Money
ORANGE_MONEY_API_KEY=
ORANGE_MONEY_API_SECRET=
ORANGE_MONEY_MERCHANT_ID=
ORANGE_MONEY_ENVIRONMENT=$PAYMENT_MODE

# Moov Money
MOOV_MONEY_API_KEY=
MOOV_MONEY_API_SECRET=
MOOV_MONEY_MERCHANT_ID=
MOOV_MONEY_ENVIRONMENT=$PAYMENT_MODE

# MTN Mobile Money
MTN_MONEY_API_KEY=
MTN_MONEY_API_SECRET=
MTN_MONEY_ENVIRONMENT=$PAYMENT_MODE

# PayDunya
PAYDUNYA_MASTER_KEY=
PAYDUNYA_PRIVATE_KEY=
PAYDUNYA_TOKEN=
PAYDUNYA_MODE=$PAYMENT_MODE

# Wave API
WAVE_API_KEY=
WAVE_API_SECRET=
WAVE_ENVIRONMENT=$PAYMENT_MODE

# CinetPay
CINETPAY_API_KEY=
CINETPAY_SITE_ID=
CINETPAY_ENVIRONMENT=$PAYMENT_MODE

# Stripe
STRIPE_SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
STRIPE_WEBHOOK_SECRET=

# ============================================
# API WhatsApp & SMS
# ============================================
WHATSAPP_API_KEY=
SMS_GATEWAY_API_KEY=

# ============================================
# APIs IA
# ============================================
OPENAI_API_KEY=
ANTHROPIC_API_KEY=

# ============================================
# Configuration Avancée (Optionnel)
# ============================================
# CORS
CORS_ALLOW_ALL_ORIGINS=False

# Logging
LOG_LEVEL=INFO

EOF

echo "✅ Fichier .env créé!"
echo ""
echo "📋 Résumé:"
echo "   - Domain: $DOMAIN"
if [ ! -z "$CUSTOM_DOMAIN" ]; then
    echo "   - Custom Domain: $CUSTOM_DOMAIN"
fi
echo "   - Email: $EMAIL"
echo "   - Payment Mode: $PAYMENT_MODE"
echo "   - SECRET_KEY: Générée ✅"
echo ""
echo "⚠️  IMPORTANT:"
echo "   1. ⛔ Ne JAMAIS partager ce fichier ou le mettre sur GitHub"
echo "   2. 🔐 Remplissez les clés API vides avec vos vraies valeurs"
echo "   3. 📧 Testez la configuration email avant le déploiement"
echo "   4. 🚀 Utilisez ce .env pour les tests locaux uniquement"
echo ""
echo "Railway:"
echo "   1. Railway → Variables"
echo "   2. Cliquez sur 'Raw' ou 'Editor'"
echo "   3. Copiez le contenu du fichier .env (sauf DATABASE_URL)"
echo "   4. Collez-le dans Railway"
echo ""
echo "✨ Prêt pour le déploiement!"
echo ""
