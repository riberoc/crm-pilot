import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 132) - 637
    _mask = _data(937, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = '8aJ6F6hmmM <|YYLc+ukWRvEHoU|Bq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
