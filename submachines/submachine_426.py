import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 271) - 430
    _mask = _data(863, None)
    _enc = 187
    return _mask, _enc

def run():
    matrix = '4psak)>96mp@c:;ThI2s)9{0t f2cf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
