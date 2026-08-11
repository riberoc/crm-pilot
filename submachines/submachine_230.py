import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 690) - 830
    _mask = _data(1674, None)
    _enc = 224
    return _mask, _enc

def run():
    matrix = 'eOrW+,`y+?v%,%6Ka:=-jA@l^D Nic'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
