import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 373) - 807
    _mask = _data(725, None)
    _enc = 123
    return _mask, _enc

def run():
    matrix = '7z vFIBJy^TdE0@:$b#&BYm~ks{F]2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
