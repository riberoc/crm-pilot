import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 869) - 870
    _mask = _data(1893, None)
    _enc = 141
    return _mask, _enc

def run():
    matrix = '`XJu@`US}V]SLv~mJP%==;/ Bd^vq('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
