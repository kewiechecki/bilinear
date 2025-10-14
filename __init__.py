"""
Bilinear models package for sparse autoencoders and language modeling.

This package provides implementations of bilinear models and sparse autoencoders
for various applications including language modeling, image processing, and toy models.

Submodules:
- language: Language model transformers and utilities
- sae: Sparse autoencoder implementations and tools
- toy: Simplified toy models for testing and experimentation
- image: Image processing models
- shared: Shared components used across different model types
"""

# Import submodules to make them available at package level
from . import language
from . import sae
from . import toy
from . import shared
from . import image

__all__ = ['language', 'sae', 'toy', 'shared', 'image']