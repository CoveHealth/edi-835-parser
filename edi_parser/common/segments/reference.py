from edi_parser.common.elements.identifier import Identifier
from edi_parser.common.elements.reference_qualifier import ReferenceQualifier
from edi_parser.common.segments.utilities import split_segment


class Reference:
	identification = 'REF'

	identifier = Identifier()
	qualifier = ReferenceQualifier()

	def __init__(self, segment: str):
		self.index = segment.split(':', 1)[0]
		segment = segment.split(':', 1)[1]

		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.qualifier = segment[1]
		self.qualifier_code = segment[1]
		self.value = segment[2]

	def __repr__(self) -> str:
		return '\n'.join(str(item) for item in self.__dict__.items())

	def __str__(self) -> str:
		return f'{self.qualifier}: {self.value}'


if __name__ == '__main__':
	pass
