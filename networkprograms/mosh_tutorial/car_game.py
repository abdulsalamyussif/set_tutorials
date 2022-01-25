command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'help':
        print('start - to start the car')
        print('start - to stop the car')
        print('start - to quit the car')
    elif command == 'start':
        if started:
            print('car has already started')
        else:
            started = True
            print('car started...readdy to go')
    elif command == 'stop':
        if not started:
            print('car has already stopped')
        else:
            started = False
            print('car has stopped..')
    elif command == 'quit':
        break
    else:
        print("I don't understand")
