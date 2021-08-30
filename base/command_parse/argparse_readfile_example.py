import sys
import argparse
from textwrap import dedent

def main(kwargs):
    with kwargs["infile"] as indata,\
    kwargs["ofile"] as odata:
        for line in indata:
            odata.write(line)
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = "argparse_example", # default is sys.argv[0],
        formatter_class = argparse.RawDescriptionHelpFormatter,
        description = dedent('''
        Please do not mess up this text!
        --------------------------------
            I have indented it
            exactly the way
            I want it
            '''),
       epilog = "Contact:cm.bio@qq.com"
    )
    parser.add_argument("infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("ofile", nargs="?", type=argparse.FileType("w"), default=sys.stdout)

    args = parser.parse_args()
    main(vars(args))