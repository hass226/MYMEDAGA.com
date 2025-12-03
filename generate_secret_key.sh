#!/bin/bash

# Script pour générer une SECRET_KEY Django sécurisée

echo "🔐 Génération d'une SECRET_KEY Django sécurisée..."
echo ""

python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

echo ""
echo "✅ Copie cette clé et ajoute-la dans Railway:"
echo "   1. Railway → Variables"
echo "   2. Ajoute: SECRET_KEY=<la-clé-ci-dessus>"
echo ""
