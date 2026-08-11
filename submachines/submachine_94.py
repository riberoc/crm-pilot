import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 798) - 355
    _mask = _data(262, None)
    _enc = 168
    return _mask, _enc

def run():
    matrix = '0V&WKiune#&|B8rG/vN~vcPiTii[&u'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
