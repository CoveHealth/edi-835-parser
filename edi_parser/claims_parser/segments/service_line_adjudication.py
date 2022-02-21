from edi_parser.common.elements.identifier import Identifier
from edi_parser.common.segments.utilities import split_segment, get_element


class ServiceLineAdjudication:
	identification = 'SVD'

	identifier = Identifier()

	def __init__(self, segment: str):
		self.index = segment.split(':', 1)[0]
		segment = segment.split(':', 1)[1]
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.other_payer_id = segment[1]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
