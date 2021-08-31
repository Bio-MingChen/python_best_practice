import click

@click.command()
@click.argument("arg1",nargs=-1)
@click.argument("arg2",nargs=1)
@click.argument("arg_infile",type=click.File('r'))
@click.argument("arg_ofile",type=click.File('w'))
@click.argument("filepath",type=click.Path(exists=True))
@click.option("--count",required=True,default=1,type=int,show_default=True,help="option count")
@click.option("--option",nargs=2,type=float)
@click.option("--tup",type=(str,int))
@click.option("--bool_option",is_flag=True)
@click.option("--open/--no-open",default=False)
@click.option("--choices_option","-c",type=click.Choice(['MD5','SHA1'],case_sensitive=False))
@click.option("--username","-u",prompt=True,default=lambda:os.environ.get("USER",""),show_default="current_user")
def main(**args):
    for arg in args:
        click.echo(arg)

if __name__ == "__main__":
    main()