
class Shortener():
    def __init__(self) -> None:
        self.DB = {}
        self.Counter = [-1]
    
    def intToChar(self, x: int) -> str:
        if x in range(0, 26):
            return chr(ord('a')+x)
        if x in range(26, 52):
            return chr(ord('A')+x-26)
        if x in range(52, 62):
            return chr(ord('0')+x-52)

    def clearCounter(self, counter: list[int]) -> None:
        for charI in range(len(counter)):
            counter[charI] = 0
    
    def evaluate(self, counter) -> None:
        for i in range(len(counter)-1, -1, -1):
            if counter[i] == 61:
                counter[i] = 0
                if i == 0:
                    counter.append(0)
                else:
                    counter[i-1] += 1

    def incCounter(self, counter: list[int]) -> None:
        length = len(counter)
        counter[length-1] += 1
        self.evaluate(counter)

    def CounterToStr(self, counter: list[int]) -> str:
        s = ''
        print(counter)  
        for digit in counter:
            char = self.intToChar(digit)
            s += char
        return s

    def decode(self, shorturl: str) -> str:
        if self.DB[shorturl]:
            return self.DB[shorturl]

    def encodeAny(self, url: str) -> str:
        self.incCounter(self.Counter)
        shorturl = self.CounterToStr(self.Counter)
        self.DB[shorturl] = url
        return shorturl

    def encodeSpecific(self, shorturl, url: str) -> str:
        if self.isAvailableURL(shorturl):
            self.DB[shorturl] = url
            return 'Encoded successfully'
        else:
            return 'This shorturl is not available'

    def isAvailableURL(self, shorturl: str) -> bool:
        return shorturl not in self.DB

main = Shortener()