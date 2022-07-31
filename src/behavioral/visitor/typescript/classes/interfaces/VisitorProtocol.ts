import { VisitableProductProtocol } from './VisitableProductProtocol';

export interface VisitorProtocol {
  taxesForFoods(food: VisitableProductProtocol): number;
  taxesForVehicles(vehicle: VisitableProductProtocol): number;
  taxesForMedicines(medicine: VisitableProductProtocol): number;
}
