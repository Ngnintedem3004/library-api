## Install virtual  environment  python

```
python -m venv .venv
```

## Activate environment

```
.venv\Scripts\activate
```

## Install dependencies

```
pip install fastapi uvicorn
```

### Upgrade

```
python.exe -m pip install --upgrade pip
```

### Verify installation

```
python -c import fastapi; print(fastapi.**version**)
```

### Run the server

```
uvicorn app.main:app --reload
```

### Add postgress  database

```
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```
