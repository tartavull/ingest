import zlib
import io
import numpy as np
from PIL import Image

def encode_npz(subvol):
    """
    This file format is unrelated to np.savez
    We are just saving as .npy and the compressing
    using zlib. 
    The .npy format contains metadata indicate
    shape and dtype, in opositon to just doing np.tobytes
    """
    fileobj = io.BytesIO()
    if len(subvol.shape) == 3:
        subvol = np.expand_dims(subvol, 0)
    np.save(fileobj, subvol)
    cdz = zlib.compress(fileobj.getvalue())
    return cdz

def decode_npz(string):
    fileobj = io.BytesIO(zlib.decompress(string))
    return np.load(fileobj)



# encoding test
# import h5py
# with h5py.File('/home/it2/Downloads/0-1024_0-1024_0-100.ml.h5') as f:
#   string  = encode_npz(f['main'][:])
#   with open('/home/it2/Downloads/0-1024_0-1024_0-100.npz','w') as f1:
#     f1.write(string)

#   with open('/home/it2/Downloads/0-1024_0-1024_0-100.npz','r') as f2:
#     vol = decode_npz(f2.read())

#   assert np.all(vol[0,:,:,:] == f['main'][:])


def encode_jpeg(subvol):
    shape = subvol.shape
    reshaped = subvol.reshape(shape[0] * shape[1], shape[2])
    img = Image.fromarray(reshaped)
    f = io.BytesIO()
    img.save(f, "JPEG")
    return f.getvalue()


def encode_raw(subvol):
    return subvol.tostring('C')