import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 984) - 853
    _mask = _data(2028, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = 'K*^KwaH?M{eeM+^ va?lHdywRN%,dp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
