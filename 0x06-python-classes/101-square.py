#!/usr/bin/python3
# """ Defines a square with a size attribute"""


class Square:
    """square class with size attribute

    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size 
        self.__position = position   
    
    @property
    def size(self):
        return (self.__size)
    
    @property
    def position(self):
        return (self.__position)
    @size.setter
    def size(self, value):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        


    
    @position.setter
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """ Calculates the area of a square"""
        return self.__size * self.__size
    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        for i in range(0, self.__position[1]):
            print("") 
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="") 
            for k in range(0, self.__size):
                print("#", end="") 
            print("")
#=================================================================================


#!/usr/bin/python3
class SinglyLinkedList:
    """class for a singly-linked list."""

    def __init__(self):
        """Initalizing a  SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the List.

        Args:
            value (Node): The new Node to be inserted.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Defines representation of a SinglyLinkedList."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
    
 
#===========================================================================
#!/usr/bin/python3   
class Square:
    """square class with size attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size 
        self.__position = position   
    
    @property
    def size(self):
        return (self.__size)
    
    @property
    def position(self):
        return (self.__position)
    @size.setter
    def size(self, value):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        


    
    @position.setter
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """ Calculates the area of a square"""
        return self.__size * self.__size
    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        for i in range(0, self.__position[1]):
            print("") 
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="") 
            for k in range(0, self.__size):
                print("#", end="") 
            print("")
    
    def __str__(self):
    """Defines the print function representation of a Square."""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        for i in range(0, self.__position[1]):
            print("") 
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="") 
            for k in range(0, self.__size):
                print("#", end="") 
            print("")
    return ("")
