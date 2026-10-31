import { Component, Inject, OnInit, PLATFORM_ID } from '@angular/core';
import { CommonModule, isPlatformBrowser } from '@angular/common';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { ClubeService } from '../../../../services/clube-service';
import { TableModule } from 'primeng/table';
import { RouterLink } from '@angular/router';



@Component({
  selector: 'app-clube-list',
  imports: [
    CommonModule,
    ButtonModule,
    CardModule,
    TableModule,
    RouterLink,
    ],
  templateUrl: './clube-list.html',
  styleUrl: './clube-list.css',
})
export class ClubeList implements OnInit {
    clubes: any[] = [];

    constructor(
      private clubeService: ClubeService,
      @Inject(PLATFORM_ID) private platformId: object
    ) {}

    ngOnInit() {
        // A lista depende da API e será carregada no navegador, após o SSR.
        if (isPlatformBrowser(this.platformId)) {
          this.carregarClubes();
        }
    }

    carregarClubes() {
    this.clubeService.getClubes().subscribe({
      next: (data) => {
        this.clubes = data;
      },
      error: (err) => {
        console.error('Erro ao carregar clubes:', err);
      }
    });
  }
}
