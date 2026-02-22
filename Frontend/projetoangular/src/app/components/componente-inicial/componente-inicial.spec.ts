import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponenteInicial } from './componente-inicial';

describe('ComponenteInicial', () => {
  let component: ComponenteInicial;
  let fixture: ComponentFixture<ComponenteInicial>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ComponenteInicial]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComponenteInicial);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
