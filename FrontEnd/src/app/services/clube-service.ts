import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";


@Injectable({    providedIn: 'root'  })

export class ClubeService {
  private apiUrl = 'http://127.0.0.1:8001';

  constructor(private http: HttpClient) {}

  // Buscar estados para o formulário
  getEstados(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/localidades/estados`);
  }

  // Buscar municípios do estado selecionado
  getMunicipios(ufId: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/localidades/estados/${ufId}/municipios`);
  }

  // Cadastrar novo clube (POST)
  cadastrarClube(clube: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/clubes/`, clube);
  }

  // Listar todos os clubes cadastrados (GET)
  getClubes(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/clubes/`);
  }

  getClube(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/clubes/${id}`);
  }

  atualizarClube(id: number, clube: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/clubes/${id}`, clube);
  }
}


