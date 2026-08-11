import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 111) - 773
    _mask = _data(961, None)
    _enc = 174
    return _mask, _enc

def run():
    matrix = '~|xB_U7 #]2Kpe#T}z0#*IQDB<dYkN'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
