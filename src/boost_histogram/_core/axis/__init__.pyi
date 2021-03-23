from typing import Any, Iterable, Iterator, Tuple, TypeVar

import numpy as np
from numpy.typing import ArrayLike

from . import transform

T = TypeVar("T", bound="_BaseAxis")

class _BaseAxis:
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __imul__(self: T, other: float) -> T: ...
    def __repr__(self) -> str: ...
    def __copy__(self: T) -> T: ...
    def __deepcopy__(self: T, memo: Any) -> T: ...
    def _ipython_key_completions_(self) -> Tuple[str, ...]: ...
    @property
    def traits_underflow(self) -> bool: ...
    @property
    def traits_overflow(self) -> bool: ...
    @property
    def traits_circular(self) -> bool: ...
    @property
    def traits_growth(self) -> bool: ...
    @property
    def traits_continuous(self) -> bool: ...
    @property
    def traits_ordered(self) -> bool: ...
    @property
    def metadata(self) -> Any: ...
    @property
    def size(self) -> int: ...
    @property
    def extent(self) -> int: ...
    @property
    def edges(self) -> np.ndarray: ...
    @property
    def centers(self) -> np.ndarray: ...
    @property
    def widths(self) -> np.ndarray: ...
    def index(self, arg0: ArrayLike) -> int | np.ndarray: ...
    def value(self, arg0: ArrayLike) -> float | np.ndarray: ...

class _BaseRegular(_BaseAxis):
    def __init__(self, bins: int, start: float, stop: float) -> None: ...
    def __iter__(self) -> Iterator[tuple[float, float]]: ...
    def bin(self, arg0: int) -> tuple[float, float]: ...

class regular_none(_BaseRegular): ...
class regular_uflow(_BaseRegular): ...
class regular_oflow(_BaseRegular): ...
class regular_uoflow(_BaseRegular): ...
class regular_uoflow_growth(_BaseRegular): ...
class regular_circular(_BaseRegular): ...
class regular_numpy(_BaseRegular): ...

class regular_pow(_BaseRegular):
    def __init__(self, bins: int, start: float, stop: float, power: float) -> None: ...
    @property
    def transform(self) -> transform.pow: ...

class regular_trans(_BaseRegular):
    def __init__(
        self, bins: int, start: float, stop: float, transform: transform._BaseTransform
    ) -> None: ...
    @property
    def transform(self) -> transform._BaseTransform: ...

class _BaseVariable(_BaseAxis):
    def __init__(self, edges: Iterable[float]) -> None: ...
    def __iter__(self) -> Iterator[tuple[float, float]]: ...
    def bin(self, arg0: int) -> tuple[float, float]: ...

class variable_none(_BaseVariable): ...
class variable_uflow(_BaseVariable): ...
class variable_oflow(_BaseVariable): ...
class variable_uoflow(_BaseVariable): ...
class variable_uoflow_growth(_BaseVariable): ...
class variable_circular(_BaseVariable): ...

class _BaseInteger(_BaseAxis):
    def __init__(self, start: int, stop: int) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def bin(self, arg0: int) -> int: ...

class integer_none(_BaseInteger): ...
class integer_uflow(_BaseInteger): ...
class integer_oflow(_BaseInteger): ...
class integer_uoflow(_BaseInteger): ...
class integer_growth(_BaseInteger): ...
class integer_circular(_BaseInteger): ...

class _BaseCatInt(_BaseAxis):
    def __init__(self, categories: Iterable[int]) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def bin(self, arg0: int) -> int: ...

class category_int(_BaseCatInt): ...
class category_int_growth(_BaseCatInt): ...

class _BaseCatStr(_BaseAxis):
    def __init__(self, categories: Iterable[str]) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def bin(self, arg0: int) -> str: ...

class category_str(_BaseCatStr): ...
class category_str_growth(_BaseCatStr): ...

class boolean(_BaseAxis):
    def __iter__(self) -> Iterator[int]: ...
    def bin(self, arg0: int) -> int: ...
