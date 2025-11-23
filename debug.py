import os
import subprocess

print("🔍 DEBUG - Structure du projet Render")
print("=" * 50)

# Dossier courant
print(f"📁 Dossier courant: {os.getcwd()}")

# Liste tous les fichiers/dossiers
print("\n📁 Contenu racine:")
try:
    result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
    print(result.stdout)
except:
    items = os.listdir('.')
    for item in items:
        print(f"  - {item}")

# Recherche récursive
print("\n🔎 Recherche récursive de app.py:")
for root, dirs, files in os.walk('.'):
    for file in files:
        if 'app.py' in file or 'requirements' in file:
            print(f"✅ {os.path.join(root, file)}")

# Test différents chemins possibles
print("\n🧪 Tests de chemins:")
possible_paths = [
    '/opt/render/project/',
    '/opt/render/project/src/',
    '/opt/render/project/root/',
    './',
    './src/'
]

for path in possible_paths:
    if os.path.exists(path):
        print(f"📁 {path} - EXISTE")
        if os.path.exists(os.path.join(path, 'app.py')):
            print(f"   ✅ app.py trouvé dans {path}")
    else:
        print(f"📁 {path} - N'EXISTE PAS")

print("\n🎯 CHEMIN RECOMMANDÉ pour Start Command:")
if os.path.exists('./app.py'):
    print("👉 python app.py")
elif os.path.exists('./src/app.py'):
    print("👉 cd src && python app.py")
else:
    print("❌ Aucun app.py trouvé")
