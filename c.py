import os
# no need to import gitmodules for ordinary modules,
# try to run this script it should work as is
from ordinary_submodule import d


def main():
    print("This is git submodule 'c' called from " +
          os.path.abspath(".") +
          " and it is going to call main function from its ordinary submodule 'd':")
    d.main()


if __name__ == "__main__":
    main()
