from edi_835_parser.elements import Element
from edi_835_parser.elements.utilities import split_element


class FacilityCode(Element):

	def parser(self, value: str) -> str:
		if value is not None:
			value = split_element(value)
			code, *_ = value
			return code
