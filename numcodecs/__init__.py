# ruff: noqa: E402
"""Numcodecs is a Python package providing buffer compression and
transformation codecs for use in data storage and communication
applications. These include:

* Compression codecs, e.g., Zlib, BZ2, LZMA, ZFPY and Blosc.
* Pre-compression filters, e.g., Delta, Quantize, FixedScaleOffset,
  PackBits, Categorize.
* Integrity checks, e.g., CRC32, Adler32.

All codecs implement the same API, allowing codecs to be organized into
pipelines in a variety of ways.

If you have a question, find a bug, would like to make a suggestion or
contribute code, please `raise an issue on GitHub
<https://github.com/zarr-developers/numcodecs/issues>`_.

"""

import atexit
import multiprocessing
from contextlib import suppress

from numcodecs.registry import get_codec as get_codec
from numcodecs.registry import register_codec
from numcodecs.version import version as __version__  # noqa: F401
from numcodecs.zlib import Zlib

register_codec(Zlib)

from numcodecs.gzip import GZip

register_codec(GZip)

from numcodecs.bz2 import BZ2

register_codec(BZ2)

with suppress(ImportError):
    from numcodecs.lzma import LZMA

    register_codec(LZMA)

with suppress(ImportError):
    from numcodecs import blosc
    from numcodecs.blosc import Blosc

    register_codec(Blosc)
    # initialize blosc
    try:
        ncores = multiprocessing.cpu_count()
    except OSError:  # pragma: no cover
        ncores = 1
    blosc.init()
    blosc.set_nthreads(min(8, ncores))
    atexit.register(blosc.destroy)

with suppress(ImportError):
    from numcodecs import zstd as zstd
    from numcodecs.zstd import Zstd

    register_codec(Zstd)

with suppress(ImportError):
    from numcodecs import lz4 as lz4
    from numcodecs.lz4 import LZ4

    register_codec(LZ4)

with suppress(ImportError):
    from numcodecs.zfpy import ZFPY

    register_codec(ZFPY)

from numcodecs.astype import AsType

register_codec(AsType)

from numcodecs.delta import Delta

register_codec(Delta)

from numcodecs.quantize import Quantize

register_codec(Quantize)

from numcodecs.fixedscaleoffset import FixedScaleOffset

register_codec(FixedScaleOffset)

from numcodecs.packbits import PackBits

register_codec(PackBits)

from numcodecs.categorize import Categorize

register_codec(Categorize)

from numcodecs.pickles import Pickle

register_codec(Pickle)

from numcodecs.base64 import Base64

register_codec(Base64)

from numcodecs.shuffle import Shuffle

register_codec(Shuffle)

from numcodecs.bitround import BitRound

register_codec(BitRound)

with suppress(ImportError):
    from numcodecs.msgpacks import MsgPack

    register_codec(MsgPack)

from numcodecs.checksum32 import CRC32, CRC32C, Adler32, JenkinsLookup3

register_codec(CRC32)
register_codec(CRC32C)
register_codec(Adler32)
register_codec(JenkinsLookup3)

from numcodecs.json import JSON

register_codec(JSON)

with suppress(ImportError):
    from numcodecs import vlen as vlen
    from numcodecs.vlen import VLenArray, VLenBytes, VLenUTF8

    register_codec(VLenUTF8)
    register_codec(VLenBytes)
    register_codec(VLenArray)

from numcodecs.fletcher32 import Fletcher32

register_codec(Fletcher32)

from numcodecs.pcodec import PCodec

register_codec(PCodec)
