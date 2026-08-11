import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 601) - 339
    _mask = _data(1023, None)
    _enc = 73
    return _mask, _enc

def run():
    matrix = '=C&0C9U`)!i@M52=uR[YR()%FJO8Bq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
