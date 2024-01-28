#Write a Python program to implement the concept of queue using list.


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)


# Example usage:
if __name__ == "__main__":
    # Creating a queue
    my_queue = Queue()

    # Enqueue elements
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)

    # Display the queue
    print("Queue:", my_queue.items)

    # Dequeue element
    dequeued_item = my_queue.dequeue()
    print("Dequeued item:", dequeued_item)

    # Peek at the front element
    front_item = my_queue.peek()
    print("Front item:", front_item)

    # Display the updated queue
    print("Updated Queue:", my_queue.items)

    # Check the size of the queue
    print("Size of the Queue:", my_queue.size())
