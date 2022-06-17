from tax_visitor_protocol import TaxVisitor
from product_protocol import VisitableProductProtocol


class Medicine(VisitableProductProtocol):

   def get_price_with_taxes(self, visitor: TaxVisitor) -> float:
      return visitor.calculate_taxes_for_medicine(self)