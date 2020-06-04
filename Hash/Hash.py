class hashXOR :
    # clen : chop length
    def __init__(self, hdict=None) :
        self.hdict = hdict if hdict else { w:i for i,w in enumerate(
            [chr(i) for i in range(65,  91, 1)]+[chr(i) for i in range(97, 123, 1)]+\
            [chr(i) for i in range(48,  58, 1)]+list('!@#$%^&*()_+=-:;<>,./?'))
        }
        self.ndict = {i:w for w,i in self.hdict.items()}         
        self.blen = len("{:b}".format(len(self.hdict)-1)) # Maximum binary length
    
    # wlen = word length
    def digest(self, raw, wlen=5) :
        if type(raw) == type([]) : raw=''.join(raw)
        # Make csize times length word
        while len(raw) % wlen != 0 : raw += raw[:wlen-(len(raw)%wlen)]
        # We make hash code from chops
        binaries = [int(str('{:0'+str(self.blen)+'b}').format(self.hdict[s]), 2) for s in raw]
        # XOR operation
        for i in range(wlen) :
            inx = i+wlen
            while inx < len(raw) :
                binaries[i] ^= binaries[inx]
                inx += wlen
        # Make the code
        code = "".join([self.ndict[b%len(self.ndict)] for b in binaries[:wlen]])
        return code

if __name__=="__main__" :
    h4 = hashXOR()
    print(h4.digest('adidas', 4))