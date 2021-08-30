from textwrap import dedent
import argparse

def main(kwargs):
    for k,v in kwargs.items():
        print(f"Argument {k:>30}: {v}")

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

    parser.add_argument("position",help="This argument is required")
    parser.add_argument("--option","-o",help="This argument is optional")
    parser.add_argument("--required_option","-ro",required=True,help="This option argument is required")
    parser.add_argument("--bool","-b",action="store_true",help="This option is a boolean argument")
    parser.add_argument("--choices","-c",choices=["awesome","brilliant","smart","excellent"],help="choose a content from %(choices)s")
    parser.add_argument("--type_option","-t",type=int,metavar="int",default=1,help="you can restrict argument to designated type")
    parser.add_argument("--nargs","-n",nargs="*",help="you can give arbitrary number of arguments")
    parser.add_argument("--abcde","-a",dest="custmised_arg_name",help="you can use dest to rename argument name used in program")
    parser.add_argument("--version","-v",action="version",version="%(prog)s v1.0",help="version argument")
    parser.add_argument(
        '--sum', dest='accumulate', action='store_const', const=sum,
        default=max, help='sum the integers (default: find the max)')

    args = parser.parse_args()
    main(vars(args))