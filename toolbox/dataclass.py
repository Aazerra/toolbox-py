from dataclasses import dataclass, field, fields, make_dataclass
from typing import List, Dict, Any, Callable, Optional, Type, Union, get_args, get_origin, TypeVar


T = TypeVar("T", bound="SerializableDataclass")


@dataclass
class SerializableDataclass:
    """Base class for serialization with alias support."""

    """
        Alias for fields. It's a dictionary that contains the field name as the key and the alias as the value.
    """
    _aliases: Dict[str, str] = field(
        default_factory=dict, init=False, repr=False)

    """
        It's a dictionary that contains the field name as the key and a function as the value.
        We can pass a function per each field to process the data before adding it to the object.
        It's only used in `from_dict` method.
    """
    _pre_processors: Dict[str, Callable] = field(
        default_factory=dict, init=False, repr=False)

    """
        If a provider is returning redundant information which we don't need to store in our object, we can pass them
        as an array of keys.
    """
    _exclude: List[str] = field(default_factory=list, init=False, repr=False)

    """Not used for now"""
    extra_data: Dict[str, Any] = field(
        default_factory=dict, init=False, repr=False)

    @classmethod
    def from_dict(
            cls: Type[T],
            data: Dict[str, Any],
            exclude: Optional[List[str]] = None,
            include_extra: bool = False,
            extra_data_cls: Optional[Type] = None
    ) -> T:
        """Create an instance from a dictionary, using aliases or field names."""
        init_data = {}
        consumed_keys = set()  # Track keys that are used to initialize declared fields
        alias_map = getattr(cls, "_aliases", {})  # Reverse alias mapping

        internal_fields = {"_aliases", "_pre_processors",
                           "_exclude", "missing_keys"}
        for field_obj in fields(cls):
            field_name = field_obj.name
            if field_name in internal_fields:
                continue  # Skip internal fields

            # Use alias or field name
            alias_name = alias_map.get(field_name, field_name)
            if alias_name not in data:
                continue

            consumed_keys.add(alias_name)

            # Process data if pre-processor exists
            pre_processors = getattr(cls, "_pre_processors", {})
            if field_name in pre_processors.keys():
                init_data[field_name] = cls._pre_processors[field_name](
                    data[alias_name])
            else:
                # TODO: Refactor this section ( its a little bit messy and its hard to understand )
                if get_origin(field_obj.type) is Union:
                    args = get_args(field_obj.type)
                    non_none_types = [arg for arg in args if arg is not type(None)]
                    if all(isinstance(arg, type) and issubclass(arg, SerializableDataclass) for arg in non_none_types) and data[alias_name] is not None:
                        field_type = get_args(field_obj.type)[0]
                        init_data[field_name] = field_type.from_dict(data[alias_name])
                    else:
                        init_data[field_name] = data[alias_name]
                elif get_origin(field_obj.type) in (list, List):
                    item_type = get_args(field_obj.type)[0]
                    if isinstance(item_type, type) and issubclass(item_type, SerializableDataclass):
                        init_data[field_name] = [item_type.from_dict(item) for item in data[alias_name]]
                    else:
                        init_data[field_name] = data[alias_name]
                elif issubclass(field_obj.type, SerializableDataclass):
                    init_data[field_name] = field_obj.type.from_dict(data[alias_name])
                else:
                    init_data[field_name] = data[alias_name]

        instance = cls(**init_data)
        if exclude is not None:
            instance._exclude = exclude
        if include_extra:
            extra_keys = {key: value for key,
                          value in data.items() if key not in consumed_keys}
            if extra_data_cls is None:
                # Dynamically create a dataclass if one is not provided
                extra_data_cls = make_dataclass(
                    "ExtraData", [(k, type(v), field(default=v)) for k, v in extra_keys.items()])

            instance.extra_data = extra_data_cls(**extra_keys)

        return instance

    def to_dict(self) -> Dict[str, Any]:
        """Convert instance to dictionary, using aliases or field names."""
        result = {}
        for field_obj in fields(self):
            field_name = field_obj.name
            if field_name in ["_aliases", "_pre_processors", "_exclude"]:
                continue
            if field_name == "extra_data" and not getattr(self, field_name):
                continue
            if self._exclude is not None and field_name in self._exclude:
                continue
            data = getattr(self, field_name)
            if isinstance(data, SerializableDataclass):
                data = data.to_dict()
            elif isinstance(data, list):
                data = [
                    item.to_dict() if isinstance(item, SerializableDataclass) else item
                    for item in data
                ]

            result[field_name] = data
        return result
