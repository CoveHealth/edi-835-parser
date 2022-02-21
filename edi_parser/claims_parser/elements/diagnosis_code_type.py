from edi_parser.common.elements import Element
from edi_parser.common.elements.utilities import split_element


class DiagnosisCodeType(Element):

	def parser(self, value: str) -> str:
		if value is not None:
			value = split_element(value)
			code_type, *_ = value
			return code_type
