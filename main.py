from fastapi import FastAPI
from routes.student import student_router


#create the app
app = FastAPI()

#register the routers
app.include_router(student_router)
