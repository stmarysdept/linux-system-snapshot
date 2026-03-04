import datetime
import socket

def main():
    
    print("The current user is: ", end='')
    print(socket.gethostname())

    t = datetime.datetime.now()
    formatted_t = t.strftime("%d/%m/%Y, and it's currently: %H:%M:%S")
    print(f"The date is: {formatted_t}")

if __name__ == "__main__":
    main()