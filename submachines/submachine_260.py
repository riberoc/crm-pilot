import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 567) - 863
    _mask = _data(333, None)
    _enc = 17
    return _mask, _enc

def run():
    matrix = 'k[&F)LWb+o =_$@IS=a#$?w~k#fr|i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
