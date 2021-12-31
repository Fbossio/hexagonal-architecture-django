from typing import Callable, Dict, List, Type, TypeVar

from myapp.eventlib.event import Event

T_contra = TypeVar('T_contra', bound=Event, covariant=True)
EventHandlerBaseType = Callable[[T_contra], None]
EventHandlersCollectionType = Dict[Type[Event], List[EventHandlerBaseType]]


class EventDispatcher:
    _handlers: EventHandlersCollectionType = {}

    def register_handler(
        self,
        event_type: Type[T_contra],
        event_handler: Callable[[T_contra], None]
    ):
        self._handlers.setdefault(event_type, list())
        self._handlers[event_type].append(event_handler)

    def dispatch(self, event: Event):
        event_handlers = self._handlers.get(type(event), list())
        for event_handler in event_handlers:
            event_handler(event)

    @property
    def handlers(self) -> EventHandlersCollectionType:
        return self._handlers
