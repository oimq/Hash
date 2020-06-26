from hasH import hasHXOR

if __name__=="__main__" :
    h4 = hasHXOR()
    print(h4.digest('adidas', 4))
    print(h4.digest('helloeveryworld', 4))