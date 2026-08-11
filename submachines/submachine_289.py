import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 132) - 327
    _mask = _data(679, None)
    _enc = 209
    return _mask, _enc

def run():
    matrix = 'm!kBKug>s8KM5wBqrmV4vxkU>#xdtt'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
