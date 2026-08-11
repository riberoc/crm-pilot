import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 923) - 912
    _mask = _data(75, None)
    _enc = 64
    return _mask, _enc

def run():
    matrix = ' WjfddO}TaQxM$dcO^75Qc:ku`y/MO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
