import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 541) - 811
    _mask = _data(411, None)
    _enc = 64
    return _mask, _enc

def run():
    matrix = 'MQ-_L(dE1u$X^6OgAU-iGrp7RFiig!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
