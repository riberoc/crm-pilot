import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 410) - 418
    _mask = _data(64, None)
    _enc = 53
    return _mask, _enc

def run():
    matrix = 'iEBpM9m8cQAv% KU5hw-P5~k[jsi6-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
