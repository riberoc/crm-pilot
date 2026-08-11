import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 433) - 412
    _mask = _data(938, None)
    _enc = 120
    return _mask, _enc

def run():
    matrix = 'R:Q^w() 0!p@BU>1n[2m)81b5nUcsO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
