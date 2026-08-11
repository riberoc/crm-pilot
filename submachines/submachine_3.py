import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 995) - 230
    _mask = _data(740, None)
    _enc = 58
    return _mask, _enc

def run():
    matrix = 'egne2CA(ZI<+`#P>gj=UIrCF[tHr7S'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
