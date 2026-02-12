# Módulo. CLI y automatización
import typer

from advance_level.laboratory17.app import orders_mock

app = typer.Typer(help="CLI to manage memory orders ")


@app.command()
def list_orders():
    orders = orders_mock.get_orders()
    if not orders:
        typer.echo("No orders.")
        return
    for o in orders:
        typer.echo(f"{o['id']}: {o['name']}")


@app.command()
def create_order(name: str):
    new_order = orders_mock.add_order(name)
    typer.echo(f"Ordencreate: {new_order['id']}: {new_order['name']}")


@app.command()
def delete_order(order_id: int):
    if orders_mock.delete_order(order_id):
        typer.echo(f"Orden {order_id} deleted")
    else:
        typer.echo(f"Order not found {order_id}")
