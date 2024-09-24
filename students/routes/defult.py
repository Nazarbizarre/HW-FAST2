from .. import app
names = []

@app.get("/add:{name}")
def main(name:str):
    if name in names:
        return "Name Already Exists"
    names.append(name)
    return "Name Added"

@app.get("/delete:{name}")
def delete(name:str):
    if name in names:
        names.remove(name)
        return "Name Deleted"
    return "Name does not exist"

@app.get("/show_all")
def show():
    return names