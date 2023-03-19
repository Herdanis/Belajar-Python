import click


@click.group
def mycommand():
    pass

@click.command
@click.option("--name", prompt="enter name", help="the name of user")
def hello(name):
    click.echo(f"hello {name}")


PRIORITIES = {
    "o" : "Optional",
    "h" : "High",
    "m" : "Mediun",
    "l" : "low"
}

@click.command
@click.argument("priority", type=click.Choice(PRIORITIES.keys()),default ="m")
@click.argument("todofile", type=click.Path(exists=False), required=0)
@click.option("-n","--name",prompt="todo name", help="the name of todo")
@click.option("-d","--desc",prompt="todo description", help="the description of todo")
def add_todo(name,desc,priority,todofile):
    filename = todofile if todofile is not None else "mytodo.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {desc} [Priority: {PRIORITIES[priority]}]\n")

@click.command
@click.argument("idx",type=int,required=1)
def delete_todo(idx):
    with open("mytodo.txt","r")as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("mytodo.txt","w")as f:
        f.write("\n".join(todo_list))
        f.write('\n')


mycommand.add_command(add_todo)
mycommand.add_command(delete_todo)

if __name__ == "__main__":
    mycommand()