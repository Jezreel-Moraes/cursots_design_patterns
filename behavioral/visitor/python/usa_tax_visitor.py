from product_protocol import VisitableProductProtocol


class USATaxVisitor:
   FOOD_TAXES:       float = 15 / 100
   VEHICLE_TAXES:    float = 20 / 100
   MEDICINE_TAXES:   float = 46 / 100
   
   
   @staticmethod   
   def calculate_taxes_for_vehicle(o: VisitableProductProtocol) -> float:
      return o.get_price() * (1 + USATaxVisitor.VEHICLE_TAXES)
   
   @staticmethod
   def calculate_taxes_for_food(o: VisitableProductProtocol) -> float:
      return o.get_price() * (1 + USATaxVisitor.FOOD_TAXES)
      
   @staticmethod
   def calculate_taxes_for_medicine(o: VisitableProductProtocol) -> float:
      return o.get_price() * (1 + USATaxVisitor.MEDICINE_TAXES)