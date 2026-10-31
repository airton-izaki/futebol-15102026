import { Routes }         from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./pages/home/home').then((module) => module.Home),
    pathMatch: 'full'
  },
   {
    path: 'clubes/novo',
    loadComponent: () => import('./features/clubes/components/clube-create/clube-create').then((module) => module.ClubeCreate)
   },
   {
    path: 'clubes/editar/:id',
    loadComponent: () => import('./features/clubes/components/clube-create/clube-create').then((module) => module.ClubeCreate)
   },
   {
    path: 'clubes',
    loadComponent: () => import('./pages/clubes/clubes').then((module) => module.Clubes),
    pathMatch: 'full'
   },
   {
    path: 'classificacao',
    loadComponent: () => import('./pages/classificacao/classificacao').then((module) => module.Classificacao)
   }
];
