from edi_parser.common.elements import Element

contact_function_codes = {
    'CX': 'payers_claim_office',
    'IC': 'information_contact',
    'BL': 'technical_contact'
}


class ContactFunctionCode(Element):

    def parser(self, value: str) -> str:
        return contact_function_codes.get(value, value)
