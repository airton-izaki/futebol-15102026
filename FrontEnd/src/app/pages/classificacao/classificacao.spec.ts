import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Classificacao } from './classificacao';

describe('Classificacao', () => {
  let component: Classificacao;
  let fixture: ComponentFixture<Classificacao>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Classificacao],
    }).compileComponents();

    fixture = TestBed.createComponent(Classificacao);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
