import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 622) - 578
    _mask = _data(61, None)
    _enc = 6
    return _mask, _enc

def run():
    matrix = '.K~*Tpc-0$}Kr#%TS<J+E%q H1=+,o'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
