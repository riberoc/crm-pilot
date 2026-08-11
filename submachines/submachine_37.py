import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 895) - 749
    _mask = _data(91, None)
    _enc = 57
    return _mask, _enc

def run():
    matrix = 'oxju`L|ONdw^c? ;)VyJg3AP%pc;zX'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
