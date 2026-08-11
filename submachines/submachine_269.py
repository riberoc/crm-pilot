import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 279) - 305
    _mask = _data(248, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = 'XCuLj20S3&zGPaAYlj_lpJAU/u cUv'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
