import { BuilderFacade } from './facade/BuilderFacade';
import { BuilderFacadeProtocol } from './interfaces/BuilderFacadeProtocol';

export class BuilderFacadeDecorator implements BuilderFacadeProtocol {
  private facade = new BuilderFacade();

  private before(): void {
    this.facade.mainDishBuilder.reset();
  }

  makeMealWithTwoBuilders(): void {
    this.before();
    this.facade.makeMealWithTwoBuilders();
    console.log('\n >> Finish makeMealWithTwoBuilders\n');
  }
  makeMealWithoutBuilder(): void {
    this.before();
    this.facade.makeMealWithoutBuilder();
    console.log('\n >> Finish makeMealWithoutBuilder\n');
  }
}
