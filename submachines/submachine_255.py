import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 724) - 386
    _mask = _data(138, None)
    _enc = 196
    return _mask, _enc

def run():
    matrix = '(&?+8C,qx[c3-oq-~RE>{JU5eC]Epd'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
