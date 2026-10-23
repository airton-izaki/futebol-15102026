import { Component }                    from '@angular/core';

import { RouterLink, RouterLinkActive } from '@angular/router';
import { MenubarModule } from 'primeng/menubar';
import { MenuItem } from 'primeng/api';



@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [MenubarModule],
  templateUrl: './navbar.html',
  styleUrl: './navbar.css',
})
export class Navbar {
  items: MenuItem[] = [
    {
      label: 'Home',
      icon: 'pi pi-home',
      routerLink: '/'
    },
    {
      label: 'Clubes',
      icon: 'pi pi-shield',
      routerLink: '/clubes'
    },
    {
      label: 'Classificação',
      icon: 'pi pi-list',
      routerLink: '/classificacao'
    }
  ]
}
