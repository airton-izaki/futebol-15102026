import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClubeList } from './clube-list';

describe('ClubeList', () => {
  let component: ClubeList;
  let fixture: ComponentFixture<ClubeList>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ClubeList],
    }).compileComponents();

    fixture = TestBed.createComponent(ClubeList);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
