import { VisitableProductProtocol } from './VisitableProductProtocol';
import { VisitorProtocol } from './VisitorProtocol';

export abstract class AbstractVisitor implements VisitorProtocol {
  protected foodTax = 0;
  protected vehicleTax = 0;
  protected medicineTax = 0;

  taxesForFoods(food: VisitableProductProtocol): number {
    return food.price * (1 + this.foodTax);
  }
  taxesForVehicles(vehicle: VisitableProductProtocol): number {
    return vehicle.price * (1 + this.vehicleTax);
  }
  taxesForMedicines(medicine: VisitableProductProtocol): number {
    return medicine.price * (1 + this.medicineTax);
  }
}
