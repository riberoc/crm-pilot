import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 793) - 539
    _mask = _data(443, None)
    _enc = 143
    return _mask, _enc

def run():
    matrix = '7V7Ejl[3 Vk67bf/|c8*wL#Kbfc^rm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
