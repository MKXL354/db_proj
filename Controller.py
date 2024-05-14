@app.post("/create_table")
def root(table: Table):
    print(table)
    db.create_table(table.name, table.attr)
    return table


@app.post("/insert_into_table")
def say_hello(name: str):
    return {"message": f"Hello {name}"}