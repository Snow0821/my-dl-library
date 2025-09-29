# Forward propagation
$ \hat y = \sigma (z) = \frac{1}{1 + e^{-z}}$

$ z = wx + b $

# Loss Calculation
$ L = yln(\hat y) + (1 - y)ln(1 - \hat y) $

# Weight and bias update

$ \hat w = w - \eta \frac{\partial L}{ \partial w} $

$ \hat b = b - \eta \frac{\partial L}{\partial b} $

# Common
$\frac{\partial L}{\partial \hat y} = \frac{y}{\hat y} + \frac{1 - y}{1 - \hat y}$

$\frac{\partial \hat y}{\partial z} = \frac{(1 + e^{-z})^{-1}}{\partial z} = \hat y(1 - \hat y)$

$\frac{\partial L}{\partial z} = \hat y - y$

# Weight update



# Bias update