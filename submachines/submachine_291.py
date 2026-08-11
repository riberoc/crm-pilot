import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 245) - 195
    _mask = _data(496, None)
    _enc = 67
    return _mask, _enc

def run():
    matrix = 'm -83h#z>QmnY{xhq*Bf]sS),hbhb+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
