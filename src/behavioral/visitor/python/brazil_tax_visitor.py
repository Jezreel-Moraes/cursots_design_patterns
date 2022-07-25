from product_protocol import VisitableProductProtocol


class BrazilTaxVisitor:
   FOOD_TAXES:       float = 20 / 100
   VEHICLE_TAXES:    float = 32 / 100
   MEDICINE_TAXES:   float = 26 / 100
   
   @staticmethod
   def calculate_taxes_for_vehicle(o: VisitableProductProtocol) -> float:
      return o.get_price() * (1 + BrazilTaxVisitor.VEHICLE_TAXES)
   
   @staticmethod
   def calculate_taxes_for_food(o: VisitableProductProtocol) -> float:
      return o.get_price() * (1 + BrazilTaxVisitor.FOOD_TAXES)
   
   @staticmethod   
   def calculate_taxes_for_medicine(o: VisitableProductProtocol) -> float:
      return o.get_price() * (1 + BrazilTaxVisitor.MEDICINE_TAXES)