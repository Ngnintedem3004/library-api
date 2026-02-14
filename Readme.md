# install environnement  virtuel python 
`python -m venv .venv`
# activate environnement 
`.venv\Scripts\activate `
# Installer les dépendances 
`pip install fastapi uvicorn `
# Upgrade 
`python.exe -m pip install --upgrade pip`
# Vérifier l'installation
`python -c import fastapi; print(fastapi.__version__)`
# Lancer le serveur 
uvicorn app.main:app --reload