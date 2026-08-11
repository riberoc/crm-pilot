import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 483) - 788
    _mask = _data(546, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = 'NK0sYt@_$ Jx3jTPez:HuAI#nA&=!h'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
