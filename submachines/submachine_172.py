import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 384) - 278
    _mask = _data(43, None)
    _enc = 157
    return _mask, _enc

def run():
    matrix = ':wELO?ozn-{<-XK%HEW0HH<edA#K|('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
