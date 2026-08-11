import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 732) - 270
    _mask = _data(776, None)
    _enc = 197
    return _mask, _enc

def run():
    matrix = 'o8x jai<g7Bm*):R>]YI3C|]hnb:DK'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
