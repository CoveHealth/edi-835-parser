from edi_parser.common.elements.identifier import Identifier
from edi_parser.common.segments.utilities import split_segment, get_element

from edi_parser.claims_parser.elements.claim_freqeuncy_code import ClaimFrequencyCode
from edi_parser.claims_parser.elements.facility_code import FacilityCode
from edi_parser.claims_parser.elements.facility_code_qualifier import FacilityCodeQualifier


class Claim:
	identification = 'CLM'

	identifier = Identifier()
	facility_code = FacilityCode()
	facility_code_qualifier = FacilityCodeQualifier()
	claim_freq_code = ClaimFrequencyCode()

	def __init__(self, segment: str):
		self.index = segment.split(':', 1)[0]
		segment = segment.split(':', 1)[1]
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.submit_id = segment[1]
		self.monetary_amt = get_element(segment, 2)
		self.facility_code = get_element(segment, 5)
		self.facility_code_qualifier = get_element(segment, 5)
		self.claim_freq_code = get_element(segment, 5)
		self.status = get_element(segment, 17)

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
