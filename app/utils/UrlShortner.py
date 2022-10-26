
class UrlShortner:
    alphabets = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    base = len(alphabets)
    alpha_dict = dict((c, v) for v, c in enumerate(alphabets))
  

    def encode(self ,num: int):  
        if not num:
           return self.alpha_dict[0]

        encoding = ""
        while num:
           num, rem = divmod(num, self.base)
           encoding = self.alphabets[rem] + encoding

        return encoding    

    def decode(self ,shortString: str):     
        num = 0
        for char in shortString:
           num = num * self.base + self.alpha_dict[char]

        return num

