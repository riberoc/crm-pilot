import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 650) - 383
    _mask = _data(832, None)
    _enc = 87
    return _mask, _enc

def run():
    matrix = '6|V7o:e,;u:{HgS}|zl:)7<}bBP3 {'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
