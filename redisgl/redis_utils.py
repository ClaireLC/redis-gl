from typing import Optional, Tuple, Union
import numpy as np
import msgpack_numpy as m
m.patch()


def decode_matlab(s: Union[str, bytes]) -> np.ndarray:
    """Decodes a matrix encoded as a string in matlab format."""
    if isinstance(s, bytes):
        s = s.decode("utf8")
    s = s.strip()
    tokens = [list(map(float, row.strip().split())) for row in s.split(";")]
    return np.array(tokens).squeeze()


def encode_matlab(A: np.ndarray) -> str:
    """Encodes a matrix to a string in matlab format."""
    if len(A.shape) == 1:
        return " ".join(map(str, A.tolist()))
    return "; ".join(" ".join(map(str, row)) for row in A.tolist())

def encode_image(img):
    img_bin = m.packb(img)
    return img_bin

def decode_image(img_bin):
    img = m.unpackb(img_bin)
    return img
