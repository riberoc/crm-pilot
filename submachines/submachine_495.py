import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 880) - 329
    _mask = _data(665, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = 'duAG=rNX=s/J}Q^o2ZH=${sJ}1NR X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
