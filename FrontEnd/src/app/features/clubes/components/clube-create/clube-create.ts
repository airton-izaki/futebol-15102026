import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { DatePickerModule } from 'primeng/datepicker';
import { FloatLabelModule } from 'primeng/floatlabel';
import { IconFieldModule } from 'primeng/iconfield';
import { InputIconModule } from 'primeng/inputicon';

@Component({
  selector: 'app-clube-create',
  imports: [
    FormsModule,
    InputTextModule,
    ButtonModule,
    CardModule,
    DatePickerModule,
    FloatLabelModule,

    IconFieldModule,
    InputIconModule
  ],
  templateUrl: './clube-create.html',
  styleUrl: './clube-create.css',
})
export class ClubeCreate {
  clube = {
    nomeOficial: '',
    nomePopular: '',
    sigla: '',
    dataFundacao: null as Date | null
  };

  salvar() {
    console.log('Dados enviados:', this.clube);
    alert(`Clube "${this.clube.nomePopular || this.clube.nomeOficial}" salvo com sucesso!`);
  }

  limpar() {
    this.clube = {
      nomeOficial: '',
      nomePopular: '',
      sigla: '',
      dataFundacao: null
    };
  }
}
