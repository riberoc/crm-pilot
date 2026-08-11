import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 275) - 802
    _mask = _data(1331, None)
    _enc = 255
    return _mask, _enc

def run():
    matrix = ') `-G=D~,r![/58dj$`]#<]v.5d1&c'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
