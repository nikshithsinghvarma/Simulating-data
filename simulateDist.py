import sys
import math
import random
# giving the seed to random number
random.seed(2)


def bernoulli(arguments):
    if len(arguments) != 4:
        sys.exit('Incorrect number of arguments')
    n = int(arguments[1])
    p = float(arguments[3])
    if p < 0.0 or p > 1.0:
        sys.exit('Incorrect probability value ,enter value between 0 and 1')
    lis = []
    for i in range(0, n):
        temp = random.uniform(0, 1)
        if temp <= p:
            lis.append(1)
        else:
            lis.append(0)
    return lis


def binomial(arguments):
    if len(arguments) != 5:
        sys.exit('Incorrect number of arguments')
    n1 = int(arguments[1])
    n2 = int(arguments[3])
    p = float(arguments[4])
    if p < 0.0 or p > 1.0:
        sys.exit('Incorrect probability value ,enter value between 0 and 1')
    count = 0
    lis = []
    for i in range(0, n1):
        for j in range(0, n2):
            temp = random.uniform(0, 1)
            if temp <= p:
                count = count+1
        lis.append(count)
        count = 0
    return lis


def geometric(arguments):
    if len(arguments) != 4:
        sys.exit('Incorrect number of arguments')
    n = int(arguments[1])
    p = float(arguments[3])
    if p < 0.0 or p > 1.0:
        sys.exit('Incorrect probability value ,enter value between 0 and 1')
    lis = []
    for i in range(0, n):
        count = 0
        j = 0
        while j != 1:
            temp = random.uniform(0, 1)
            count = count+1
            if temp <= p:
                j = 1
        lis.append(count)
    return lis


def neg_binomial(arguments):
    if len(arguments) != 5:
        sys.exit('Incorrect number of arguments')
    n = int(arguments[1])
    k = int(arguments[3])
    p = float(arguments[4])
    if p < 0.0 or p > 1.0:
        sys.exit('Incorrect probability value ,enter value between 0 and 1')
    lis = []
    for i in range(0, n):
        count = 0
        j = 0
        while j < k:
            temp = random.uniform(0, 1)
            count = count + 1
            if temp <= p:
                j = j+1
        lis.append(count)
    return lis


def uniform(arguments):
    if len(arguments) != 5:
        sys.exit('Incorrect number of arguments')
    n = int(arguments[1])
    a = int(arguments[3])
    b = int(arguments[4])
    lis = []
    for i in range(0, n):
        u = random.uniform(0, 1)
        lis.append(a+u*(b-a))
    return lis


def exponential(arguments):
    if len(arguments) != 4:
        sys.exit('Incorrect number of arguments')
    n = int(arguments[1])
    lmd = float(arguments[3])
    lis = []
    for i in range(0, n):
        u = random.uniform(0, 1)
        x = ((-1)/lmd)*math.log(1-u)
        lis.append(x)
    return lis


def normal(arguments):
    if len(arguments) != 5:
        sys.exit('Incorrect number of arguments')
    n = int(arguments[1])
    if n % 2 != 0:
        n = n+1
    mu = float(arguments[3])
    std = float(arguments[4])
    lis = []
    for i in range(0, n):
        u1 = random.uniform(0, 1)
        u2 = random.uniform(0, 1)
        z1 = math.sqrt((-2)*math.log(u1))*math.cos(2*math.pi*u2)
        z2 = math.sqrt((-2)*math.log(u1))*math.sin(2*math.pi*u2)
        x1 = mu+std*z1
        x2 = mu+std*z2
        lis.append(x1)
        lis.append(x2)
    return lis


def gamma(arguments):
    if len(arguments) != 5:
        sys.exit('Incorrect number of arguments')
    n = int(arguments[1])
    alp = int(arguments[3])
    lmd = float(arguments[4])
    lis = []
    for i in range(0, n):
        s = 0
        for j in range(0, alp):
            u = random.uniform(0, 1)
            x = ((-1) / lmd) * math.log(1 - u)
            s = s+x
        lis.append(s)
    return lis


def arb_discreet_func(x, arguments):
    s = 0
    for i in range(0, x+1):
            s = s+arguments[i]
    return s


def arb_discreet(arguments):
    n = int(arguments[1])
    p = []
    lis = []
    for i in range(3, len(arguments)):
        p.append(float(arguments[i]))
    if sum(p) != 1:
        sys.exit('Sum of probabilities must be equal to 1')
    for j in range(0, n):
        u = random.uniform(0, 1)
        f = 1
        while f <= len(p):

            if arb_discreet_func(f-1, p) <= u:
                if arb_discreet_func(f, p) > u:
                    lis.append(f)
                    break
            else:
                lis.append(int(0))
                break
            f = f+1
    return lis


def poisson(arguments):
    if len(arguments) != 4:
        sys.exit('Incorrect number of arguments')
    n = int(arguments[1])
    lmd = float(arguments[3])
    lis = []
    for i in range(0, n):
        f = 0
        t = []
        while f >= 0:
            f = f+1
            u = random.uniform(0, 1)
            x = ((-1) / lmd) * math.log(u)
            t.append(x)
            if sum(t) > 1:
                break
        lis.append(f-1)
    return lis


if __name__ == '__main__':
    if sys.argv[2] == 'bernoulli':
        result = bernoulli(sys.argv)
    if sys.argv[2] == 'binomial':
        result=binomial(sys.argv)
    if sys.argv[2] == 'geometric':
        result = geometric(sys.argv)
    if sys.argv[2] == 'neg-binomial':
        result = neg_binomial(sys.argv)
    if sys.argv[2] == 'uniform':
        result = uniform(sys.argv)
    if sys.argv[2] == 'exponential':
        result = exponential(sys.argv)
    if sys.argv[2] == 'normal':
        result = normal(sys.argv)
    if sys.argv[2] == 'gamma':
        result = gamma(sys.argv)
    if sys.argv[2] == 'arb-discreet':
        result = arb_discreet(sys.argv)
    if sys.argv[2] == 'poisson':
        result = poisson(sys.argv)
    print(result)
