"""Run the REST API application."""

from sys import argv

from backend import DEBUG, app
from utils import api

if __name__ == "__main__":
    argc = len(argv)
    print(argc)

    if argc > 1:
        if argv[1] == "start":
            try:
                argHost, argPort = argv[2].split(":")
                app.run(argHost, int(argPort), debug=DEBUG)
            except Exception as e:
                print("Error: input not understood. Ensure your input " +
                      "string is of the correct form.")
        elif argv[1] == "newapikey":
            try:
                print(api.addApiKey())
            except Exception as e:
                print("Error: input not understood. Ensure your input " +
                      "string is of the correct form.")
        else:
            print("Error: command '" + str(argv[1]) + "' not recognised.")
    else:
        print("Error: incorrect number of arguments to function.")
