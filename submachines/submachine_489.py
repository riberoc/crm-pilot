import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 970) - 558
    _mask = _data(347, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = ';318P*r~^jAmAT_%uo*V>3hWO; #D^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
