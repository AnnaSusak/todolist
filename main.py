from fastapi import FastAPI
from routes import router
#from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.include_router(router)
'''app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
'''app.add_middleware(
 CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)'''



