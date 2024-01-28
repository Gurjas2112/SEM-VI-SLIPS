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

    def first_element(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    # Creating a queue
    my_queue = Queue()

    # Enqueue elements to the Queue using user input
    elements = input("Enter the elements to enqueue: ").split()
    
    for i in elements:
        my_queue.enqueue(i)

    # Displaying the queue
    print("Queue:", my_queue.items)

    # Dequeue elements from the queue
    print("Dequeued element:", my_queue.dequeue())

    # Displaying the front element of the queue
    print("Front element:", my_queue.first_element())

    # Displaying the size of the queue
    print("Size of the queue:", my_queue.size())