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
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { ClubeService } from '../../../../services/clube-service';

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
    InputIconModule,
    RouterLink
  ],
  templateUrl: './clube-create.html',
  styleUrl: './clube-create.css',
  host: { 'ngSkipHydration': 'true' }
})
export class ClubeCreate implements OnInit{
  isEdicao = false;
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
  private clubeId: number | null = null;

  tiposGestao = [
    { label: 'Associativo', value: 'Associativo' },
    { label: 'SAF', value: 'SAF' },
    { label: 'Privado', value: 'Privado' },
    { label: 'Híbrido', value: 'Híbrido' }
  ];

  constructor(
    private clubeService: ClubeService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.clubeId = Number(id);
      this.isEdicao = true;
    }
    this.carregarEstados();
  }

  carregarDadosClube() {
    if (!this.clubeId) return;
    this.clubeService.getClube(this.clubeId).subscribe({
      next: (dados) => {
        const uf = this.estados.find((estado) => estado.sigla === dados.estado_sigla);
        this.clube = {
          nome_oficial: dados.nome_oficial ?? '',
          nome: dados.nome ?? '',
          sigla: dados.sigla ?? '',
          gestao: dados.gestao ?? 'Associativo',
          fundacao: dados.fundacao ?? '',
          codigo_ibge_municipio: dados.codigo_ibge_municipio ?? null,
          estadio: dados.estadio ?? '',
          cor_principal: dados.cor_principal ?? '',
          cor_secundaria: dados.cor_secundaria ?? '',
          cor_terciaria: dados.cor_terciaria ?? '',
          website: dados.website ?? '',
          escudo: dados.escudo ?? '',
          ativo: dados.ativo ?? true,
          descricao: dados.descricao ?? ''
        };
        if (uf) {
          this.estadoSelecionado = uf.id;
          this.carregandoMunicipios = true;
          this.clubeService.getMunicipios(uf.id).pipe(
            finalize(() => this.carregandoMunicipios = false)
          ).subscribe({
            next: (municipios) => {
              this.municipios = municipios;
              this.municipioSelecionado = municipios.find(
                (municipio: Municipio) => municipio.id === dados.codigo_ibge_municipio
              ) ?? null;
            },
            error: (err) => console.error('Erro ao carregar municípios:', err)
          });
        }
      },
      error: (err) => {
        console.error('Erro ao carregar clube:', err);
        alert('Não foi possível carregar os dados do clube.');
      }
    });
  }

  carregarEstados() {
    this.clubeService.getEstados().subscribe({
      next: (data) => {
        // Ordena por nome do estado
        this.estados = data.sort((a, b) => a.nome.localeCompare(b.nome));
        if (this.clubeId) this.carregarDadosClube();
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

    const requisicao = this.isEdicao && this.clubeId
      ? this.clubeService.atualizarClube(this.clubeId, payload)
      : this.clubeService.cadastrarClube(payload);
    requisicao.subscribe({
      next: (resposta) => {
        alert(`Clube "${resposta.nome}" ${this.isEdicao ? 'atualizado' : 'cadastrado'} com sucesso!`);
        this.router.navigate(['/clubes']);
      },
      error: (err) => {
        console.error('Erro ao salvar clube:', err);
        const detalhe = Array.isArray(err.error?.detail)
          ? err.error.detail.map((item: any) => `${item.loc?.join('.')}: ${item.msg}`).join('\n')
          : err.error?.detail;
        alert(detalhe || `Erro ao ${this.isEdicao ? 'atualizar' : 'cadastrar'} clube. Verifique os dados.`);
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
