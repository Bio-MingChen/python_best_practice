import click

@click.command()
@click.argument("position_arg")
@click.option("--option_arg","-o",help="Help can be use to option arguments")
@click.option("--bool_","-b",is_flag=True,help="This is a boolean option")
def click_func(**kwargs):
    """\b
    Usage: click_example.py <position_arg> <options>
    This annotation will appear when you input --help
    add '\\b' make annotation output multiple lines
    """
    for k,v in kwargs.items():
        print(f'Argument {k}: {v}')

if __name__ == "__main__":
    click_func()
