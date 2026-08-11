import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 915) - 402
    _mask = _data(559, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = 'm3A 66G+~mK%:Amvo6RTsn^r9@fl+m'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
