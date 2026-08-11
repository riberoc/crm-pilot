import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 751) - 232
    _mask = _data(913, None)
    _enc = 158
    return _mask, _enc

def run():
    matrix = 'eiti#4iF E^?7~B|P~n37CN!b.ciIk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
