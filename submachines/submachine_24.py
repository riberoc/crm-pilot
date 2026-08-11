import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 576) - 625
    _mask = _data(141, None)
    _enc = 65
    return _mask, _enc

def run():
    matrix = 'nFtm9nr.l.5T4.F#7!TJ(GA0?0#}j '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
