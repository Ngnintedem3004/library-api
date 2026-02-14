### install environnement  virtuel python 
```markdown
   python -m venv .venv`
### activate environnement 
```markdown
   .venv\Scripts\activate
### Installer les dépendances 
```markdown
   pip install fastapi uvicorn 
### Upgrade 
```markdown
   python.exe -m pip install --upgrade pip`
### Vérifier l'installation
```markdown
   python -c import fastapi; print(fastapi.__version__)
### Lancer le serveur 
 ```markdown
    uvicorn app.main:app --reload
### Intégrer la base de données Postgres 
```markdown
   pip install fastapi uvicorn sqlalchemy psycopg2-binary`

