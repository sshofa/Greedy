class Clothes(object):
    def __init__(self, n, v, p):
        self.name = n
        self.value = v
        self.price = p
    def getValue(self):
        return self.value
    def getPrice(self):
        return self.price
    def getDesire(self):
        return self.getValue()/self.getPrice()
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.price) + '>'
def buildShoppingCart(names, values, prices):
    """names, values, prices lists of same length.
    name a list of strings
    values and prices lists of numbers
    returns lists of Clothes"""
    ShoppingCart = []
    for i in range(len(values)):
        ShoppingCart.append(Clothes(names[i], values[i], prices[i]))
    return ShoppingCart
def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
    keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction, reverse=True)
    result = []
    totalValue, totalPrice = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if(totalPrice+itemsCopy[i].getPrice()) <= maxCost:
            result.append(itemsCopy[i])
            totalPrice += itemsCopy[i].getPrice()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print(' ', item)
def testGreedys(clothes, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'price')
    testGreedy(clothes, maxUnits, Clothes.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'price')
    testGreedy(clothes, maxUnits, lambda x: 1/Clothes.getPrice(x))
    print('\nUse greedy by desire to allocate', maxUnits, 'price')
    testGreedy(clothes, maxUnits, Clothes.getDesire)
names = ['red dress', 'sunny dress', 'running sneakers', 'shorts', 'bathing suit', 'baseball cap']
prices = [90, 90, 60, 20, 20, 10]
values = [100, 70, 70, 90, 60, 20]
clothes = buildShoppingCart(names, values, prices)
testGreedys(clothes, 150)
