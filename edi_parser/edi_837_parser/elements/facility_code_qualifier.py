from edi_835_parser.elements import Element
from edi_835_parser.elements.utilities import split_element


class FacilityCodeQualifier(Element):

	def parser(self, value: str) -> str:
		if value is not None:
			value = split_element(value)
			if len(value) > 1:
				_, qualifier, *_ = value
				return qualifier
