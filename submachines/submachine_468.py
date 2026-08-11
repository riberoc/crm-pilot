import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 204) - 823
    _mask = _data(792, None)
    _enc = 133
    return _mask, _enc

def run():
    matrix = 'VQB.^Qp-u)5i?FaaeH3YvfUCT.hyZn'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
