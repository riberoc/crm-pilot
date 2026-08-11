import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 324) - 878
    _mask = _data(640, None)
    _enc = 92
    return _mask, _enc

def run():
    matrix = '-?wckgzsxZ uxn+Zd?0h*AUI{AgA-p'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
