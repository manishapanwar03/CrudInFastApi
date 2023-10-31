from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def manisha():
    return {
        'message':'heyy!I am manisha'
    }
    
@app.get("/avani")
def Avani():
    return {
        'message':'heyy!I am Avani'
    }