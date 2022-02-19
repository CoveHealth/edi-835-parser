from edi_835_parser.elements.identifier import Identifier
from edi_835_parser.segments.utilities import split_segment, get_element


class Subscriber:
	identification = 'SBR'

	identifier = Identifier()

	def __init__(self, segment: str):
		self.index = segment.split(':', 1)[0]
		segment = segment.split(':', 1)[1]
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.payer_resp_seq_code = segment[1]
		self.individual_relationship_code = get_element(segment, 2)
		self.ref_id = get_element(segment, 3)
		self.name = get_element(segment, 4)
		self.insurance_type = get_element(segment, 5)
		self.coordination_of_benefit = get_element(segment, 6)
		self.response = get_element(segment, 7)
		self.employment_status = get_element(segment, 8)
		self.claim_filing_indicator = get_element(segment, 9)

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
