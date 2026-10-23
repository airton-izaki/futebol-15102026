import { Component } from '@angular/core';
import { ClubeCreate } from '../../features/clubes/components/clube-create/clube-create';





@Component({
  selector: 'app-clubes',
  imports: [ClubeCreate],
  templateUrl: './clubes.html',
  styleUrl: './clubes.css',
})
export class Clubes {

}
