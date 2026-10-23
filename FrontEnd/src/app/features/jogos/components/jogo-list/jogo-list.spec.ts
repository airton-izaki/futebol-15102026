import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JogoList } from './jogo-list';

describe('JogoList', () => {
  let component: JogoList;
  let fixture: ComponentFixture<JogoList>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [JogoList],
    }).compileComponents();

    fixture = TestBed.createComponent(JogoList);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
