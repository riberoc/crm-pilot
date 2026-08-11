import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 105) - 716
    _mask = _data(831, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = 'Hf88 hf0Lu{n|/5SA5i2<R?+SgisJ('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
