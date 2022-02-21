from typing import Optional

from edi_parser.common.elements import Element
from edi_parser.common.elements.utilities import split_element


class ServiceModifier1(Element):

	def parser(self, value: str) -> Optional[str]:
		if value is not None:
			value = split_element(value)
			if len(value) > 2:
				return value[2]
