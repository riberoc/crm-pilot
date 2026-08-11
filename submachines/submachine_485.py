import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 654) - 650
    _mask = _data(92, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = 'K+/DB-z+%h/)V`$Q{s?-?~=x CRhDe'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
