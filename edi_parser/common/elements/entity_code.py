from edi_835_parser.elements import Element

# https://ediacademy.com/blog/x12-n101-entity-identifier-codes/
entity_codes = {
	'QC': 'patient',
	'74': 'insured',
	'82': 'rendering provider',
	'85': 'billing provider',
	'IL': 'insured or subscriber',
	'41': 'submitter',
	'40': 'receiver',
	'87': 'pay-to-provider',
	'PE': 'payee',
	'PR': 'payer',
	'77': 'service location',
	'DQ': 'supervising physician',
	'PW': 'pickup address'
}


class EntityCode(Element):

	def parser(self, value: str) -> str:
		return entity_codes.get(value, value)
