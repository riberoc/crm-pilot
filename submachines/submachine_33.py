import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 501) - 120
    _mask = _data(329, None)
    _enc = 64
    return _mask, _enc

def run():
    matrix = ']|s2 R28$5[)%_/82a*P0-WiQsy_NI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
