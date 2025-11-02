from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'TwinOps backend running successfully!'}
