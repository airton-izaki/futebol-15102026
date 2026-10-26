import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { ClubeService } from '../../../../services/clube-service';
import { TableModule } from 'primeng/table';



@Component({
  selector: 'app-clube-list',
  imports: [
    CommonModule,
    ButtonModule,
    CardModule,
    TableModule,
    ],
  templateUrl: './clube-list.html',
  styleUrl: './clube-list.css',
})
export class ClubeList implements OnInit {
    clubes: any[] = [];

    constructor(private clubeService: ClubeService) {}

    ngOnInit() {
        this.carregarClubes();
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
