import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 193) - 118
    _mask = _data(399, None)
    _enc = 217
    return _mask, _enc

def run():
    matrix = '(nRJ`q939JIez<NRk2CwPF!-vk!*LY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
