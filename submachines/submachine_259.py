import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 984) - 722
    _mask = _data(315, None)
    _enc = 22
    return _mask, _enc

def run():
    matrix = '~ol|J6. $E_5&Qu?D#5E/lc&35U>2p'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
