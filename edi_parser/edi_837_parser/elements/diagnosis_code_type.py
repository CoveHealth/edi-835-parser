from edi_835_parser.elements import Element
from edi_835_parser.elements.utilities import split_element


class DiagnosisCodeType(Element):

	def parser(self, value: str) -> str:
		if value is not None:
			value = split_element(value)
			code_type, *_ = value
			return code_type
