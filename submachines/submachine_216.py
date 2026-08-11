import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 227) - 780
    _mask = _data(984, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = 'vKxo)9br`(#,+Q9uWkMy/Hr*jd= rW'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
