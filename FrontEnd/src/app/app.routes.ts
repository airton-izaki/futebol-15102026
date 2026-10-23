import { Routes }         from '@angular/router';
import { Home }           from './pages/home/home';
import { Clubes }         from './pages/clubes/clubes';
import { Classificacao }  from './pages/classificacao/classificacao';

export const routes: Routes = [
  {
    path: '',
    component: Home
  },
   {
    path: 'clubes',
    component: Clubes
   },
   {
    path: 'classificacao',
    component: Classificacao
   }
];
