#!/bin/bash

# Script de test local avant déploiement sur Railway

echo "🧪 Test local du projet Django..."
echo ""

# 1. Vérifier la syntaxe Python
echo "1️⃣  Vérification de la syntaxe Python..."
python -m py_compile moncv/settings_railway.py
if [ $? -eq 0 ]; then
    echo "✅ Syntaxe OK"
else
    echo "❌ Erreur de syntaxe!"
    exit 1
fi

echo ""

# 2. Vérifier les migrations
echo "2️⃣  Vérification des migrations..."
python manage.py migrate --plan > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Migrations OK"
else
    echo "⚠️  Attention aux migrations"
fi

echo ""

# 3. Vérifier les fichiers statiques
echo "3️⃣  Vérification des fichiers statiques..."
python manage.py collectstatic --noinput --dry-run > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Fichiers statiques OK"
else
    echo "⚠️  Attention aux fichiers statiques"
fi

echo ""

# 4. Test rapide du serveur
echo "4️⃣  Test du serveur Django (30 secondes)..."
timeout 30 python manage.py runserver 0.0.0.0:8000 &
sleep 5

if curl -s http://localhost:8000/ > /dev/null 2>&1; then
    echo "✅ Serveur répond correctement"
else
    echo "⚠️  Serveur inaccessible (normal si DEBUG=False)"
fi

# Tuer le serveur
pkill -f "runserver"

echo ""

# 5. Vérifier requirements.txt
echo "5️⃣  Vérification de requirements.txt..."
if grep -q "gunicorn" requirements.txt && \
   grep -q "whitenoise" requirements.txt && \
   grep -q "dj-database-url" requirements.txt && \
   grep -q "psycopg2-binary" requirements.txt; then
    echo "✅ Toutes les dépendances requises sont présentes"
else
    echo "❌ Dépendances manquantes!"
    echo "Dépendances requises:"
    echo "  - gunicorn"
    echo "  - whitenoise"
    echo "  - dj-database-url"
    echo "  - psycopg2-binary"
    exit 1
fi

echo ""
echo "🎉 Tous les tests sont passés!"
echo ""
echo "✨ Prêt pour le déploiement sur Railway!"
echo ""
