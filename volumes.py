import numpy as np

class Volume(object):

    def __getitem__(self, slices):
        """
        Asumes x,y,z coordinates
        """
        raise NotImplemented

    @property
    def shape(self):
        """
        Asumes x,y,z coordinates
        """
        return self._shape

    @property
    def data_type(self):
        """
        Data type of the voxels in this volume
        """

        return self._data_type
    

    @property
    def layer_type(self):
        """
        Either segmentation or image
        """
        return self._layer_type

    @property
    def mesh(self):
        """
        Return True if mesh is desired
        """
        return self._mesh

    @property
    def resolution(self):
        """
        Size of voxels in nanometers
        """
        return self._resolution

    @property
    def underlying(self):
        """
        Size of the underlying chunks
        """
        return self._underlying

    @property
    def num_channels(self):
        if len(self.shape) == 3:
            return 1
        elif len(self.shape) == 4:
            return self.shape[0]
        else:
            raise Exception('Wrong shape')  
    
class HDF5Volume(Volume):

    def __init__(self, path):
        import h5py
        self._f = h5py.File(path)
        self._data = np.swapaxes(self._f['main'],0,2)
        self._layer_type = 'segmentation'
        self._mesh = True
        self._resolution = [6,6,30]
        self._underlying = self.shape
        self._data_type = self._f['main'].dtype

    @property
    def shape(self):
        return self._data.shape


    def __getitem__(self, slices):
        """
        Asumes x,y,z coordinates
        """
        return self._data.__getitem__(slices)

    def __del__(self):
        self._f.close()

class FakeVolume(Volume):

    def __init__(self):
        arr = np.ones(shape=(127,127,127),dtype=np.uint32)
        self._data = np.pad(arr, 1, 'constant')
        self._layer_type = 'segmentation'
        self._mesh = True
        self._resolution = [6,6,30]
        self._underlying = self.shape
        self._data_type = self._data.dtype

    @property
    def shape(self):
        return self._data.shape


    def __getitem__(self, slices):
        """
        Asumes x,y,z coordinates
        """
        return self._data.__getitem__(slices)
