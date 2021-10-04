import click

## method 1 

# @click.group()
# def group():
#     """
#     .group method indicate a main function
#     """
#     pass

# @group.command()
# @click.option("--count",default=1,help="count to show")
# def sub_func1(count):
#     print(f"Your input: {count}")

# @group.command()
# @click.option("--count",default=2,help="count to show")
# def sub_func2():
#     print("Another sub func run...")
#     print(f"Your input: {count}")
##--------------------------------------------------

## method 2
@click.command()
@click.option("--count",default=1,help="count to show")
def sub_func1(count):
    print(f"Your input: {count}")

@click.command()
@click.option("--count",default=2,help="count to show")
def sub_func2():
    print("Another sub func run...")
    print(f"Your input: {count}")

@click.group()
def group():
    """
    .group method indicate a main function
    """
    pass

group.add_command(sub_func1)
group.add_command(sub_func2)

if __name__ == "__main__":
    group()