# lti-arithmetic
Arithmetic manipulation for scipy.signal.lti TransferFunction

LTI system representations in scipy do not offer built-in composability.
Given two instances of `scipy.signal.lti`, for example, `H` and `G`,
you cannot directly write `H * G`.

This package defines a `scipy.signal.lti`-compatible `TransferFunction`
that permits standard arithmetical combination: `H + G`, `H - G`, `H * G`,
 `H / G`, and `H**n`. In addition, the parallel combination
(reciprocal of reciprocal sums) of systems is available by writing `H | G`.

The package also defines functions `Z_R`, `Z_C`, and `Z_L` that represent
the impedance of a resistance, capacitance, and inductance, respectively,
as LTI systems that can be composed to represent the transfer function
of a larger network.

For convenience, the package also defines `s` so that transfer functions
can be written as rational expressions in `s`.

## Examples

```
>>> from ltiarithmetic import TransferFunction, Z_R, Z_C, Z_L, s
```

Compute the product of two LTI systems:
```
>>> H = TransferFunction([1,2,3],[1])
>>> G = TransferFunction[[1],[2,3,4])
>>> H * G
TransferFunction(
array([0.5, 1. , 1.5]),
array([1. , 1.5, 2. ]),
dt: None
)
```

Compute the transfer function of a RC lowpass filter:
```
Z_1 = Z_R(1000.)
Z_2 = Z_C(1e-9)
H = Z_2 / (Z_1 + Z_2)
```

Construct LTI systems from rational expressions in `s`:
```
import math
w0 = 2 * math.pi * 1000.
Q = 2.
H = 1/(1 + s / (Q * w0) + (s / w0)**2)
```
