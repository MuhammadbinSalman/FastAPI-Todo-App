from fastapi import FastAPI, Body, Depends
app : FastAPI = FastAPI()

# @app.get("/in/{pname}")
# def index(pname:str):
#     return {"message" : {"Get api response": f"for user {pname}"}}

# @app.post("/product")
# def greet(pname:str = Body(embed=True)):
#     return f"ok so {pname} is the body in post request"

@app.post("/todos/")
def create_todo( db = Body(embed=True)):
    return f"{db} is posted in db"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("APIs:app",reload=True)