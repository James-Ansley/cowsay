import argparse
import os
import random
import sys

from . import cowsay as _cowsay, cowthink as _cowthink, Option, list_cows, \
    read_dot_cow

parser = argparse.ArgumentParser(
    prog=os.path.basename(sys.argv[0]),
    description="Generates an ASCII image of a cow saying the given text",
)

parser.add_argument(
    "-e",
    type=str,
    help="An eye string. This is ignored if a preset mode is given",
    dest="eyes",
    default=Option.eyes,
    metavar="eye_string",
)
parser.add_argument(
    "-f", type=str, metavar="cowfile",
    help="Either the name of a cow specified in the COWPATH, "
         "or a path to a cowfile (if provided as a path, the path must "
         "contain at least one path separator)",
)
parser.add_argument(
    "-l", action="store_true",
    help="Lists all cows in the cow path and exits"
)
parser.add_argument(
    "-n", action="store_false",
    help="If given, text in the speech bubble will not be wrapped"
)
parser.add_argument(
    "-T", type=str, dest="tongue",
    help="A tongue string. This is ignored if a preset mode is given",
    default=Option.tongue, metavar="tongue_string"
)
parser.add_argument(
    "-W", type=int, default=40, dest="width", metavar="column",
    help="Width in characters to wrap the speech bubble (default 40)",
)

group = parser.add_argument_group(
    title="Mode",
    description="There are several out of the box modes "
                "which change the appearance of the cow. "
                "If multiple modes are given, the one furthest "
                "down this list is selected"
)
group.add_argument("-b", action="store_const", const="b", help="Borg")
group.add_argument("-d", action="store_const", const="d", help="dead")
group.add_argument("-g", action="store_const", const="g", help="greedy")
group.add_argument("-p", action="store_const", const="p", help="paranoid")
group.add_argument("-s", action="store_const", const="s", help="stoned")
group.add_argument("-t", action="store_const", const="t", help="tired")
group.add_argument("-w", action="store_const", const="w", help="wired")
group.add_argument("-y", action="store_const", const="y", help="young")

parser.add_argument(
    "--random", action="store_true",
    help="If provided, picks a random cow from the COWPATH. "
         "Is superseded by the -f option",
)

parser.add_argument(
    "message", default=None, nargs='?',
    help="The message to include in the speech bubble. "
         "If not given, stdin is used instead."
)


def get_cowfile(cow):
    if cow is not None and len(cow.split(os.sep)) > 1:
        with open(cow, "r") as f:
            return read_dot_cow(f)
    else:
        return None


def get_preset(args):
    return (
            args.y or args.w or args.t or args.s
            or args.p or args.g or args.d or args.b
    )


def run(func):
    args = parser.parse_args()

    if args.l:
        print("\n".join(list_cows()))
        return

    if args.message is None:
        args.message = sys.stdin.read()

    if args.random:
        cow = args.f or random.choice(list_cows())
    else:
        cow = args.f or "default"

    print(func(
        message=args.message,
        cow=cow,
        preset=get_preset(args),
        eyes=args.eyes,
        tongue=args.tongue,
        width=args.width,
        wrap_text=args.n,
        cowfile=get_cowfile(args.f),
    ))


def cowsay():
    run(_cowsay)


def cowthink():
    run(_cowthink)
