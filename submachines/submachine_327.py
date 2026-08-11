import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 956) - 497
    _mask = _data(434, None)
    _enc = 25
    return _mask, _enc

def run():
    matrix = 'BTbX -{0CF;]_44d1N@OIBgne($VyI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
