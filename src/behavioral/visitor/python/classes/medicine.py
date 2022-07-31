from classes.interfaces.product_protocol import VisitableProductProtocol
from classes.interfaces.tax_visitor_protocol import TaxVisitor


class Medicine(VisitableProductProtocol):

    def get_price_with_taxes(self, visitor: TaxVisitor) -> float:
        return visitor.calculate_taxes_for_medicine(self)
