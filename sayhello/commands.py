# author:LWZ
# datetime:2021/2/14 20:28

"""
文件说明：

"""
import click
from sayhello import app, db
from sayhello.models import Message


# 初始化数据库
@app.cli.command()
@click.option("--drop", is_flag=True, help='create after drop.')
def initdb(drop):
    if drop:
        click.confirm("此选项将会删除所有数据，确定吗？", abort=True)
        db.drop_all()
        click.echo("Drop tables")
    db.create_all()
    click.echo("initialized database..")


# 虚拟数据
@app.cli.command()
@click.option("--count", default=20, help="create fake message")
def forge(count):
    db.drop_all()
    db.create_all()

    from faker import Faker
    fake = Faker('en')
    click.echo("Working....")

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
        )
        db.session.add(message)

    db.session.commit()
    click.echo(f"Create {count} fake messages.")
