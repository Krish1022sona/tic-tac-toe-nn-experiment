import math

def softplus(x):
    return math.log(1 + math.exp(x))

def derivative_softplus(x):
    return 1 / (1 + math.exp(-x))

def ReLU(x):
    return max(0, x)

def derivative_ReLU(x):
    if x < 0 : return 0
    else: return 1

def softmax(outputs):
    # Numerical stability: subtract the maximum value
    max_val = max(outputs)
    shifted_outputs = [x - max_val for x in outputs]
    
    # Now compute exp of shifted values
    exp_outputs = [math.exp(x) for x in shifted_outputs]
    denominator = sum(exp_outputs)
    
    return [exp_val / denominator for exp_val in exp_outputs]

def cross_entropy(x):
    return -1 * math.log(x)

def cross_entropy_loss(cross_entropies):
    return sum(cross_entropies)

