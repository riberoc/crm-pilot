import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 314) - 921
    _mask = _data(1471, None)
    _enc = 233
    return _mask, _enc

def run():
    matrix = 'I,ER8 W_.8S|aQ964!taPz/rh1HJMe'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
