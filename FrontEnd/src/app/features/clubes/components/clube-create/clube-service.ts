import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";


@Injectable({    providedIn: 'root'  })

export class ClubeService {
  private apiUrl = 'http://127.0.0.1:8001';

  constructor(private http: HttpClient) {}

  getEstados(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/localidades/estados`);
  }

  getMunicipios(ufId: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/localidades/estados/${ufId}/municipios`);
  }

  cadastrarClube(clube: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/clubes/`, clube);
  }
}
