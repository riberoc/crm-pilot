import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 286) - 141
    _mask = _data(12, None)
    _enc = 148
    return _mask, _enc

def run():
    matrix = 'N#(CSOgDt[LAd3?csh$27)3g[;.nN&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
