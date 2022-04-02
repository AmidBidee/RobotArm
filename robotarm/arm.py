#!/usr/bin/python3
"""
RobotArm entry script v0.01
"""
from robotarm import controllers
import os
import pathlib
import sys

#BASE_DIR = pathlib.Path(__file__).resolve().parent

# maps keys to controller method
STATE_CONTROLLERS = {
    'list': 'controllers.StateController().list',
    'create': 'controllers.StateController().create',
    'activate': 'controllers.StateController().activate',
    'stop': 'controllers.StateController().stop',
    'delete': 'controllers.StateController().delete',
}

COMMAND_CONTROLLERS = {
    'execute': 'controllers.CommandController().executeCommand',
    'list': 'controllers.CommandController().listCommands'
}

TEST_CONTROLLERS = {
    'run': 'cotrollers.TestController().run'
}

API_STATUS_CONTROLLERS = {
    'health': 'controllers.APIStatusController().health_check',
}

def main():
    # maps keys to controller classes
    options = {
        '-v': 'v0.01',
        '-h': 'help',
        '-s': STATE_CONTROLLERS,
        '-c': COMMAND_CONTROLLERS,
        '-t': TEST_CONTROLLERS,
        '-p': 'Pipeline controller/handler',
        'status': API_STATUS_CONTROLLERS,
    }

    # extract file name and remove it
    args = sys.argv
    args_length = len(args)  # store args length

    arm_usage = 'Usage'
    file_name = args[0]

    # make sure length isn't less than 2
    if args_length < 2:
        exit(arm_usage)

    # remove file name
    del(args[0])

    # extract option and check if
    # option is valid
    option = args[0]
    if option in options.keys():
        pass
    else:
        exit(arm_usage)

    # remove option
    del(args[0])

    # check if option is version or help
    if args_length == 2:
        # Prints arm script version or help
        if option in ('-v', '-h'):
            print(options[option])
            exit()
        else:
            exit(arm_usage)

    # builds controller path
    # fails if controller method doesn't exists
    try:
        ct = options[option]

        if ct is COMMAND_CONTROLLERS:
            try:
                eval(ct[args[0]])(args)
            except KeyError:
                eval(ct['execute'])(args)
            exit()
        # if ct is TEST_CONTROLLERS:
            # pass
        else:
            # passes all arguments into controller method for now
            eval(ct[args[0]])(args)
    except KeyError:
        exit('Unknown option command')

if __name__ == '__main__':
    main()