main_dict = {'global':
               {'parent': None,
                'variables': set()
               }
          }

count = int(input())


def create(namespace, parent):
    main_dict[namespace] = {'parent': parent,
                            'variables': set()}


def get(namespace, var):
    if var in main_dict[namespace]['variables']:
        print(namespace)
        return namespace
    else:
        if main_dict[namespace]['parent'] == None:
            print(None)
            return None
        get(main_dict[namespace]['parent'], var)
        return



def add(namespace, var):
    main_dict[namespace]['variables'].add(var)


for i in range(count):
    cmd, namesp, arg = input().split()
    if cmd == 'add':
        add(namesp, arg)
    elif cmd == 'get':
        get(namesp, arg)
    elif cmd == 'create':
        create(namesp, arg)
