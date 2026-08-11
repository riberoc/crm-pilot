import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 197) - 510
    _mask = _data(576, None)
    _enc = 128
    return _mask, _enc

def run():
    matrix = 'miM:Gn= `wfkKG{{2R7o2F4MmoFZ7n'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
