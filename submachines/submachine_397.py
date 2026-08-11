import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 746) - 337
    _mask = _data(192, None)
    _enc = 197
    return _mask, _enc

def run():
    matrix = '2S-rBMW|w;%=!N*ze-}d,5t6J()( Z'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
