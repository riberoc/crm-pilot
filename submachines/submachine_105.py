import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 784) - 997
    _mask = _data(1898, None)
    _enc = 137
    return _mask, _enc

def run():
    matrix = 'WqDm=XSDF%SEmCNt`n8N%B/#oerW H'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
