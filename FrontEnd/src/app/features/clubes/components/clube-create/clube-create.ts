import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { finalize } from 'rxjs';
import { InputTextModule } from 'primeng/inputtext';
import { AutoCompleteModule } from 'primeng/autocomplete';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { DatePickerModule } from 'primeng/datepicker';
import { FloatLabelModule } from 'primeng/floatlabel';

import { IconFieldModule } from 'primeng/iconfield';
import { InputIconModule } from 'primeng/inputicon';
import { ClubeService } from './clube-service';

interface Municipio {
  id: number;
  nome: string;
}


@Component({
  selector: 'app-clube-create',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    InputTextModule,
    AutoCompleteModule,
    ButtonModule,
    CardModule,
    DatePickerModule,
    FloatLabelModule,
    IconFieldModule,
    InputIconModule
  ],
  templateUrl: './clube-create.html',
  styleUrl: './clube-create.css',
  host: { 'ngSkipHydration': 'true' }
})
export class ClubeCreate implements OnInit{
  clube = {
    nome_oficial: '',
    nome: '',
    sigla: '',
    gestao: 'Associativo',
    fundacao: '',
    codigo_ibge_municipio: null as number | null,
    estadio: '',
    cor_principal: '',
    cor_secundaria: '',
    cor_terciaria: '',
    website: '',
    escudo: '',
    ativo: true,
    descricao: '',
  };

  estados: any[] = [];
  municipios: Municipio[] = [];
  municipiosFiltrados: Municipio[] = [];
  municipioSelecionado: Municipio | string | null = null;
  consultaMunicipio = '';
  carregandoMunicipios = false;
  estadoSelecionado: number | null = null;

  tiposGestao = [
    { label: 'Associativo', value: 'Associativo' },
    { label: 'SAF', value: 'SAF' },
    { label: 'Privado', value: 'Privado' },
    { label: 'Híbrido', value: 'Híbrido' }
  ];

  constructor(private clubeService: ClubeService) {}

  ngOnInit() {
    this.carregarEstados();
  }

  carregarEstados() {
    this.clubeService.getEstados().subscribe({
      next: (data) => {
        // Ordena por nome do estado
        this.estados = data.sort((a, b) => a.nome.localeCompare(b.nome));
      },
      error: (err) => console.error('Erro ao carregar estados:', err)
    });
  }

  onEstadoChange(ufId: number | null) {
    this.clube.codigo_ibge_municipio = null;
    this.municipioSelecionado = null;
    this.consultaMunicipio = '';
    this.municipios = [];
    this.municipiosFiltrados = [];
    if (!ufId) {
      this.carregandoMunicipios = false;
      return;
    }
    this.carregandoMunicipios = true;
    this.clubeService.getMunicipios(ufId).pipe(
      finalize(() => this.carregandoMunicipios = false)
    ).subscribe({
      next: (data) => {
        this.municipios = data.sort((a, b) => a.nome.localeCompare(b.nome));
        this.filtrarMunicipios(this.consultaMunicipio);
      },
      error: (err) => console.error('Erro ao carregar municípios:', err)
    });
  }

  filtrarMunicipios(consulta: string) {
    this.consultaMunicipio = consulta;
    const termo = this.normalizarTexto(consulta.trim());
    if (termo.length < 2) {
      this.municipiosFiltrados = [];
      return;
    }

    this.municipiosFiltrados = this.municipios
      .filter((municipio) => this.normalizarTexto(municipio.nome).includes(termo))
      .slice(0, 20);
  }

  atualizarMunicipioSelecionado(valor: Municipio | string | null) {
    this.municipioSelecionado = valor;
    this.clube.codigo_ibge_municipio =
      typeof valor === 'object' && valor !== null ? valor.id : null;
  }

  private normalizarTexto(valor: string): string {
    return valor.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase();
  }

  salvar() {
    const payload = {
      ...this.clube,
      fundacao: this.clube.fundacao || null,
      estadio: this.clube.estadio.trim() || null,
      cor_principal: this.clube.cor_principal.trim() || null,
      cor_secundaria: this.clube.cor_secundaria.trim() || null,
      cor_terciaria: this.clube.cor_terciaria.trim() || null,
      website: this.clube.website.trim() || null,
      escudo: this.clube.escudo.trim() || null,
      descricao: this.clube.descricao.trim() || null
    };

    this.clubeService.cadastrarClube(payload).subscribe({
      next: (resposta) => {
        alert(`Clube "${resposta.nome}" cadastrado com sucesso!`);
        this.limpar();
      },
      error: (err) => {
        console.error('Erro ao salvar clube:', err);
        const detalhe = Array.isArray(err.error?.detail)
          ? err.error.detail.map((item: any) => `${item.loc?.join('.')}: ${item.msg}`).join('\n')
          : err.error?.detail;
        alert(detalhe || 'Erro ao cadastrar clube. Verifique os dados.');
      }
    });
  }

  limpar() {
    this.clube = {
      nome_oficial: '',
      nome: '',
      sigla: '',
      gestao: 'Associativo',
      fundacao: '',
      codigo_ibge_municipio: null,
      estadio: '',
      cor_principal: '',
      cor_secundaria: '',
      cor_terciaria: '',
      website: '',
      escudo: '',
      ativo: true,
      descricao: '',
    };
    this.estadoSelecionado = null;
    this.municipios = [];
    this.municipiosFiltrados = [];
    this.municipioSelecionado = null;
    this.consultaMunicipio = '';
    this.carregandoMunicipios = false;
  }
}
