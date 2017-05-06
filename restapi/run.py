"""Run the REST API application."""

from sys import argv

from backend import DEBUG, app

if __name__ == "__main__":
    argc = len(argv)

    if argc == 2:
        try:
            argHost, argPort = argv[1].split(":")
            app.run(argHost, int(argPort), debug=DEBUG)
        except Exception as e:
            print("Error: input not understood." + e)
    else:
        print("Error: please give ip:port as one positional argument.")
