class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.numbers = [i for i in range(maxNumbers)]
        self.mp = set()
        

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if len(self.numbers) == 0:
            return -1
        number = self.numbers.pop()
        self.mp.add(number)
        return number
        

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number not in self.mp
        

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.mp:
            self.mp.remove(number)
            self.numbers.append(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)