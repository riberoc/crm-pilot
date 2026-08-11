import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 232) - 701
    _mask = _data(899, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = ':vD9jFFq2z Hnd/Fqi-eB_``Hma,VJ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
