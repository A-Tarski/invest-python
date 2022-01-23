import abc
from typing import Generic, Iterable, TypeVar

TId = TypeVar("TId")
TItem = TypeVar("TItem")


class IItemStorage(Generic[TId, TItem], abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> Iterable[TItem]:
        ...

    @abc.abstractmethod
    def update(self, item_id: TId, new_item: TItem) -> None:
        ...

    @abc.abstractmethod
    def add(self, item: TItem) -> None:
        ...

    @abc.abstractmethod
    def delete(self, item: TId) -> None:
        ...