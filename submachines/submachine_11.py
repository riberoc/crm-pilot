import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 106) - 686
    _mask = _data(831, None)
    _enc = 178
    return _mask, _enc

def run():
    matrix = 'SA^Wt}1Ft{}stcTYsgNtr m*kClT&('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
