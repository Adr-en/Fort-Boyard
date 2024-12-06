def upper_case(s):
    if ord("z") >= ord(s) >= ord("a"):
        return chr(ord(s)-32)
