"""Top-level package for torchio."""

__author__ = """Fernando Perez-Garcia"""
__email__ = 'fernando.perezgarcia.17@ucl.ac.uk'
<<<<<<< HEAD
__version__ = '0.18.42'
=======
__version__ = '0.18.45'
>>>>>>> a0b73a93490ed9f61aad2c2fa43ab7a75d94ba14


from . import utils
from .constants import *  # noqa: F401, F403
from .transforms import *  # noqa: F401, F403
from .data import (
    io,
    sampler,
    inference,
    SubjectsDataset,
    Image,
    ScalarImage,
    LabelMap,
    Queue,
    Subject,
    WeightedSampler,
    UniformSampler,
    LabelSampler,
    GridSampler,
    GridAggregator,
)
from . import datasets
from . import reference


__all__ = [
    'utils',
    'io',
    'sampler',
    'inference',
    'SubjectsDataset',
    'Image',
    'ScalarImage',
    'LabelMap',
    'Queue',
    'Subject',
    'datasets',
    'reference',
    'WeightedSampler',
    'UniformSampler',
    'LabelSampler',
    'GridSampler',
    'GridAggregator',
]
