import os


def main():
    print("This is ordinary submodule 'd' called from " +
          os.path.abspath("."))


if __name__ == "__main__":
    main()
