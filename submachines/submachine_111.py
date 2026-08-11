import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 156) - 703
    _mask = _data(898, None)
    _enc = 77
    return _mask, _enc

def run():
    matrix = 'Q=E(2.#CUN@B|!wa.m ZsgY#xKbPv4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
