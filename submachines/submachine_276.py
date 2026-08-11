import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 693) - 754
    _mask = _data(370, None)
    _enc = 220
    return _mask, _enc

def run():
    matrix = 'J[igF+_;, 8zK},D,Z,1l:7juxj^;q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
