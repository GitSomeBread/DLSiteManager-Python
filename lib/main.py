import argparse
import asyncio
import Constants
import CoreModule

def main():
    parser = argparse.ArgumentParser(description="A program that manage your local DLSite archives.")
    parser.add_argument("Action",type = str)
    parser.add_argument("Targets", nargs='*')
    parser.add_argument("--format", "-f", type = str, nargs='+', default=Constants.default_format)
    parser.add_argument("--recursion", "-r", action="store_true")

    args = parser.parse_args()
    if (args.Action.upper() == "rename".upper()):
        CoreModule.rename_directories(args.format, *args.Targets).get()


if __name__ == "__main__":
    main()