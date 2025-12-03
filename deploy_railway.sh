#!/bin/bash

# Script de déploiement pour Railway
# Ce script prépare votre projet Django pour Railway

echo "🚀 Préparation du projet Django pour Railway..."
echo ""

# 1. Vérifier les fichiers requis
echo "📋 Vérification des fichiers requis..."

files=("Procfile" ".env.example" "requirements.txt" "moncv/settings_railway.py")

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file trouvé"
    else
        echo "❌ $file MANQUANT - À créer!"
    fi
done

echo ""

# 2. Vérifier les dépendances requises
echo "📦 Vérification des dépendances..."

required_packages=(
    "Django"
    "gunicorn"
    "psycopg2-binary"
    "whitenoise"
    "python-dotenv"
    "dj-database-url"
)

while IFS= read -r package; do
    for req_pkg in "${required_packages[@]}"; do
        if echo "$package" | grep -q "^${req_pkg}"; then
            echo "✅ $req_pkg trouvé"
        fi
    done
done < requirements.txt

echo ""

# 3. Instructions pour Railway
echo "🎯 Prochaines étapes pour le déploiement sur Railway:"
echo ""
echo "1️⃣  Allez sur https://railway.app"
echo "2️⃣  Créez un compte gratuit"
echo "3️⃣  Cliquez sur 'New Project' → 'Deploy from GitHub'"
echo "4️⃣  Sélectionnez votre dépôt GitHub"
echo "5️⃣  Railway détecte automatiquement Django"
echo ""
echo "6️⃣  Ajoutez les variables d'environnement:"
echo "    - Copiez le contenu de .env.example"
echo "    - Remplissez vos valeurs réelles"
echo "    - Ajoutez-les dans Railway → Variables"
echo ""
echo "7️⃣  Ajoutez PostgreSQL:"
echo "    - Railway → Add → Postgres"
echo "    - La variable DATABASE_URL sera créée automatiquement"
echo ""
echo "8️⃣  Effectuez les migrations:"
echo "    - Railway → Votre service Django → Shell"
echo "    - Exécutez: python manage.py migrate"
echo "    - Exécutez: python manage.py createsuperuser"
echo "    - Exécutez: python manage.py collectstatic --noinput"
echo ""
echo "✅ Terminé!"
echo ""
echo "📝 Fichiers créés:"
echo "   - Procfile (configuration gunicorn)"
echo "   - .env.example (variables d'environnement)"
echo "   - railway.json (configuration Railway)"
echo "   - moncv/settings_railway.py (settings pour production)"
echo ""
echo "💡 Conseil: Mettez à jour votre settings.py ou utilisez settings_railway.py"
echo ""
