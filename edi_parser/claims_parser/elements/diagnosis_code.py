from edi_parser.common.elements import Element
from edi_parser.common.elements.utilities import split_element


class DiagnosisCode(Element):

	def parser(self, value: str) -> str:
		if value is not None:
			value = split_element(value)
			if len(value) > 1:
				return value[1]
