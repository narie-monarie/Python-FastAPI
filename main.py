from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware
#cors is a middle ware
# React will be running in this IP and PORT
client_apps = ['http://localhost:3000']

#create the app
app = FastAPI()

#register the routers
app.include_router(student_router)

# Register the cors so that we can enable 2 IPs to communicate with each other(Literally!!)

app.add_middleware(
    CORSMiddleware,
    allow_origins = client_apps,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)