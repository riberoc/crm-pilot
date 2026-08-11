import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 648) - 737
    _mask = _data(502, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = '/0&e<35d&B-wk?=KI3X .Xvt}ezVCa'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
