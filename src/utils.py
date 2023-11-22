import os

def clearConsole():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        print("\033c")
    else:
        pass