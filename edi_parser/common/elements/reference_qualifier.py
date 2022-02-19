from edi_835_parser.elements import Element

# https://ushik.ahrq.gov/ViewItemDetails?&system=sdo&itemKey=133213000
reference_qualifiers = {
	'6R': 'provider control number',
	'CE': 'contract code',
	'0K': 'policy form identifying number',
	'PQ': 'payee identification',
	'TJ': 'federal taxpayer identification number',
	'LU': 'location number',
	'OB': 'State License Number',
	'1A': 'Blue Cross Provider Number',
	'1B':  'Blue Shield Provider Number',
	'1C': 'Medicare Provider Number',
	'1D': 'Medicaid Provider Number',
	'1G': 'Provider Number UPIN Number',
	'1H': 'CHAMPUS Identification Number',
	'1J':  'Facility ID Number',
	'D3': 'National Council for Prescription Drug Programs Pharmacy Number',
	'G2': 'Provider Commercial Number',
	'HPI': 'Centers for Medicare and Medicaid Services National Provider Identifier',
	'SY': 'Social Security Number',
	'EI': 'employer identification',
	'2U': 'payer identification',
	'FY': 'claim office number',
	'NF': 'NAIC code',
	'Y4': 'agency claim number',
	'4N': 'Special Payment Reference Number'

}


# class ReferenceQualifier(Element):
#
# 	def parser(self, value: str) -> Code:
# 		description = reference_qualifiers.get(value, None)
# 		return Code(value, description)

class ReferenceQualifier(Element):

	def parser(self, value: str) -> str:
		return reference_qualifiers.get(value, value)
