## install environnement virtuel python

````bash
python -m venv .venv
### activate environnement

```bash
.venv\Scripts\activate

### Installer les dépendances

```bash
pip install fastapi uvicorn

### Upgrade

```bash
python.exe -m pip install --upgrade pip

### Vérifier l'installation

```bash
python -c import fastapi; print(fastapi.**version**)

### Lancer le serveur

```bash
uvicorn app.main:app --reload

### Intégrer la base de données Postgres

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
````
