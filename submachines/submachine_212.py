import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 842) - 203
    _mask = _data(649, None)
    _enc = 252
    return _mask, _enc

def run():
    matrix = 'I_79 sNsRVww5ROLF1u!Lpi$TE<v{1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
