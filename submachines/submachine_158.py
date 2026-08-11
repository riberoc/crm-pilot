import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 690) - 315
    _mask = _data(892, None)
    _enc = 145
    return _mask, _enc

def run():
    matrix = 'eH )vjL6o@&!YL<]PD*@&[_Ua?.T/V'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
