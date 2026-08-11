import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 285) - 599
    _mask = _data(565, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = ',P eWs0X6F{V2(D&bq(EZiH+&~&>h2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
