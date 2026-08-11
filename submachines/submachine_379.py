import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 628) - 913
    _mask = _data(1663, None)
    _enc = 96
    return _mask, _enc

def run():
    matrix = 'MsFOFh4(c6=0k35EDDhDBATFR| kmU'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
