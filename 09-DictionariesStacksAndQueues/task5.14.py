###
# Customer service queue with automatic ticket numbers
#
import queue

customers = queue.Queue()
next_ticket = 1

while True:
    print('1. New customer (take ticket)')
    print('2. Serve next customer')
    print('0. Quit')
    choice = input('Select option: ')

    if choice == '1':
        customers.put(next_ticket)
        print(f'Your ticket number: {next_ticket}')
        next_ticket += 1            # kolejny numerek zawsze o 1 wiekszy
    elif choice == '2':
        if not customers.empty():
            ticket = customers.get()     # FIFO - pierwszy w kolejce
            print(f'Now serving ticket number: {ticket}')
        else:
            print('No customers waiting.')
    elif choice == '0':
        break