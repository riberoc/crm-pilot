import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 548) - 561
    _mask = _data(131, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = '=r 9x&X{|X!XnKoKusk4Oo6IIxUmw:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
