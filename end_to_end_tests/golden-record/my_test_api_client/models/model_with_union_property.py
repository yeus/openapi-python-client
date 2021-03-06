from typing import Any, Dict, Union

import attr

from ..models.an_enum import AnEnum
from ..models.an_int_enum import AnIntEnum
from ..types import UNSET, Unset


@attr.s(auto_attribs=True)
class ModelWithUnionProperty:
    """  """

    a_property: Union[Unset, AnEnum, AnIntEnum] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        a_property: Union[Unset, AnEnum, AnIntEnum]
        if isinstance(self.a_property, Unset):
            a_property = UNSET
        elif isinstance(self.a_property, AnEnum):
            a_property = UNSET
            if not isinstance(self.a_property, Unset):
                a_property = self.a_property

        else:
            a_property = UNSET
            if not isinstance(self.a_property, Unset):
                a_property = self.a_property

        field_dict = {}
        if a_property is not UNSET:
            field_dict["a_property"] = a_property

        return field_dict

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ModelWithUnionProperty":
        def _parse_a_property(data: Any) -> Union[Unset, AnEnum, AnIntEnum]:
            data = None if isinstance(data, Unset) else data
            a_property: Union[Unset, AnEnum, AnIntEnum]
            try:
                a_property = UNSET
                if data is not None:
                    a_property = AnEnum(data)

                return a_property
            except:  # noqa: E722
                pass
            a_property = UNSET
            if data is not None:
                a_property = AnIntEnum(data)

            return a_property

        a_property = _parse_a_property(d.get("a_property", UNSET))

        return ModelWithUnionProperty(
            a_property=a_property,
        )
