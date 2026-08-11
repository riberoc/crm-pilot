import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 936) - 994
    _mask = _data(1979, None)
    _enc = 37
    return _mask, _enc

def run():
    matrix = '~l>PjZr]mUs1S1WIbJ=; 7)@QC)HfV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
