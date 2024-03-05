import uuid
from fastapi import FastAPI

app = FastAPI(
    title='API project',
    version='0.0.1'
)

@app.post('/api/v1register/')
async def register_user(username: str, email: str, password: str):
    return {
        'username': username,
        'email': email,
        'ID': str(uuid.uuid4()),
        'message': 'the user was created successfully',
        'status_code': 201
    }

@app.get('/api/v1datos/{ID}')
async def datos_usuarios(ID: str):
    return {
        'message': 'datos usuarios',
        'ID': ID,
        'username': 'Nombre usuario',
        'email': 'Email usuario'
    }

@app.post('/api/v1task/')
async def crear_task(ID: str, title: str, description: str, status: str):
    task_id = str(uuid.uuid4())
    return {
        'message': 'Tarea creada correctamente',
        'task_id': task_id
    }

@app.get('/api/v1tasks/{ID}')
async def lista_task_users(ID: str):
    return {
        'message': 'lista creada correctamente',
        'ID': ID,
        'tasks': []
    }
