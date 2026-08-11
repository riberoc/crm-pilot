import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 709) - 512
    _mask = _data(1, None)
    _enc = 220
    return _mask, _enc

def run():
    matrix = '>}bf?~{=@k0Q7l#*eKU%)3i$ .p&pZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
