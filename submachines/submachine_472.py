import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 442) - 182
    _mask = _data(175, None)
    _enc = 84
    return _mask, _enc

def run():
    matrix = 'qOng?_|/Ykl ;O&529p>(K[4({9KXd'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
