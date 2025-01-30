import threading
import time
from queue import Queue

class Messenger:
    def __init__(self):
        self.user_queues = {}
        self.lock = threading.Lock()

    def send_message(self, sender, receiver, message):
        with self.lock:
            if receiver not in self.user_queues:
                print(f"Error: {receiver} is not a valid user.")
                return
            self.user_queues[receiver].put((sender, message))

    def receive_messages(self, user):
        while True:
            if user not in self.user_queues:
                print(f"Error: {user} is not a valid user.")
                return
            if not self.user_queues[user].empty():
                sender, message = self.user_queues[user].get()
                print(f"[{sender} -> {user}]: {message}")
            time.sleep(1)

if __name__ == "__main__":
    messenger = Messenger()

    # Initialize queues for users
    users = ["Alice", "Bob", "Charlie"]
    for user in users:
        messenger.user_queues[user] = Queue()

    # Start receiver threads for users
    receiver_threads = []
    for user in users:
        receiver_thread = threading.Thread(target=messenger.receive_messages, args=(user,))
        receiver_thread.daemon = True
        receiver_thread.start()
        receiver_threads.append(receiver_thread)

    # Send some messages
    messenger.send_message("Alice", "Bob", "Hello Bob!")
    messenger.send_message("Bob", "Alice", "Hi Alice!")
    messenger.send_message("Charlie", "Alice", "Hey Alice!")

    # Wait for a while to allow messages to be processed
    time.sleep(2)

    # Send more messages
    messenger.send_message("Bob", "Charlie", "Hello Charlie!")
    messenger.send_message("Charlie", "Bob", "Hi Bob!")

    # Keep the main thread alive to keep the receiver threads running
    for receiver_thread in receiver_threads:
        receiver_thread.join()