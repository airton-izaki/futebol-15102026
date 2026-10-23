import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClubeCreate } from './clube-create';

describe('ClubeCreate', () => {
  let component: ClubeCreate;
  let fixture: ComponentFixture<ClubeCreate>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ClubeCreate],
    }).compileComponents();

    fixture = TestBed.createComponent(ClubeCreate);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
