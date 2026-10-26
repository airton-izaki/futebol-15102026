import { Component } from '@angular/core';
import { ClubeCreate } from '../../features/clubes/components/clube-create/clube-create';
import { ClubeList } from '../../features/clubes/components/clube-list/clube-list';



@Component({
  selector: 'app-clubes',
  imports: [
    ClubeCreate,
    ClubeList,
    ],
  templateUrl: './clubes.html',
  styleUrl: './clubes.css',
})
export class Clubes {

}
