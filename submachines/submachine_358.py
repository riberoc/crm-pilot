import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 474) - 435
    _mask = _data(1016, None)
    _enc = 119
    return _mask, _enc

def run():
    matrix = 'FU)do/t]w65ra:8}p~)l5Hjlaf$nF3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
