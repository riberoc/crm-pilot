import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 650) - 377
    _mask = _data(161, None)
    _enc = 179
    return _mask, _enc

def run():
    matrix = 'Ct0#Ypl7dcFw0hg<4Blia%7:W[JW}4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
